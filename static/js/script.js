// ✅ Ensure variables are declared only once
if (typeof bookingStep === "undefined") {
    var bookingStep = 0;
    var bookingData = {};
}

// ✅ Disease List (10 major diseases with 3 clinics each)
if (typeof diseases === "undefined") {
    var diseases = {
        "Fever": [
            "City Hospital - Dr. Thomas (General Physician)",
            "City Hospital - Dr. Meera (Internal Medicine)",
            "City Hospital - Dr. Raj (General Physician)",
            "Apollo Clinic - Dr. Rina (Family Medicine)",
            "Apollo Clinic - Dr. Ajay (General Physician)",
            "Apollo Clinic - Dr. Sneha (General Medicine)",
            "Green Life - Dr. Anand (Physician)",
            "Green Life - Dr. Neha (General Medicine)",
            "Green Life - Dr. Kiran (Internal Medicine)"
        ],
        "Diabetes": [
            "Sunrise Clinic - Dr. Kavitha (Endocrinologist)",
            "Sunrise Clinic - Dr. Arun (Diabetologist)",
            "Sunrise Clinic - Dr. Nila (General Physician)",
            "Sugar Care Center - Dr. Vimal (Diabetologist)",
            "Sugar Care Center - Dr. Reshma (Endocrinologist)",
            "Sugar Care Center - Dr. Farhan (Internal Medicine)",
            "Metro Health - Dr. Isha (Endocrinologist)",
            "Metro Health - Dr. Ravi (Diabetologist)",
            "Metro Health - Dr. Sneha (General Medicine)"
        ],
        "Hypertension": [
            "Carewell Hospital - Dr. Veena (Cardiologist)",
            "Carewell Hospital - Dr. Mohan (General Physician)",
            "Carewell Hospital - Dr. Rekha (Internal Medicine)",
            "BP Wellness - Dr. Nikhil (Cardiologist)",
            "BP Wellness - Dr. Raji (Hypertension Specialist)",
            "BP Wellness - Dr. Karthik (General Physician)",
            "MediCare - Dr. Aarti (Cardiologist)",
            "MediCare - Dr. Satish (Physician)",
            "MediCare - Dr. Laya (Internal Medicine)"
        ],
        "Migraine": [
            "Neurology Care - Dr. Hari (Neurologist)",
            "Neurology Care - Dr. Deepa (Headache Specialist)",
            "Neurology Care - Dr. Vikram (Neurologist)",
            "Headache Relief Clinic - Dr. Anu (Neurologist)",
            "Headache Relief Clinic - Dr. Rajesh (Neuro Specialist)",
            "Headache Relief Clinic - Dr. Shreya (Pain Management)",
            "NeuroMed - Dr. Divya (Neurologist)",
            "NeuroMed - Dr. Kiran (Migraine Specialist)",
            "NeuroMed - Dr. Naveen (General Neurology)"
        ],
        "Eye Infection": [
            "Vision Hospital - Dr. Suresh (Ophthalmologist)",
            "Vision Hospital - Dr. Kavya (Eye Surgeon)",
            "Vision Hospital - Dr. Vinoth (Eye Specialist)",
            "Eye Care Center - Dr. Keerthi (Ophthalmologist)",
            "Eye Care Center - Dr. George (Eye Consultant)",
            "Eye Care Center - Dr. Lakshmi (Ophthalmologist)",
            "Ophthalmic Plus - Dr. Ramesh (Cornea Specialist)",
            "Ophthalmic Plus - Dr. Ayesha (Eye Surgeon)",
            "Ophthalmic Plus - Dr. Bala (Ophthalmologist)"
        ],
        "Skin Allergy": [
            "DermaLife - Dr. Nithya (Dermatologist)",
            "DermaLife - Dr. Raghav (Skin Specialist)",
            "DermaLife - Dr. Anjali (Allergy Specialist)",
            "Skin Solutions - Dr. Prakash (Dermatologist)",
            "Skin Solutions - Dr. Swetha (Skin Allergy Expert)",
            "Skin Solutions - Dr. Manoj (Immunologist)",
            "Healthy Skin Clinic - Dr. Dhanya (Dermatologist)",
            "Healthy Skin Clinic - Dr. Arjun (Allergy Specialist)",
            "Healthy Skin Clinic - Dr. Sana (Skin Specialist)"
        ],
        "Thyroid": [
            "Hormone Wellness - Dr. Reema (Endocrinologist)",
            "Hormone Wellness - Dr. Kishore (Thyroid Specialist)",
            "Hormone Wellness - Dr. Meenakshi (Hormone Expert)",
            "Endocrine Care - Dr. Dev (Endocrinologist)",
            "Endocrine Care - Dr. Ritu (Thyroid Specialist)",
            "Endocrine Care - Dr. Farooq (General Endocrinology)",
            "Thyroid Cure - Dr. Aarthi (Thyroid Consultant)",
            "Thyroid Cure - Dr. Imran (Endocrinologist)",
            "Thyroid Cure - Dr. Yash (Hormone Therapy Expert)"
        ],
        "Arthritis": [
            "Joint Relief Center - Dr. Sanjay (Rheumatologist)",
            "Joint Relief Center - Dr. Priya (Ortho-Rheumo)",
            "Joint Relief Center - Dr. Abhinav (Orthopedic)",
            "Ortho Life - Dr. Swaminathan (Orthopedic Surgeon)",
            "Ortho Life - Dr. Isha (Joint Specialist)",
            "Ortho Life - Dr. Mani (Physiotherapist)",
            "Bone & Joint Care - Dr. Rekha (Ortho-Rheumatology)",
            "Bone & Joint Care - Dr. Aditya (Bone Specialist)",
            "Bone & Joint Care - Dr. Nidhi (Ortho Expert)"
        ],
        "Asthma": [
            "Lung Health - Dr. Parth (Pulmonologist)",
            "Lung Health - Dr. Jaya (Respiratory Specialist)",
            "Lung Health - Dr. Varun (Chest Physician)",
            "Breathe Easy - Dr. Snehal (Pulmonologist)",
            "Breathe Easy - Dr. Aravind (Asthma Expert)",
            "Breathe Easy - Dr. Radhika (Allergy Specialist)",
            "Pulmonology Plus - Dr. Dinesh (Pulmonologist)",
            "Pulmonology Plus - Dr. Shalini (Respiratory Therapist)",
            "Pulmonology Plus - Dr. Mohit (Chest Specialist)"
        ],
        "Dental Pain": [
            "Smile Dental - Dr. Krishna (Dentist)",
            "Smile Dental - Dr. Anusha (Dental Surgeon)",
            "Smile Dental - Dr. Rakesh (Oral Specialist)",
            "Tooth Care Clinic - Dr. Geetha (Orthodontist)",
            "Tooth Care Clinic - Dr. Shyam (Prosthodontist)",
            "Tooth Care Clinic - Dr. Neeraja (Endodontist)",
            "Oral Health Center - Dr. Vinay (Dental Surgeon)",
            "Oral Health Center - Dr. Lavanya (Cosmetic Dentist)",
            "Oral Health Center - Dr. Ashwin (Oral & Maxillofacial)"
        ]
    }
    ;
}

