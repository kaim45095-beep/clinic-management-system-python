# ============================
# File paths used in the system
# ============================
DOCTOR_LOG = 'doctorlog.txt'
PATIENTS_FILE = "patients.txt"
APPOINTMENTS_FILE = "appointments.txt"
MEDICAL_RECORDS_FILE = "medrecords.txt"
DOCTOR_SCHEDULE_FILE = "doctor_schedule.txt"
OBSERVATION_FILE = "observations.txt"

# ============================
# Read data from a file
# ============================
def read_data(filename):
    """
    Reads a file and returns a list of records.
    """
    # Step 1: Try to open and read the file
    try:
        with open(filename, "r") as file:
            # Step 2: Split each line into a list and return all records
            return [line.strip().split(",") for line in file.readlines()]
    except FileNotFoundError:
        # Step 3: If file not found, return empty list
        print(f"❌ Error 102: {filename} file not found.")
        return []

# ============================
# Save data to a file
# ============================
def save_data(filename, data):
    """
    Writes a list of records to a file.
    """
    # Step 1: Try to open the file for writing
    try:
        with open(filename, "w") as file:
            # Step 2: Write each record as a comma-separated line
            for record in data:
                file.write(",".join(record) + "\n")
    except Exception as e:
        # Step 3: Handle any write errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

# ============================
# View patient observations
# ============================
def view_observations():
    """
    Displays observations for a specific patient on a specific date.
    """
    # Step 1: Get patient ID and date from user
    patient_id = input("Enter Patient ID: ").strip()
    date = input("Enter date (DDMMYYYY): ").strip()

    # Step 2: Validate input
    if not patient_id or not date:
        print("❌ Error 103: Patient ID and date are required.")
        return

    # Step 3: Read all observation records
    all_records = read_data(OBSERVATION_FILE)

    # Step 4: Filter records matching patient ID and date
    patient_records = [record for record in all_records if len(record) >= 5 and record[0] == patient_id and record[1] == date]

    # Step 5: Display results
    if not patient_records:
        print("No observation found for this patient or date.")
    else:
        print("\nOBSERVATIONS:")
        print("------------------")
        for record in patient_records:
            print(f"Date: {record[1]}")
            print(f"BP: {record[2]}")
            print(f"Pulse: {record[3]}")
            print(f"Temp: {record[4]}")
            print("-------------------")

# ============================
# View medical history
# ============================
def view_medical_history():
    """
    Displays all medical records for a specific patient.
    """
    # Step 1: Get patient ID from user
    patient_id = input("Enter Patient ID: ").strip()

    # Step 2: Validate input
    if not patient_id:
        print("❌ Error 103: Patient ID is required.")
        return

    # Step 3: Read all medical records
    all_records = read_data(MEDICAL_RECORDS_FILE)

    # Step 4: Filter records for the given patient
    patient_records = [record for record in all_records if len(record) >= 6 and record[0] == patient_id]

    # Step 5: Display results
    if not patient_records:
        print("No medical records found for this patient.")
    else:
        print("\nMEDICAL HISTORY:")
        print("================")
        for record in patient_records:
            print(f"Doctor ID: {record[1]}")
            print(f"Date: {record[2]}")
            print(f"Diagnosis: {record[3]}")
            print(f"Medicine(s): {record[4]}")
            print(f"Treatment Plan: {record[5]}")
            print("----------------")

# ============================
# Update patient medical record
# ============================
def update_patient_record(doctor_id):
    """
    Adds a new medical record for a patient.
    """
    # Step 1: Get patient ID
    patient_id = input("Enter Patient ID: ").strip()

    # Step 2: Validate patient ID
    if not patient_id:
        print("❌ Error 101: Invalid input. Patient ID is required.")
        return

    # Step 3: Check if patient exists
    patients = read_data(PATIENTS_FILE)
    found = any(patient[0] == f"Patient ID:{patient_id}" for patient in patients)

    if not found:
        print("❌ Error 103: Patient ID not found.")
        return

    # Step 4: Get medical details
    date = input("Enter date (DDMMYYYY): ").strip()
    diagnosis = input("Diagnosis: ").strip()
    medicines = input("Medicine(s): ").strip()
    treatment = input("Treatment Plan: ").strip()

    # Step 5: Validate required fields
    if not diagnosis or not medicines:
        print("❌ Error 101: Invalid input. Diagnosis and Medicine(s) are required.")
        return

    # Step 6: Create and save new record
    new_record = [patient_id, doctor_id, date, diagnosis, medicines, treatment]
    existing_records = read_data(MEDICAL_RECORDS_FILE)
    existing_records.append(new_record)
    save_data(MEDICAL_RECORDS_FILE, existing_records)
    print("✅ Record updated successfully!")

