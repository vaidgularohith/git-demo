<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hospital Management System</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }

        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }

        .header p {
            font-size: 1.1em;
            opacity: 0.9;
        }

        .tabs {
            display: flex;
            background: #f5f5f5;
            border-bottom: 2px solid #ddd;
        }

        .tab-btn {
            flex: 1;
            padding: 15px;
            border: none;
            background: #f5f5f5;
            cursor: pointer;
            font-size: 1em;
            font-weight: 500;
            transition: all 0.3s;
            border-bottom: 3px solid transparent;
        }

        .tab-btn:hover {
            background: #e8e8e8;
        }

        .tab-btn.active {
            background: white;
            color: #667eea;
            border-bottom-color: #667eea;
        }

        .tab-content {
            display: none;
            padding: 30px;
        }

        .tab-content.active {
            display: block;
            animation: fadeIn 0.3s;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        .form-row.full {
            grid-template-columns: 1fr;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #333;
        }

        input, select, textarea {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1em;
            font-family: inherit;
            transition: border-color 0.3s;
        }

        input:focus, select:focus, textarea:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
        }

        textarea {
            resize: vertical;
            min-height: 100px;
        }

        .btn-group {
            display: flex;
            gap: 10px;
            margin-top: 30px;
        }

        button {
            padding: 12px 30px;
            border: none;
            border-radius: 5px;
            font-size: 1em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }

        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            flex: 1;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .btn-secondary {
            background: #e0e0e0;
            color: #333;
        }

        .btn-secondary:hover {
            background: #d0d0d0;
        }

        .btn-delete {
            background: #ff6b6b;
            color: white;
        }

        .btn-delete:hover {
            background: #ee5a52;
        }

        .table-container {
            margin-top: 30px;
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
        }

        th {
            background: #667eea;
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }

        td {
            padding: 12px 15px;
            border-bottom: 1px solid #ddd;
        }

        tr:hover {
            background: #f9f9f9;
        }

        .action-btn {
            padding: 6px 12px;
            margin: 0 3px;
            font-size: 0.9em;
        }

        .success-message {
            background: #d4edda;
            color: #155724;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            display: none;
        }

        .error-message {
            background: #f8d7da;
            color: #721c24;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            display: none;
        }

        .required {
            color: #ff0000;
        }

        @media (max-width: 768px) {
            .form-row {
                grid-template-columns: 1fr;
            }

            .tabs {
                flex-wrap: wrap;
            }

            .header h1 {
                font-size: 1.8em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏥 Hospital Management System</h1>
            <p>Manage Patients, Doctors, and Appointments</p>
        </div>

        <div class="tabs">
            <button class="tab-btn active" onclick="openTab(event, 'patients')">Patients</button>
            <button class="tab-btn" onclick="openTab(event, 'doctors')">Doctors</button>
            <button class="tab-btn" onclick="openTab(event, 'appointments')">Appointments</button>
        </div>

        <!-- PATIENTS TAB -->
        <div id="patients" class="tab-content active">
            <h2>Patient Registration</h2>
            
            <div class="success-message" id="patientSuccess">Patient added successfully!</div>
            <div class="error-message" id="patientError"></div>

            <form id="patientForm" onsubmit="addPatient(event)">
                <div class="form-row">
                    <div class="form-group">
                        <label>Patient ID <span class="required">*</span></label>
                        <input type="text" id="patientId" required placeholder="PID001">
                    </div>
                    <div class="form-group">
                        <label>Full Name <span class="required">*</span></label>
                        <input type="text" id="patientName" required placeholder="John Doe">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label>Age <span class="required">*</span></label>
                        <input type="number" id="patientAge" required placeholder="25">
                    </div>
                    <div class="form-group">
                        <label>Gender <span class="required">*</span></label>
                        <select id="patientGender" required>
                            <option value="">Select Gender</option>
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label>Phone Number <span class="required">*</span></label>
                        <input type="tel" id="patientPhone" required placeholder="1234567890">
                    </div>
                    <div class="form-group">
                        <label>Email <span class="required">*</span></label>
                        <input type="email" id="patientEmail" required placeholder="john@example.com">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label>Address <span class="required">*</span></label>
                        <input type="text" id="patientAddress" required placeholder="123 Main Street">
                    </div>
                    <div class="form-group">
                        <label>Blood Type</label>
                        <select id="patientBloodType">
                            <option value="">Select Blood Type</option>
                            <option value="A+">A+</option>
                            <option value="A-">A-</option>
                            <option value="B+">B+</option>
                            <option value="B-">B-</option>
                            <option value="O+">O+</option>
                            <option value="O-">O-</option>
                            <option value="AB+">AB+</option>
                            <option value="AB-">AB-</option>
                        </select>
                    </div>
                </div>

                <div class="form-row full">
                    <div class="form-group">
                        <label>Medical History</label>
                        <textarea id="patientHistory" placeholder="Enter any relevant medical history"></textarea>
                    </div>
                </div>

                <div class="btn-group">
                    <button type="submit" class="btn-primary">Add Patient</button>
                    <button type="reset" class="btn-secondary">Clear</button>
                </div>
            </form>

            <div class="table-container">
                <h3 style="margin-top: 30px; margin-bottom: 15px;">Patient Records</h3>
                <table id="patientTable">
                    <thead>
                        <tr>
                            <th>Patient ID</th>
                            <th>Name</th>
                            <th>Age</th>
                            <th>Phone</th>
                            <th>Email</th>
                            <th>Blood Type</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody></tbody>
                </table>
            </div>
        </div>

        <!-- DOCTORS TAB -->
        <div id="doctors" class="tab-content">
            <h2>Doctor Registration</h2>

            <div class="success-message" id="doctorSuccess">Doctor added successfully!</div>
            <div class="error-message" id="doctorError"></div>

            <form id="doctorForm" onsubmit="addDoctor(event)">
                <div class="form-row">
                    <div class="form-group">
                        <label>Doctor ID <span class="required">*</span></label>
                        <input type="text" id="doctorId" required placeholder="DOC001">
                    </div>
                    <div class="form-group">
                        <label>Full Name <span class="required">*</span></label>
                        <input type="text" id="doctorName" required placeholder="Dr. Smith">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label>Specialization <span class="required">*</span></label>
                        <input type="text" id="doctorSpecialization" required placeholder="Cardiology">
                    </div>
                    <div class="form-group">
                        <label>Qualification <span class="required">*</span></label>
                        <input type="text" id="doctorQualification" required placeholder="MBBS, MD">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label>Phone Number <span class="required">*</span></label>
                        <input type="tel" id="doctorPhone" required placeholder="1234567890">
                    </div>
                    <div class="form-group">
                        <label>Email <span class="required">*</span></label>
                        <input type="email" id="doctorEmail" required placeholder="doctor@hospital.com">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label>Department <span class="required">*</span></label>
                        <select id="doctorDepartment" required>
                            <option value="">Select Department</option>
                            <option value="Cardiology">Cardiology</option>
                            <option value="Neurology">Neurology</option>
                            <option value="Orthopedics">Orthopedics</option>
                            <option value="Pediatrics">Pediatrics</option>
                            <option value="Surgery">Surgery</option>
                            <option value="General">General Medicine</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>License Number <span class="required">*</span></label>
                        <input type="text" id="doctorLicense" required placeholder="LIC123456">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label>Available Hours</label>
                        <input type="text" id="doctorHours" placeholder="9:00 AM - 5:00 PM">
                    </div>
                    <div class="form-group">
                        <label>Status</label>
                        <select id="doctorStatus">
                            <option value="Active">Active</option>
                            <option value="On Leave">On Leave</option>
                            <option value="Inactive">Inactive</option>
                        </select>
                    </div>
                </div>

                <div class="btn-group">
                    <button type="submit" class="btn-primary">Add Doctor</button>
                    <button type="reset" class="btn-secondary">Clear</button>
                </div>
            </form>

            <div class="table-container">
                <h3 style="margin-top: 30px; margin-bottom: 15px;">Doctor Records</h3>
                <table id="doctorTable">
                    <thead>
                        <tr>
                            <th>Doctor ID</th>
                            <th>Name</th>
                            <th>Specialization</th>
                            <th>Department</th>
                            <th>Phone</th>
                            <th>Status</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody></tbody>
                </table>
            </div>
        </div>

        <!-- APPOINTMENTS TAB -->
        <div id="appointments" class="tab-content">
            <h2>Appointment Booking</h2>

            <div class="success-message" id="appointmentSuccess">Appointment booked successfully!</div>
            <div class="error-message" id="appointmentError"></div>

            <form id="appointmentForm" onsubmit="addAppointment(event)">
                <div class="form-row">
                    <div class="form-group">
                        <label>Appointment ID <span class="required">*</span></label>
                        <input type="text" id="appointmentId" required placeholder="APT001">
                    </div>
                    <div class="form-group">
                        <label>Patient ID <span class="required">*</span></label>
                        <input type="text" id="appointmentPatientId" required placeholder="PID001">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label>Doctor ID <span class="required">*</span></label>
                        <input type="text" id="appointmentDoctorId" required placeholder="DOC001">
                    </div>
                    <div class="form-group">
                        <label>Appointment Date <span class="required">*</span></label>
                        <input type="date" id="appointmentDate" required>
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label>Appointment Time <span class="required">*</span></label>
                        <input type="time" id="appointmentTime" required>
                    </div>
                    <div class="form-group">
                        <label>Type <span class="required">*</span></label>
                        <select id="appointmentType" required>
                            <option value="">Select Type</option>
                            <option value="Consultation">Consultation</option>
                            <option value="Follow-up">Follow-up</option>
                            <option value="Surgery">Surgery</option>
                            <option value="Checkup">Checkup</option>
                        </select>
                    </div>
                </div>

                <div class="form-row full">
                    <div class="form-group">
                        <label>Reason for Visit</label>
                        <textarea id="appointmentReason" placeholder="Enter reason for appointment"></textarea>
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label>Status</label>
                        <select id="appointmentStatus">
                            <option value="Scheduled">Scheduled</option>
                            <option value="Confirmed">Confirmed</option>
                            <option value="Completed">Completed</option>
                            <option value="Cancelled">Cancelled</option>
                        </select>
                    </div>
                </div>

                <div class="btn-group">
                    <button type="submit" class="btn-primary">Book Appointment</button>
                    <button type="reset" class="btn-secondary">Clear</button>
                </div>
            </form>

            <div class="table-container">
                <h3 style="margin-top: 30px; margin-bottom: 15px;">Appointment Records</h3>
                <table id="appointmentTable">
                    <thead>
                        <tr>
                            <th>Appointment ID</th>
                            <th>Patient ID</th>
                            <th>Doctor ID</th>
                            <th>Date</th>
                            <th>Time</th>
                            <th>Type</th>
                            <th>Status</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody></tbody>
                </table>
            </div>
        </div>
    </div>

    <script>
        // Initialize data arrays from localStorage
        let patients = JSON.parse(localStorage.getItem('patients')) || [];
        let doctors = JSON.parse(localStorage.getItem('doctors')) || [];
        let appointments = JSON.parse(localStorage.getItem('appointments')) || [];

        // Tab switching function
        function openTab(evt, tabName) {
            const contents = document.querySelectorAll('.tab-content');
            contents.forEach(content => content.classList.remove('active'));

            const buttons = document.querySelectorAll('.tab-btn');
            buttons.forEach(button => button.classList.remove('active'));

            document.getElementById(tabName).classList.add('active');
            evt.currentTarget.classList.add('active');
        }

        // Show message function
        function showMessage(elementId, message, isSuccess = true) {
            const element = document.getElementById(elementId);
            element.textContent = message;
            element.style.display = 'block';
            setTimeout(() => {
                element.style.display = 'none';
            }, 3000);
        }

        // Add Patient
        function addPatient(event) {
            event.preventDefault();

            const patient = {
                id: document.getElementById('patientId').value,
                name: document.getElementById('patientName').value,
                age: document.getElementById('patientAge').value,
                gender: document.getElementById('patientGender').value,
                phone: document.getElementById('patientPhone').value,
                email: document.getElementById('patientEmail').value,
                address: document.getElementById('patientAddress').value,
                bloodType: document.getElementById('patientBloodType').value,
                history: document.getElementById('patientHistory').value,
                registrationDate: new Date().toLocaleDateString()
            };

            // Check for duplicate ID
            if (patients.some(p => p.id === patient.id)) {
                showMessage('patientError', 'Patient ID already exists!', false);
                return;
            }

            patients.push(patient);
            localStorage.setItem('patients', JSON.stringify(patients));
            document.getElementById('patientForm').reset();
            showMessage('patientSuccess', 'Patient added successfully!');
            displayPatients();
        }

        // Display Patients
        function displayPatients() {
            const tbody = document.querySelector('#patientTable tbody');
            tbody.innerHTML = '';

            patients.forEach(patient => {
                const row = tbody.insertRow();
                row.innerHTML = `
                    <td>${patient.id}</td>
                    <td>${patient.name}</td>
                    <td>${patient.age}</td>
                    <td>${patient.phone}</td>
                    <td>${patient.email}</td>
                    <td>${patient.bloodType || 'N/A'}</td>
                    <td><button class="btn-primary action-btn" onclick="editPatient('${patient.id}')">Edit</button>
                    <button class="btn-delete action-btn" onclick="deletePatient('${patient.id}')">Delete</button></td>
                `;
            });
        }

        // Delete Patient
        function deletePatient(id) {
            if (confirm('Are you sure you want to delete this patient?')) {
                patients = patients.filter(p => p.id !== id);
                localStorage.setItem('patients', JSON.stringify(patients));
                displayPatients();
                showMessage('patientSuccess', 'Patient deleted successfully!');
            }
        }

        // Add Doctor
        function addDoctor(event) {
            event.preventDefault();

            const doctor = {
                id: document.getElementById('doctorId').value,
                name: document.getElementById('doctorName').value,
                specialization: document.getElementById('doctorSpecialization').value,
                qualification: document.getElementById('doctorQualification').value,
                phone: document.getElementById('doctorPhone').value,
                email: document.getElementById('doctorEmail').value,
                department: document.getElementById('doctorDepartment').value,
                license: document.getElementById('doctorLicense').value,
                hours: document.getElementById('doctorHours').value,
                status: document.getElementById('doctorStatus').value
            };

            // Check for duplicate ID
            if (doctors.some(d => d.id === doctor.id)) {
                showMessage('doctorError', 'Doctor ID already exists!', false);
                return;
            }

            doctors.push(doctor);
            localStorage.setItem('doctors', JSON.stringify(doctors));
            document.getElementById('doctorForm').reset();
            showMessage('doctorSuccess', 'Doctor added successfully!');
            displayDoctors();
        }

        // Display Doctors
        function displayDoctors() {
            const tbody = document.querySelector('#doctorTable tbody');
            tbody.innerHTML = '';

            doctors.forEach(doctor => {
                const row = tbody.insertRow();
                row.innerHTML = `
                    <td>${doctor.id}</td>
                    <td>${doctor.name}</td>
                    <td>${doctor.specialization}</td>
                    <td>${doctor.department}</td>
                    <td>${doctor.phone}</td>
                    <td><span style="padding: 5px 10px; border-radius: 3px; background: ${doctor.status === 'Active' ? '#d4edda' : '#f8d7da'}; color: ${doctor.status === 'Active' ? '#155724' : '#721c24'}">${doctor.status}</span></td>
                    <td><button class="btn-primary action-btn" onclick="editDoctor('${doctor.id}')">Edit</button>
                    <button class="btn-delete action-btn" onclick="deleteDoctor('${doctor.id}')">Delete</button></td>
                `;
            });
        }

        // Delete Doctor
        function deleteDoctor(id) {
            if (confirm('Are you sure you want to delete this doctor?')) {
                doctors = doctors.filter(d => d.id !== id);
                localStorage.setItem('doctors', JSON.stringify(doctors));
                displayDoctors();
                showMessage('doctorSuccess', 'Doctor deleted successfully!');
            }
        }

        // Add Appointment
        function addAppointment(event) {
            event.preventDefault();

            const appointment = {
                id: document.getElementById('appointmentId').value,
                patientId: document.getElementById('appointmentPatientId').value,
                doctorId: document.getElementById('appointmentDoctorId').value,
                date: document.getElementById('appointmentDate').value,
                time: document.getElementById('appointmentTime').value,
                type: document.getElementById('appointmentType').value,
                reason: document.getElementById('appointmentReason').value,
                status: document.getElementById('appointmentStatus').value,
                bookedDate: new Date().toLocaleDateString()
            };

            // Check for duplicate ID
            if (appointments.some(a => a.id === appointment.id)) {
                showMessage('appointmentError', 'Appointment ID already exists!', false);
                return;
            }

            appointments.push(appointment);
            localStorage.setItem('appointments', JSON.stringify(appointments));
            document.getElementById('appointmentForm').reset();
            showMessage('appointmentSuccess', 'Appointment booked successfully!');
            displayAppointments();
        }

        // Display Appointments
        function displayAppointments() {
            const tbody = document.querySelector('#appointmentTable tbody');
            tbody.innerHTML = '';

            appointments.forEach(appointment => {
                const row = tbody.insertRow();
                const statusColor = appointment.status === 'Confirmed' ? '#d4edda' : appointment.status === 'Cancelled' ? '#f8d7da' : '#e2e3e5';
                const statusTextColor = appointment.status === 'Confirmed' ? '#155724' : appointment.status === 'Cancelled' ? '#721c24' : '#383d41';
                
                row.innerHTML = `
                    <td>${appointment.id}</td>
                    <td>${appointment.patientId}</td>
                    <td>${appointment.doctorId}</td>
                    <td>${appointment.date}</td>
                    <td>${appointment.time}</td>
                    <td>${appointment.type}</td>
                    <td><span style="padding: 5px 10px; border-radius: 3px; background: ${statusColor}; color: ${statusTextColor}">${appointment.status}</span></td>
                    <td><button class="btn-primary action-btn" onclick="editAppointment('${appointment.id}')">Edit</button>
                    <button class="btn-delete action-btn" onclick="deleteAppointment('${appointment.id}')">Delete</button></td>
                `;
            });
        }

        // Delete Appointment
        function deleteAppointment(id) {
            if (confirm('Are you sure you want to cancel this appointment?')) {
                appointments = appointments.filter(a => a.id !== id);
                localStorage.setItem('appointments', JSON.stringify(appointments));
                displayAppointments();
                showMessage('appointmentSuccess', 'Appointment cancelled successfully!');
            }
        }

        // Placeholder edit functions
        function editPatient(id) {
            alert('Edit functionality for Patient ' + id + ' will be implemented soon!');
        }

        function editDoctor(id) {
            alert('Edit functionality for Doctor ' + id + ' will be implemented soon!');
        }

        function editAppointment(id) {
            alert('Edit functionality for Appointment ' + id + ' will be implemented soon!');
        }

        // Initialize display on page load
        window.addEventListener('load', function() {
            displayPatients();
            displayDoctors();
            displayAppointments();
        });
    </script>
</body>
</html>
