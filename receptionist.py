
# File Path Constants

# Stores all registered patient information such as ID, name, age, gender, contact, email, and address.
PATIENTS_FILE = 'patients.txt'

# Stores appointment records including patient ID, doctor ID, appointment date/time, and status.
APPOINTMENTS_FILE = 'appointments.txt'

# Stores payment transactions including patient ID, amount paid, payment method, and date.
PAYMENTS_FILE = 'payments.txt'

# Logs receptionist login ID and Pass.
RECEPTIONIST_FILE = 'receptionistlog.txt'

# Contains doctor availability schedules including doctor ID, available dates/times, and specialties.
DOCTOR_SCHEDULE_FILE = 'doctor_schedule.txt'


def generate_patient_id():
    """
    Generates a unique patient ID in the format P00001, P00002, etc.
    Reads the last line of the patients file to determine the next ID.
    """
    try:
        # Step 1: Open the patients file and read all lines
        with open(PATIENTS_FILE, 'r') as file:
            lines = file.readlines()

            # Step 2: If the file is empty, start with the first ID
            if not lines:
                return "P00001"

            # Step 3: Extract the last patient ID from the last line
            last_line = lines[-1].strip()
            last_id = last_line.split(',')[0]  # Expected format: "Patient ID:P00001"

            # Step 4: Check and increment the numeric part of the ID
            if last_id.startswith("Patient ID:P"):
                num = int(last_id.split(':')[1][1:]) + 1  # Extract "P00001", then slice to get number
                return f"P{num:05d}"

    except FileNotFoundError:
        # Step 5: Handle missing file
        print("!Error 102: patients.txt file not found. Starting new file.")
    except Exception as e:
        # Step 6: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

    # Default ID if file is missing or unreadable
    return "P00001"


def register_patient():
    # Step 1: Generate a unique patient ID using a helper function
    # This ensures each patient has a distinct identifier
    patient_id = generate_patient_id()
    print(f"Assigned Patient ID: {patient_id}")
    
   

    # Step 2: Validate and collect patient's name
    # Thid ensures patient name is not empty and contains only letters and spaces
    while True:
        name = input("Enter patient name: ").strip()
        if name.replace(" ", "").isalpha():
            break
        else:
            print("❌ Error 101: Invalid name. Please enter alphabetic characters only.")

    
    # Step 3: Validate and collect patient's age
    # Age must be a valid integer; loop until correct input is provided
    while True:
        try:
            age = int(input("Enter patient age: "))
            break  # Exit loop if input is valid
        except ValueError:
            print("❌ Error 101: Invalid input. Please enter a valid integer for age.")
    
    # Step 4: Validate and collect patient's gender
    # Accept only predefined values to maintain consistency
    valid_genders = ["Male", "Female", "Other"]
    while True:
        gender = input("Enter patient gender (Male/Female/Other): ").capitalize()
        if gender in valid_genders:
            break  # Exit loop if input is valid
        else:
            print("❌ Error 101: Invalid input. Please enter 'Male', 'Female', or 'Other'.")
    
    # Step 5: Validate and collect contact number
    # Contact must be an integer; you could also add length or format checks
    while True:
        try:
            contact = int(input("Enter contact number: "))
            break  # Exit loop if input is valid
        except ValueError:
            print("❌ Error 101: Invalid input. Please enter a valid integer for contact number.")
    
    # Step 6: Collect patient's email address
    # Basic email format validation
    while True:
        email = input("Enter patient E-Mail: ").strip()
    
        # Basic checks: must contain '@' and '.', and '@' must come before the last '.'
        if "@" in email and "." in email and email.index("@") < email.rindex("."):
            break
        else:
            print("❌ Error 101: Invalid email format. Please enter a valid email address (e.g., user@example.com).")

    
    # Step 7: Collect patient's physical address
    # Address must not be empty
    while True:
        address = input("Enter address: ").strip()
        if address:
            break
        print("❌ Error 101: Invalid input. Address cannot be empty.")


    # Step 8: Save patient data to file
    # Use try-except to handle potential file I/O errors
    try:
        with open(PATIENTS_FILE, 'a') as file:
            # Write patient data in a structured format (CSV-like)
            file.write(
                f"Patient ID:{patient_id},"
                f"Name:{name},"
                f"Age:{age},"
                f"Gender:{gender},"
                f"Contact:{contact},"
                f"E-Mail:{email},"
                f"Address:{address}\n"
            )
        print("✅ Patient registered successfully.")
    
    except FileNotFoundError:
        print("❌ Error 102: patients.txt file not found.")
    except Exception as e:
        # Step 9: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")