// ✅ Toggle Menu (☰)
function toggleMenu() {
    const menu = document.getElementById("menu-items");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}

// ✅ Toggle Chatbot (💬)
function toggleChatbot() {
    const chatbotContainer = document.getElementById("chatbot-container");
    chatbotContainer.style.display = chatbotContainer.style.display === "none" ? "block" : "none";

    if (chatbotContainer.style.display === "block") {
        showInitialOptions();
    }
}

function startBooking() {
    bookingStep = 1;
    bookingData = { option: "Book Appointment" };
    appendMessage("Chatbot", "What is your name?");
}


// ✅ Show Initial Options (Booking & Disease Info)
function showInitialOptions() {
    appendMessage("Chatbot", "Hello! What do you want to do?");
    appendMessage("Chatbot", `
        <button class="btn btn-sm btn-primary m-1" onclick="startBooking()">📅 Book Appointment</button>
        <button class="btn btn-sm btn-info m-1" onclick="startDiseaseLookup()">🔍 Know About Diseases</button>
    `);
}




// ✅ Function to Send Message
function sendMessage() {
    const inputField = document.getElementById("chat-input");
    const userMessage = inputField.value.trim();
    if (userMessage === "") return;

    appendMessage("You", userMessage);

    if (bookingStep > 0) {
        handleBookingResponse(userMessage);
    } else if (bookingStep === -1) {
        handleDiseaseResponse(userMessage);
    } else {
        appendMessage("Chatbot", "Please select an option first.");
    }

    inputField.value = "";
}



