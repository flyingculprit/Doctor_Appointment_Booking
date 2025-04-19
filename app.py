from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from mongo_utils import register_user, authenticate_user, get_user_profile, store_appointment, get_user_appointments, delete_appointment, update_user_diseases, update_user_profile, cleanup_duplicates, get_all_users, get_all_bookings
from api_utils import get_medical_info  # Corrected import
from datetime import datetime, timedelta
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv("SECRET_KEY")

@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/admin')
def admin():
    if 'username' not in session or session['username'] != 'admin@@00':
        return redirect(url_for('login'))

    filter_date = request.args.get('dateFilter')
    filter_name = request.args.get('nameFilter')

    users = get_all_users(filter_date, filter_name)
    bookings = get_all_bookings(filter_date, filter_name)

    return render_template('admin.html', users=users, bookings=bookings)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin@@00' and password == 'admin@@00':
            session['username'] = username
            return redirect(url_for('admin'))

        if authenticate_user(username, password):
            session['username'] = username
            return redirect(url_for('index'))

        return render_template('login.html', error="Invalid credentials. Please enter the correct credentials.")

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        diseases = request.form.get('diseases', '')  # Default to empty string if not provided

        if not all([name, username, email, phone, password]):
            return jsonify({"status": "error", "message": "All fields are required"}), 400

        if register_user(name, username, email, phone, password, diseases):  # Pass diseases to register_user
            session['username'] = username
            return redirect(url_for('index'))

        return jsonify({"status": "error", "message": "Username already exists"}), 409

    return render_template('signup.html')

@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))

    user = get_user_profile(session['username'])
    appointments = get_user_appointments(session['username'])
    print(appointments)  # Debug statement to check the appointments data
    return render_template('profile.html', user=user, appointments=appointments)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/profile_data')
def profile_data():
    user = get_user_profile(session['username'])
    return render_template('profile_data.html', user=user)

@app.route('/update_data', methods=['GET', 'POST'])
def update_data():
    if request.method == 'POST':
        new_diseases = request.form.get('diseases', '')
        if update_user_diseases(session['username'], new_diseases):
            flash("Profile updated successfully!", "success")
            return redirect(url_for('profile_data'))
    user = get_user_profile(session['username'])
    return render_template('update_data.html', user=user)

@app.route('/appointments_data')
def appointments_data():
    appointments = get_user_appointments(session['username'])
    return render_template('appointments_data.html', appointments=appointments)

@app.route('/delete_appointment/<string:appointment_id>', methods=['DELETE'])
def delete_appointment_route(appointment_id):
    if 'username' not in session:
        return jsonify({"success": False, "message": "Unauthorized"}), 401

    if delete_appointment(session['username'], appointment_id):
        return jsonify({"success": True, "message": "Appointment deleted successfully!"})
    else:
        return jsonify({"success": False, "message": "Failed to delete appointment."})

@app.route('/edit_diseases', methods=['POST'])
def edit_diseases():
    if 'username' not in session:
        return jsonify({"success": False, "message": "Unauthorized"}), 401

    new_diseases = request.form.get('diseases', '')

    if update_user_diseases(session['username'], new_diseases):
        flash("Diseases updated successfully!", "success")
        return redirect(url_for('profile'))

    return jsonify({"success": False, "message": "Failed to update diseases."}), 500

@app.route('/delete_disease', methods=['POST'])
def delete_disease():
    if 'username' not in session:
        return jsonify({"success": False, "message": "Unauthorized"}), 401

    disease_to_delete = request.form.get('disease', '').strip()
    user = get_user_profile(session['username'])
    if user:
        current_diseases = user['diseases'].split(',')
        new_diseases = ','.join([d for d in current_diseases if d.strip() != disease_to_delete.strip()])
        if update_user_diseases(session['username'], new_diseases):
            flash("Disease deleted successfully!", "success")
            return redirect(url_for('profile'))

    return jsonify({"success": False, "message": "Failed to delete disease."}), 500

@app.route('/chatbot', methods=['POST'])
def chatbot():
    option = request.form.get('option')

    if option == "Book Appointment":
        return handle_appointment_booking(request)

    elif option == "Know About Diseases":
        return handle_disease_info(request)

    return jsonify({"message": "Invalid request."})

@app.route('/get_disease_info')
def get_disease_info_api():
    disease_name = request.args.get("disease", "").strip()
    if not disease_name:
        return jsonify({"error": "No disease name provided"}), 400

    disease_info = get_medical_info(disease_name)
    return jsonify({"result": disease_info})

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    name = request.form.get('name')
    email = request.form.get('email')
    disease = request.form.get('disease')
    clinic = request.form.get('clinic')
    date = request.form.get('date')
    time = request.form.get('time')

    print(f"Name: {name}, Email: {email}, Disease: {disease}, Clinic: {clinic}, Date: {date}, Time: {time}")

    if not all([name, email, disease, clinic, date, time]):
        return jsonify({"success": False, "message": "All fields are required"}), 400

    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return jsonify({"success": False, "message": "Invalid date format. Use YYYY-MM-DD."}), 400

    store_appointment(session['username'], name, email, disease, clinic, date_obj, time)

    # Clean up duplicates after booking
    cleanup_duplicates()

    return jsonify({"success": True, "message": "Appointment booked successfully!"})

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
    if 'username' not in session:
        return jsonify({"success": False, "message": "Unauthorized"}), 401

    update_data = {}
    name = request.form.get('name')
    phone = request.form.get('phone')
    diseases = request.form.get('diseases')
    password = request.form.get('password')

    if name:
        update_data['name'] = name
    if phone:
        update_data['phone'] = phone
    if diseases:
        update_data['diseases'] = diseases
    if password:
        update_data['password'] = password  # Make sure to hash the password before storing it

    if update_data:
        if update_user_profile(session['username'], update_data):
            flash("Profile updated successfully!", "success")
            return redirect(url_for('profile'))
        else:
            return jsonify({"success": False, "message": "Failed to update profile."}), 500
    else:
        flash("No changes made to the profile.", "info")
        return redirect(url_for('profile'))

def handle_appointment_booking(request):
    name = request.form.get('name')
    email = request.form.get('email')
    disease = request.form.get('disease')
    clinic = request.form.get('clinic')  # Get the clinic name from the form
    date_str = request.form.get('date')
    time = request.form.get('time')

    if not all([name, email, disease, clinic, date_str, time]):
        return jsonify({"message": "All fields are required."}), 400

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return jsonify({"message": "Invalid date format. Use YYYY-MM-DD."}), 400

    store_appointment(session['username'], name, email, disease, clinic, date, time)

    return jsonify({"message": f"Appointment booked for {name} on {date_str} at {time}."})

def handle_disease_info(request):
    disease_query = request.form.get('disease_query')

    if not disease_query:
        return jsonify({"error": "Please enter a disease name"}), 400

    try:
        response = get_medical_info(disease_query)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": f"Failed to fetch disease info: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)