def update_patient():
    # Prompt user for the patient ID to update
    patient_id = input("Enter patient ID to update: ").strip()
    updated = False  # Flag to track if update was successful

    try:
        # Read all existing patient records
        with open(PATIENTS_FILE, 'r') as file:
            lines = file.readlines()

        # Open the file again in write mode to overwrite with updated data
        with open(PATIENTS_FILE, 'w') as file:
            for line in lines:
                # Check if the current line matches the patient ID
                if line.startswith(f"Patient ID:{patient_id},"):
                    print("🔄 Updating patient details...")

                    # Validate name
                    while True:
                        name = input("Enter new name: ").strip()
                        if name.replace(" ", "").isalpha():
                            break
                        print("❌ Error 101:Invalid name. Use letters only.")

                    # Validate age
                    while True:
                        try:
                            age = int(input("Enter new age: "))
                            break
                        except ValueError:
                            print("❌ Error 101: Invalid input. Age must be a number.")

                    # Validate gender
                    while True:
                        gender = input("Enter new gender (Male/Female/Other): ").capitalize()
                        if gender in ["Male", "Female", "Other"]:
                            break
                        print("❌ Error 101: Invalid input.Please enter Male, Female, or Other.")

                    # Validate contact
                    while True:
                        try:
                            contact = int(input("Enter new contact number: "))
                            break
                        except ValueError:
                            print("❌ Error 101: Invalid input. Contact number must be digits only.")

                    # Validate email (basic check)
                    while True:
                        email = input("Enter new E-Mail: ").strip()
                        if "@" in email and "." in email:
                            break
                        print("❌ Error 101: Invalid email format. Please enter a valid email address (e.g., user@example.com).")

                    # Validate address
                    while True:
                        address = input("Enter new address: ").strip()
                        if address:
                            break
                        print("❌ Error 101: Invalid input. Address cannot be empty.")

                    # Write updated patient info
                    file.write(
                        f"Patient ID:{patient_id},"
                        f"Name:{name},Age:{age},Gender:{gender},"
                        f"Contact:{contact},E-Mail:{email},Address:{address}\n"
                    )
                    updated = True
                else:
                    # Write unchanged lines back to the file
                    file.write(line)

        # Final status message
        if updated:
            print("✅ Patient updated successfully.")
        else:
            print("❌ Error 103: Patient ID not found.")

    except FileNotFoundError:
        print("❌ Error 102: patients.txt file not found.")
    except Exception as e:
        print(f"❌ Error 999: Unexpected error occurred - {e}")


def generate_appointment_id():
    """
    Generates a unique appointment ID in the format A00001, A00002, etc.
    It reads the last line of the appointments file to determine the next number.
    """
    try:
        # Try to open the appointments file and read all lines
        with open(APPOINTMENTS_FILE, 'r') as file:
            lines = file.readlines()

            # If the file is empty, start with the first ID
            if not lines:
                return "A00001"

            # Get the last line and extract the appointment ID
            last_line = lines[-1].strip()
            last_id = last_line.split(',')[0]  # Assumes ID is the first field

            # Check if the ID starts with 'A' and increment the number
            if last_id.startswith("A"):
                num = int(last_id[1:]) + 1
                return f"A{num:05d}"

    except FileNotFoundError:
        # If the file doesn't exist, assume it's the first appointment
        print("!Error 102: appointments.txt file not found. Starting new file.")
    except Exception as e:
        # Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

    # Default return if file is missing or unreadable
    return "A00001"