// ✅ Function to Handle Booking Flow
function handleBookingResponse(userInput) {
    if (bookingStep === 1) {
        if (userInput.length < 3) {
            appendMessage("Chatbot", "❌ Name must be at least 3 letters. Try again.");
            return;
        }
        bookingData.name = userInput;
        appendMessage("Chatbot", "What is your email?");
        bookingStep = 2;
    } else if (bookingStep === 2) {
        if (!userInput.includes("@") || !userInput.includes(".")) {
            appendMessage("Chatbot", "❌ Enter a valid email.");
            return;
        }
        bookingData.email = userInput;
        appendMessage("Chatbot", "What disease do you need an appointment for?");
        showDiseaseOptions();
        bookingStep = 3;
    } else if (bookingStep === 3) {
        if (diseases[userInput]) {
            bookingData.disease = userInput;
            showClinicOptions(userInput);
            bookingStep = 4;
        } else {
            bookingData.disease = userInput;
            appendMessage("Chatbot", "Please enter your preferred clinic location.");
            bookingStep = 4;
        }
    } else if (bookingStep === 4) {
        bookingData.clinic = userInput;
        appendMessage("Chatbot", "What date do you prefer? (e.g., tmrw, next week, YYYY-MM-DD)");
        bookingStep = 5;
    } else if (bookingStep === 5) {
        bookingData.date = convertToDate(userInput);
        appendMessage("Chatbot", "Select a time slot:");
        showTimeOptions();  // 🔴 Error Happens Here
        bookingStep = 6;
    }
    
        else if (bookingStep === 6) {
        bookingData.time = userInput;
        completeBooking();
    }
}
function showTimeOptions() {
    let times = ["09:00 AM", "10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM", "04:00 PM", "06:00 PM", "07:00 PM"];
    let buttons = times.map(time => 
        `<button class="btn btn-sm btn-success m-1" onclick="handleBookingResponse('${time}')">${time}</button>`
    ).join("");

    // Check if chat container exists
    const chatContainer = document.getElementById("chat-messages");
    if (!chatContainer) {
        console.error("Chat container not found.");
        return;
    }

    appendMessage("Chatbot", `Select a time slot:<br> ${buttons}`);
}


// Function to Convert NLP Dates (e.g., "tmrw", "next week") to YYYY-MM-DD Format
function convertToDate(userInput) {
    let today = new Date();
    let newDate;

    if (userInput.toLowerCase() === "tmrw") {
        newDate = new Date(today);
        newDate.setDate(today.getDate() + 1);
    } else if (userInput.toLowerCase().includes("next week")) {
        newDate = new Date(today);
        newDate.setDate(today.getDate() + 7);
    } else if (userInput.toLowerCase().includes("next next day")) {
        newDate = new Date(today);
        newDate.setDate(today.getDate() + 2);
    } else if (userInput.toLowerCase().includes("yesterday")) {
        newDate = new Date(today);
        newDate.setDate(today.getDate() - 1);
    } else {
        newDate = new Date(userInput);
    }

    return newDate.toISOString().split("T")[0];  // Returns date in YYYY-MM-DD format
}

