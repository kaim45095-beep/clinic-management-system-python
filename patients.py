# ============================
# Constants for file paths
# ============================
PATIENTS_FILE = 'patients.txt'
MEDICAL_RECORDS_FILE = 'medrecords.txt'
APPOINTMENTS_FILE = 'appointments.txt'
PAYMENTS_FILE = 'payments.txt'
PATIENTS_LOG = 'patientlog.txt'

# ============================
# View personal information
# ============================
def view_personal_info(patient_id):
    """
    Displays personal details of the patient.
    """
    # Step 1: Initialize flag
    found = False

    try:
        # Step 2: Open patient file and search for matching ID
        with open(PATIENTS_FILE, 'r') as file:
            for line in file:
                if f"Patient ID:{patient_id}," in line:
                    # Step 3: Display personal info
                    print("\n--- Personal Information ---")
                    print(line.strip())
                    found = True
                    break

        # Step 4: If not found, show message
        if not found:
            print("❌ Patient not found.")

    except FileNotFoundError:
        # Step 5: Handle missing file
        print("❌ Error 102: patients.txt not found.")
    except Exception as e:
        # Step 6: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

# ============================
# Update contact information
# ============================
def update_contact_info(patient_id):
    """
    Updates contact number, email, and address for a patient.
    """
    # Step 1: Initialize flag
    updated = False

    try:
        # Step 2: Read all patient records
        with open(PATIENTS_FILE, 'r') as file:
            lines = file.readlines()

        # Step 3: Open file to overwrite updated data
        with open(PATIENTS_FILE, 'w') as file:
            for line in lines:
                parts = line.strip().split(",")
                if f"Patient ID:{patient_id}" in line:
                    # Step 4: Prompt for new contact info with validation

                    # Validate contact number
                    while True:
                        try:
                            contact = int(input("Enter contact number: "))
                            break  # Exit loop if input is valid
                        except ValueError:
                            print("❌ Error 101: Invalid input. Please enter a valid integer for contact number.")

                    # Validate email format
                    while True:
                        email = input("Enter patient E-Mail: ").strip()
    
                        # Basic checks: must contain '@' and '.', and '@' must come before the last '.'
                        if "@" in email and "." in email and email.index("@") < email.rindex("."):
                            break
                        else:
                            print("❌ Error 101: Invalid email format. Please enter a valid email address (e.g., user@example.com).")

                    # Validate address
                    while True:
                        address = input("Enter address: ").strip()
                        if address:
                            break
                        print("❌ Error 101: Invalid input. Address cannot be empty.")

                    # Step 5: Write updated info
                    file.write(f"Patient ID:{patient_id},{parts[1]},{parts[2]},{parts[3]},Contact:{contact},E-Mail:{email},Address:{address}\n")
                    updated = True
                else:
                    file.write(line)

        # Step 6: Show result
        if updated:
            print("✅ Information updated.")

    except FileNotFoundError:
        # Step 7: Handle missing file
        print("❌ Error 102: patients.txt file not found.")

    except Exception as e:
        # Step 8: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

# ============================
# View appointments
# ============================
def view_appointments_patient(patient_id):
    """
    Displays all appointments for the patient.
    """
    # Step 1: Initialize flag
    found = False

    try:
        # Step 2: Read appointment records
        with open(APPOINTMENTS_FILE, 'r') as file:
            lines = file.readlines()

        # Step 3: Display header
        print("Appointment ID  |  Doctor ID  |  Date  |  Time  ")

        # Step 4: Filter and display matching appointments
        for line in lines:
            parts = line.strip().split(",")
            if parts[1] == patient_id:
                print(f"     {parts[0]}     |     {parts[2]}    |{parts[3]}|  {parts[4]}")
                found = True

        # Step 5: If no appointments found
        if not found:
            print("❌ No appointments found.")

    except FileNotFoundError:
        # Step 6: Handle missing file
        print("❌ Error 102: appointments.txt file not found.")
    except Exception as e:
        # Step 7: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

# ============================
# View medical records
# ============================
def view_medical_records(patient_id):
    """
    Displays medical records for the patient.
    """
    # Step 1: Initialize flag
    found = False

    try:
        # Step 2: Read medical records
        with open(MEDICAL_RECORDS_FILE, 'r') as file:
            lines = file.readlines()

        # Step 3: Filter and display matching records
        for line in lines:
            record = line.strip().split(",")
            if record[0] == patient_id:
                print("---------------------------------")
                print(f"Doctor ID: {record[1]}")
                print(f"Date: {record[2]}")
                print(f"Diagnosis: {record[3]}")
                print(f"Medicine(s): {record[4]}")
                print(f"Treatment Plan: {record[5]}")
                print("---------------------------------")
                found = True

        # Step 4: If no records found
        if not found:
            print("❌ No medical records found.")

    except FileNotFoundError:
        # Step 5: Handle missing file
        print("❌ Error 102: medrecords.txt file not found.")
    except Exception as e:
        # Step 6: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

# ============================
# View billing history
# ============================
def view_billing_history(patient_id):
    """
    Displays billing/payment history for the patient.
    """
    # Step 1: Initialize flag
    found = False

    try:
        # Step 2: Read payment records
        with open(PAYMENTS_FILE, 'r') as file:
            lines = file.readlines()

        # Step 3: Display header
        print("  Payment ID  |  Appointment ID  |  Amount  |  Date  ")

        # Step 4: Filter and display matching records
        for line in lines:
            record = line.strip().split(",")
            if record[1] == patient_id:
                print(f"   {record[0]}    |       {record[2]}     |  {record[3]}  |{record[4]}")
                found = True

        # Step 5: If no records found
        if not found:
            print("❌ No billing records found.")

    except FileNotFoundError:
        # Step 6: Handle missing file
        print("❌ Error 102: payments.txt file not found.")
    except Exception as e:
        # Step 7: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")


# ============================
# Patient login
# ============================
def patients_login():
    """
    Authenticates a patient using credentials from the log file.
    """
    # Step 1: Prompt for username and password
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    try:
        # Step 2: Open patient log file and check credentials
        with open(PATIENTS_LOG, 'r') as file:
            for line in file:
                stored_user, stored_pass = line.strip().split(',')
                if username == stored_user and password == stored_pass:
                    # Step 3: If match found, login successful
                    print("✅ Login successful.")
                    return stored_user

        # Step 4: If no match found
        print("❌ Invalid username or password.")
        return False

    except FileNotFoundError:
        # Step 5: Handle missing log file
        print("❌ Error 102: patientlog.txt file not found.")
        return False
    except Exception as e:
        # Step 6: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

# ============================
# Patient menu
# ============================
def patient_menu(patient_id):
    """
    Displays the patient menu and handles user choices.
    """
    while True:
        # Step 1: Show menu options
        print("\n--- Patient Menu ---")
        print("1. View Personal Info")
        print("2. Update Contact and Address")
        print("3. View Appointments")
        print("4. View Medical Records")
        print("5. View Billing History")
        print("6. Log out")

        # Step 2: Get user choice
        choice = input("Enter your choice: ").strip()

        # Step 3: Call corresponding function
        if choice == '1':
            view_personal_info(patient_id)
        elif choice == '2':
            update_contact_info(patient_id)
        elif choice == '3':
            view_appointments_patient(patient_id)
        elif choice == '4':
            view_medical_records(patient_id)
        elif choice == '5':
            view_billing_history(patient_id)
        elif choice == '6':
            print("👋 Goodbye. Logging out...")
            break
        else:
            # Step 4: Handle invalid input
            print("❌ Error 101: Invalid choice. Try again.")