def schedule_appointment():
    # Step 1: Get doctor ID and desired appointment date
    doctor_id = input("Enter doctor ID: ").strip()
    date = input("Enter date (DDMMYYYY): ").strip()

    # Step 2: Check if the doctor is available on the given date
    try:
        with open(DOCTOR_SCHEDULE_FILE, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 3 and parts[0] == doctor_id and parts[1] == date and parts[2].lower() == "blocked":
                    print("❌ Doctor is not available on this date.")
                    return
    except FileNotFoundError:
        # Step 3: Handle missing file
        print("❌ Error 102: doctor_schedule.txt file not found.")
        return
    except Exception as e:
        # Step 4: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

    # Step 5: Generate a unique appointment ID
    appointment_id = generate_appointment_id()
    print(f"Assigned Appointment ID: {appointment_id}")

    # Step 6: Get patient ID
    patient_id = input("Enter patient ID: ").strip()

    # Step 7: Get a valid time slot (check for conflicts)
    while True:
        time = input("Enter time (HH:MM): ").strip()
        conflict = False

        try:
            with open(APPOINTMENTS_FILE, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) >= 5 and parts[2] == doctor_id and parts[3] == date and parts[4] == time:
                        print("❌ Sorry, this time slot is already taken. Please choose a different time.")
                        conflict = True
                        break
        except FileNotFoundError:
            # Step 8: Handle missing file
            print("❌ Error 102: appointments.txt file not found. Proceeding with new entry.")
        except Exception as e:
            # Step 9: Handle unexpected errors
            print(f"❌ Error 999: Unexpected error occurred - {e}")

        if not conflict:
            break  # Valid time found

    # Step 10: Save the appointment to the file
    try:
        with open(APPOINTMENTS_FILE, 'a') as file:
            file.write(f"{appointment_id},{patient_id},{doctor_id},{date},{time}\n")
        print("✅ Appointment scheduled successfully.")
    except FileNotFoundError:
        print("❌ Error 102: appointments.txt file not found.")
    except Exception as e:
        # Step 11: handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")


def update_schedule(parts):
    """
    Updates the date and time in a given appointment record (parts list),
    and checks if the new slot is blocked or already taken.
    Assumes parts[2] is doctor_id, parts[3] is date, parts[4] is time.
    """

    doctor_id = parts[2]

    # Get new date input
    while True:
        new_date = input("Enter new date (DDMMYYYY): ").strip()
        if len(new_date) == 8 and new_date.isdigit():
            break
        print("❌ Error 101: Invalid date format. Please enter in DDMMYYYY format.")

    # Check if the doctor has blocked this date
    try:
        with open(DOCTOR_SCHEDULE_FILE, 'r') as file:
            for line in file:
                schedule_parts = line.strip().split(',')
                if len(schedule_parts) >= 3:
                    file_doctor_id = schedule_parts[0]
                    file_date = schedule_parts[1]
                    file_status = schedule_parts[2].strip().lower()
                    if file_doctor_id == doctor_id and file_date == new_date and file_status == "blocked":
                        print("❌ Doctor is not available on this date.")
                        return parts, False  # Cancel update
    
    except FileNotFoundError:
        # Handle missing file
        print("❌ Error 102: doctor_scchedule.txt file not found.")
        return parts, False  # Cancel update
    except Exception as e:
        # Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")
        return parts, False # Cancel update

    # Get new time input
    while True:
        new_time = input("Enter new time (HH:MM): ").strip()
        if len(new_time) == 5 and new_time[2] == ":" and new_time.replace(":", "").isdigit():
            break
        print("❌ Error 101: Invalid time format. Please enter in HH:MM format.")

    # Check for appointment conflicts
    conflict = False
    try:
        # This now reads the original, unmodified file
        with open(APPOINTMENTS_FILE, 'r') as file:
            for line in file:
                existing = line.strip().split(',')
                if len(existing) >= 5 and existing[0] != parts[0] and existing[2] == doctor_id and existing[3] == new_date and existing[4] == new_time:
                    conflict = True
                    break
    
    except FileNotFoundError:
        # Handle missing file
        print(f"!Error 102: {APPOINTMENTS_FILE} file not found. Assuming no conflict.")
        return parts, False #cancel update
    except Exception as e:
        # Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")
        return parts, False #cancel update
        
    if conflict:
        print("❌ This time slot is already taken for this doctor.")
        print("⚠️ Update cancelled due to scheduling conflict.")
        return parts, False  # Return original parts unchanged

    # Update the appointment record in memory
    parts[3] = new_date
    parts[4] = new_time
    # We no longer print "Schedule updated" here, we do it in the parent function.
    return parts, True


def update_appointment():
    """
    Allows user to update an appointment by searching via Appointment ID or Patient ID.
    Displays current schedule and updates date/time if available.
    """
    print("**** Search Options ****")
    print("1. Appointment ID")
    print("2. Patient ID")
    choice = input("Enter option number: ").strip()

    search_value = ""
    if choice == '1':
        search_value = input("Enter Appointment ID: ").strip()
    elif choice == '2':
        search_value = input("Enter Patient ID: ").strip()
    else:
        print("!Error 101: Invalid Choice. Please try again.")
        return

    try:
        # Step 1: Read all lines into memory FIRST.
        with open(APPOINTMENTS_FILE, 'r') as file:
            lines = file.readlines()

        updated_lines = []
        appointment_found = False
        update_successful = False

        # Step 2: Process the lines in memory and build a new list.
        for line in lines:
            parts = line.strip().split(',')
            # Check if this is the line we need to update
            if (choice == '1' and parts[0] == search_value) or \
               (choice == '2' and parts[1] == search_value and not appointment_found):
                
                appointment_found = True
                print(f"Current Schedule: Date: {parts[3]}, Time: {parts[4]}")

                # The file is NOT open for writing, so this call is now safe
                new_parts, success = update_schedule(parts)

                if success:
                    updated_lines.append(",".join(new_parts) + "\n")
                    update_successful = True
                else:
                    updated_lines.append(line) # Update failed, add original line back
            else:
                updated_lines.append(line) # This is not the line to update, add it as is

        if not appointment_found:
            print("❌ Appointment not found.")
            return

        # Step 3: AFTER all checks are done, write the modified list back to the file.
        if update_successful:
            with open(APPOINTMENTS_FILE, 'w') as file:
                file.writelines(updated_lines)
            print("✅ Appointment schedule updated successfully.")
        else:
            print("❌ Appointment schedule not updated.")

    except FileNotFoundError:
        # Handle missing file
        print("❌ Error 102: appointments.txt file not found.")
    except Exception as e:
        # Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

def generate_payment_id():
    """
    Generates a unique payment ID in the format PY00001, PY00002, etc.
    Reads the last line of the payments file to determine the next ID.
    """
    try:
        # Open the payments file and read all lines
        with open(PAYMENTS_FILE, 'r') as file:
            lines = file.readlines()

            # If the file is empty, start with the first ID
            if not lines:
                return "PY00001"

            # Extract the last payment ID
            last_line = lines[-1].strip()
            last_id = last_line.split(',')[0]  # Assumes ID is the first field

            # If the ID starts with 'PY', increment the numeric part
            if last_id.startswith("PY"):
                num = int(last_id[2:]) + 1
                return f"PY{num:05d}"

    except FileNotFoundError:
        # If the file doesn't exist, start with the first ID
        print("!Error 102: payments.txt file not found. Starting new file.")
    
    except Exception as e:
        # Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")
    
    # Default ID if file is missing or unreadable
    return "PY00001"

def process_payment():
    """
    Processes a payment by generating a unique payment ID,
    validating patient ID, and recording payment details.
    """

    # Step 1: Generate and display a unique payment ID
    payment_id = generate_payment_id()
    print(f"Assigned Payment ID: {payment_id}")

    # Step 2: Get and validate patient ID
    patient_id = input("Enter patient ID: ").strip()
    try:
        with open(PATIENTS_FILE, 'r') as file:
            existing_ids = [
                line.split(',')[0].replace("Patient ID:", "").strip()
                for line in file.readlines()
            ]
            if patient_id not in existing_ids:
                print("❌ Error 103: Patient ID not found. Please try again.")
                return
    except FileNotFoundError:
        # Step 3: Handle missing file
        print("❌ Error 102: patients.txt file not found.")
        return
    except Exception as e:
        # Step 4: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")
        return

    # Step 5: Get appointment ID
    appointment_id = input("Enter Appointment ID: ").strip()

    # Step 6: Get and validate payment amount
    while True:
        try:
            amount = float(input("Enter amount: ").strip())
            if amount > 0:
                break
            else:
                print("❌ Amount must be greater than zero.")
        except ValueError:
            print("❌ Error 101: Invalid input. Please enter a number.")

    # Step 7: Get and validate payment date
    while True:
        date = input("Enter date (DDMMYYYY): ").strip()
        if len(date) == 8 and date.isdigit():
            break
        print("❌ Error 101: Invalid date format. Please use DDMMYYYY.")

    # Step 8: Save payment record to file
    try:
        with open(PAYMENTS_FILE, 'a') as file:
            file.write(f"{payment_id},{patient_id},{appointment_id},{amount},{date}\n")
        print("✅ Payment processed and receipt generated.")
    except Exception as e:
        # Step 9: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")


def delete_patient():
    """
    Deletes a patient record from the patients file based on the given patient ID.
    """

    # Step 1: Get the patient ID to delete
    patient_id = input("Enter patient ID to delete: ").strip()
    deleted = False  # Flag to track if deletion was successful

    try:
        # Step 2: Read all patient records
        with open(PATIENTS_FILE, 'r') as file:
            lines = file.readlines()

        # Step 3: Rewrite the file excluding the matching patient ID
        with open(PATIENTS_FILE, 'w') as file:
            for line in lines:
                if not line.startswith(f"Patient ID:{patient_id},"):
                    file.write(line)
                else:
                    deleted = True

        # Step 4: Show result
        if deleted:
            print("✅ Patient record deleted.")
        else:
            print("❌ Error 103: Patient ID not found.")

    except FileNotFoundError:
        # Step 5: Handle missing file
        print("❌ Error 102: patients.txt file not found.")
    except Exception as e:
        # Step 6: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

def receptionist_login():
    """
    Authenticates a receptionist by checking username and password
    against stored credentials in the receptionist log file.
    """

    # Step 1: Get login credentials
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    try:
        # Step 2: Open the receptionist log file and check credentials
        with open(RECEPTIONIST_FILE, 'r') as file:
            for line in file:
                stored_user, stored_pass = line.strip().split(',')
                if username == stored_user and password == stored_pass:
                    print("✅ Login successful.")
                    return True

        # Step 3: If no match found
        print("❌ Invalid username or password.")
        return False

    except FileNotFoundError:
        # Step 4: Handle missing file
        print("❌ Error 102: receptionistlog.txt file not found.")
        return False
    
    except Exception as e:
        # Step 5: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")
        return False

def receptionist_menu():
    """
    Displays the receptionist menu and handles user choices
    for patient registration, appointment scheduling, payments, etc.
    """

    while True:
        # Display menu options
        print("\n--- Receptionist Menu ---")
        print("1. Register New Patient")
        print("2. Update Patient Details")
        print("3. Schedule Appointment")
        print("4. Update Appointment Schedule")
        print("5. Process Payment")
        print("6. Delete Patient Details")
        print("7. Exit")

        # Get user choice
        choice = input("Enter your choice: ").strip()

        # Handle each menu option
        if choice == '1':
            register_patient()
        elif choice == '2':
            update_patient()
        elif choice == '3':
            schedule_appointment()
        elif choice == '4':
            update_appointment()
        elif choice == '5':
            process_payment()
        elif choice == '6':
            delete_patient()
        elif choice == '7':
            print("🔒 Logging out...")
            break
        else:
            print("❌ Error 101: Invalid choice. Please try again.")