# ============================
# View doctor's appointments
# ============================
def view_appointments(doctor_id):
    """
    Displays all appointments scheduled for the logged-in doctor.
    """
    # Step 1: Read all appointments
    all_appointments = read_data(APPOINTMENTS_FILE)

    # Step 2: Filter appointments for this doctor
    my_appointments = [appt for appt in all_appointments if len(appt) >= 5 and appt[2] == doctor_id]

    # Step 3: Display results
    if not my_appointments:
        print("No appointments scheduled.")
    else:
        print("\nYOUR APPOINTMENTS:")
        print("==================")
        print("Patient ID  |  Date      |  Time     ")
        print("--------------------------------------------")
        for appt in my_appointments:
            print(f"{appt[1]:<11} | {appt[3]:<10} | {appt[4]:<8}")

# ============================
# Manage doctor's availability
# ============================
def manage_availability(doctor_id):
    """
    Allows the doctor to block or unblock specific dates.
    """
    # Step 1: Read schedule data
    schedules = read_data(DOCTOR_SCHEDULE_FILE)

    # Step 2: Filter schedule for this doctor
    my_schedule = [sched for sched in schedules if sched[0] == doctor_id]

    # Step 3: Display current blocked dates
    if my_schedule:
        print("\nCURRENT BLOCKED DATES:")
        for i, sched in enumerate(my_schedule, 1):
            print(f"{i}. {sched[1]} - {sched[2]}")
    else:
        print("No dates currently blocked.")

    # Step 4: Show menu options
    print("\n1. Block a date")
    print("2. Unblock a date")
    print("3. Back to menu")
    choice = input("Enter choice: ").strip()

    # Step 5: Handle block date
    if choice == "1":
        date = input("Enter date to block (DDMMYYYY): ").strip()
        if date:
            schedules.append([doctor_id, date, "blocked"])
            save_data(DOCTOR_SCHEDULE_FILE, schedules)
            print("✅ Date blocked successfully!")
        else:
            print("❌ Error 101: Invalid input. Date is required.")

    # Step 6: Handle unblock date
    elif choice == "2":
        if not my_schedule:
            print("No dates to unblock.")
            return
        try:
            date_num = int(input("Enter number of date to unblock: "))
            if 1 <= date_num <= len(my_schedule):
                date_to_remove = my_schedule[date_num - 1][1]
                new_schedules = [sched for sched in schedules if not (sched[0] == doctor_id and sched[1] == date_to_remove)]
                save_data(DOCTOR_SCHEDULE_FILE, new_schedules)
                print("✅ Date unblocked successfully!")
            else:
                print("❌ Error 101: Invalid selection.")
        except ValueError:
            print("❌ Error 101: Please enter a valid number.")

    # Step 7: Handle back to menu
    elif choice == "3":
        return
    else:
        print("❌ Error 101: Invalid input.")

# ============================
# Doctor login
# ============================
def doctor_login():
    """
    Authenticates a doctor using credentials from the log file.
    """
    # Step 1: Prompt the doctor to enter username and password
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Step 2: Validate input
    if not username or not password:
        print("❌ Error 101: Invalid input. Username and password are required.")
        return None

    try:
        # Step 3: Open the doctor log file
        with open(DOCTOR_LOG, 'r') as file:
            # Step 4: Read each line and check credentials
            for line in file:
                stored_user, stored_pass = line.strip().split(',')
                if username == stored_user and password == stored_pass:
                    # Step 5: If credentials match, return doctor ID
                    print("✅ Login successful.")
                    return stored_user

        # Step 6: If no match found, show error
        print("❌ Invalid username or password.")
        return None

    except FileNotFoundError:
        # Step 7: Handle missing log file
        print("❌ Error 102: doctorlog.txt file not found.")
        return None
    
def doctor_menu(doctor_id):
    """
    Displays the main menu for the doctor and handles their choices.
    """
    while True:
        # Step 1: Show menu options
        print("\n===== DOCTOR MENU =====")
        print("1. View Patient Observations")
        print("2. View Patient Medical History")
        print("3. Update Patient Record")
        print("4. View My Appointments")
        print("5. Manage Availability")
        print("6. Logout")
        print("========================")

        try:
            # Step 2: Get user's choice
            choice = int(input("Enter your choice: "))
        except ValueError:
            # Step 3: Handle non-numeric input
            print("❌ Error 101: Invalid input. Please enter a number between 1 and 6.")
            continue

        # Step 4: Execute corresponding function
        if choice == 1:
            view_observations()
        elif choice == 2:
            view_medical_history()
        elif choice == 3:
            update_patient_record(doctor_id)
        elif choice == 4:
            view_appointments(doctor_id)
        elif choice == 5:
            manage_availability(doctor_id)
        elif choice == 6:
            # Step 5: Exit the menu loop
            print("🔒 Logging out...")
            break
        else:
            # Step 6: Handle invalid menu choice
            print("❌ Error 101: Invalid choice. Please enter a number between 1 and 6.")