function showAppointmentModal() {
    let modalElement = document.getElementById('appointmentModal');

    if (modalElement) {
        let modal = new bootstrap.Modal(modalElement, {
            backdrop: 'static',  // Prevent closing by clicking outside
            keyboard: false      // Prevent closing with keyboard
        });
        modal.show();
    } else {
        console.error("❌ Error: Modal element not found in HTML.");
    }
}

function completeBooking() {
    console.log("Sending data to Flask:", bookingData);

    fetch("/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams(bookingData),
    })
    .then(response => response.json())
    .then(data => {
        appendMessage("Chatbot", `✅ Appointment confirmed!`);
        showAppointmentModal();  // 🔴 Error Happens Here
        showInitialOptions();
    })
    .catch(error => {
        console.error("Error:", error);
        appendMessage("Chatbot", "⚠️ Error booking appointment. Try again.");
    });

    bookingStep = 0;
}


// ✅ Show Disease Options
function showDiseaseOptions() {
    let buttons = Object.keys(diseases).map(disease => 
        `<button class="btn btn-sm btn-info m-1" onclick="handleBookingResponse('${disease}')">${disease}</button>`
    ).join("");
    appendMessage("Chatbot", buttons);
}

// ✅ Show Clinic Options Based on Disease
function showClinicOptions(disease) {
    let buttons = diseases[disease].map(clinic => 
        `<button class="btn btn-sm btn-warning m-1" onclick="handleBookingResponse('${clinic}')">${clinic}</button>`
    ).join("");
    appendMessage("Chatbot", `Select a clinic for ${disease}: <br>` + buttons);
}

// ✅ Append Messages to Chat Window
function appendMessage(sender, message) {
    const chatMessages = document.getElementById("chat-messages");
    const messageElement = document.createElement("div");
    messageElement.classList.add("chat-message", sender === "You" ? "user-message" : "bot-message");

    messageElement.innerHTML = `<div class="chat-bubble">${message}</div>`;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// ✅ Start Disease Lookup when clicking "Know About Diseases"
function startDiseaseLookup() {
    appendMessage("Chatbot", "Please enter the disease name.");
    bookingStep = -1;  // Set step to handle disease lookup
}

// ✅ Handle Disease Query and Fetch from Flask API
function handleDiseaseResponse(userInput) {
    let diseaseData = {
        option: "Know About Diseases",
        disease_query: userInput
    };

    console.log("Sending disease query to Flask:", diseaseData);

    fetch("/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams(diseaseData),
    })
    .then(response => response.json())
    .then(data => {
        appendMessage("Chatbot", `🩺 <b>Disease Info for ${userInput}:</b><br>${data.response}`);
        showInitialOptions();  // Return to main menu after response
    })
    .catch(error => {
        console.error("Error fetching disease info:", error);
        appendMessage("Chatbot", "⚠️ Error retrieving disease details. Try again.");
    });
}


function handleUserMessage() {
    const inputField = document.getElementById("chat-input");
    const userMessage = inputField.value.trim();
    const chatContainer = document.getElementById("chat-messages");

    if (!userMessage) return;

    // Display user message
    let userMsgDiv = document.createElement("div");
    userMsgDiv.classList.add("chat-message", "user-message");
    userMsgDiv.innerHTML = userMessage;
    chatContainer.appendChild(userMsgDiv);

    // Check if user was asked for a disease name
    if (sessionStorage.getItem("awaitingDiseaseInput") === "true") {
        sessionStorage.removeItem("awaitingDiseaseInput"); // Reset flag
        fetchDiseaseDetails(userMessage);
    } else {
        // Handle other chatbot messages
        let botReply = document.createElement("div");
        botReply.classList.add("chat-message", "bot-message");
        botReply.innerHTML = "I'm not sure how to respond to that.";
        chatContainer.appendChild(botReply);
    }

    inputField.value = ""; // Clear input field
}

