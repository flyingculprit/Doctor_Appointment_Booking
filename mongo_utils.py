
# mongo_utils.py

from pymongo import MongoClient
import os
from bson import ObjectId
from datetime import datetime

def get_mongo_client():
    client = MongoClient(os.getenv("MONGO_URI"))
    return client

def get_all_users(filter_date=None, filter_name=None):
    client = get_mongo_client()
    db = client['doctor_appointment_db']
    users_collection = db['users']
    
    query = {}
    if filter_date:
        query['date'] = filter_date
    if filter_name:
        query['name'] = filter_name
    
    users = list(users_collection.find(query, {'_id': 0, 'username': 1, 'name': 1, 'email': 1, 'phone': 1, 'diseases': 1}))
    return users

def get_all_bookings(filter_date=None, filter_name=None):
    client = get_mongo_client()
    db = client['doctor_appointment_db']
    bookings_collection = db['appointments']
    
    query = {}
    if filter_date:
        query['date'] = filter_date
    if filter_name:
        query['name'] = filter_name
    
    bookings = list(bookings_collection.find(query, {'_id': 0, 'name': 1, 'email': 1, 'disease': 1, 'clinic': 1, 'date': 1, 'time': 1, 'status': 1}))
    return bookings

def register_user(name, username, email, phone, password, diseases):
    client = get_mongo_client()
    db = client['doctor_appointment_db']  # Updated database name
    users_collection = db['users']  # Collection for user profiles
    
    if users_collection.find_one({'username': username}):
        return False
    
    users_collection.insert_one({
        'name': name,
        'username': username,
        'email': email,
        'phone': phone,
        'password': password,
        "diseases": diseases if diseases else ""  # Ensure diseases is always set
    })
    return True

def authenticate_user(username, password):
    client = get_mongo_client()
    db = client['doctor_appointment_db']  # Updated database name
    users_collection = db['users']  # Collection for user profiles
    
    user = users_collection.find_one({'username': username, 'password': password})
    return user is not None

def update_user_diseases(username, diseases):
    client = get_mongo_client()
    db = client['doctor_appointment_db']  # Updated database name
    user_collection = db['users']
    result = user_collection.update_one(
        {"username": username},
        {"$set": {"diseases": diseases}}
    )
    return result.modified_count > 0

def get_user_profile(username):
    client = get_mongo_client()
    db = client['doctor_appointment_db']  # Updated database name
    user_collection = db['users']
    user = user_collection.find_one({"username": username})
    if user:
        return {
            "name": user.get("name", ""),  # Use .get() to provide a default value if key is missing
            "username": user.get("username", ""),
            "email": user.get("email", ""),
            "phone": user.get("phone", ""),
            "diseases": user.get("diseases", "")  # Default to empty string if 'diseases' key is missing
        }
    return None

def store_appointment(username, name, email, disease, clinic, date, time):
    client = get_mongo_client()
    db = client['doctor_appointment_db']
    appointments_collection = db['appointments']
    
    appointment_id = ObjectId()  # Generate a unique ObjectId
    appointments_collection.insert_one({
        '_id': appointment_id,
        'username': username,
        'name': name,
        'email': email,
        'disease': disease,
        'clinic': clinic,  # Include the clinic name
        'date': date,
        'time': time,
        'status': 'Upcoming',
        'created_at': datetime.utcnow()  # Add a timestamp for sorting
    })

def update_user_profile(username, update_data):
    client = get_mongo_client()
    db = client['doctor_appointment_db']
    user_collection = db['users']
    result = user_collection.update_one(
        {"username": username},
        {"$set": update_data}
    )
    return result.modified_count > 0

def get_user_appointments(username):
    client = get_mongo_client()
    db = client['doctor_appointment_db']
    appointments_collection = db['appointments']
    
    appointments = list(appointments_collection.find({'username': username}, {'_id': 1, 'name': 1, 'email': 1, 'disease': 1, 'clinic': 1, 'date': 1, 'time': 1, 'status': 1, 'created_at': 1}).sort('created_at', -1))
    
    # Recalculate serial numbers
    for index, appt in enumerate(appointments, start=1):
        appt['sno'] = index
    
    return appointments

def delete_appointment(username, appointment_id):
    client = get_mongo_client()
    db = client['doctor_appointment_db']
    appointments_collection = db['appointments']
    
    result = appointments_collection.delete_one({'username': username, '_id': ObjectId(appointment_id)})
    return result.deleted_count > 0

def cleanup_duplicates():
    client = get_mongo_client()
    db = client['doctor_appointment_db']
    appointments_collection = db['appointments']

    pipeline = [
        {
            "$group": {
                "_id": {
                    "name": "$name",
                    "email": "$email",
                    "date": "$date",
                    "time": "$time"
                },
                "ids": {"$push": "$_id"},
                "count": {"$sum": 1}
            }
        },
        {
            "$match": {
                "count": {"$gt": 1}
            }
        }
    ]

    duplicates = list(appointments_collection.aggregate(pipeline))

    for duplicate in duplicates:
        ids = duplicate["ids"]
        # Keep the first entry and delete the rest
        for id_to_delete in ids[1:]:
            appointments_collection.delete_one({"_id": id_to_delete})