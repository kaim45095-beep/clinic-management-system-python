# ============================
# File paths used in the nurse system
# ============================
NURSE_LOG = 'nurselog.txt'
PATIENTS_FILE = "patients.txt"
MEDICAL_RECORDS_FILE = "medrecords.txt"
MEDADMIN_FILE = "medadmin.txt"

# ============================
# Nurse login
# ============================
def nurse_login():
    """
    Authenticates a nurse using credentials from the log file.
    """
    # Step 1: Prompt for username and password
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    try:
        # Step 2: Open nurse log file and check credentials
        with open(NURSE_LOG, 'r') as file:
            for line in file:
                stored_user, stored_pass = line.strip().split(',')
                if username == stored_user and password == stored_pass:
                    # Step 3: If match found, login successful
                    print("✅ Login successful.")
                    return True

        # Step 4: If no match found
        print("❌ Invalid username or password.")
        return False

    except FileNotFoundError:
        # Step 5: Handle missing log file
        print("❌ Error 102: nurselog.txt file not found.")
        return False

# ============================
# Nurse menu
# ============================
def nurse_menu():
    """
    Displays the nurse menu and handles user choices.
    """
    while True:
        # Step 1: Show menu options
        print("\n======== NURSE MENU ========")
        print("1. See doctor appointments (by doctor ID)")
        print("2. Write patient observations")
        print("3. See doctor prescriptions")
        print("4. Write medicine given to patient")
        print("5. See medicine given to patient")
        print("6. Update observation")
        print("7. Delete observation")
        print("8. Exit nurse system")
        print("============================")

        # Step 2: Get user choice
        choice = input("Enter option (1-8): ").strip()

        # Step 3: Call corresponding function
        if choice == "1":
            show_appointments()
        elif choice == "2":
            write_observations()
        elif choice == "3":
            show_prescriptions()
        elif choice == "4":
            write_medicine_given()
        elif choice == "5":
            show_medicine()
        elif choice == "6":
            update_observation()
        elif choice == "7":
            delete_observation()
        elif choice == "8":
            print("👋 Goodbye Nurse!")
            break
        else:
            print("❌ Error 101: Invalid option. Try again.")

# ============================
# Option 1: Show doctor's appointments
# ============================
def show_appointments():
    """
    Displays appointments filtered by doctor ID.
    """
    # Step 1: Get doctor ID
    print("\n--- View Appointments by Doctor ---")
    doctor_id = input("Enter Doctor ID to filter: ").strip()
    found = False
    try:
        # Step 2: Open appointments file and filter by doctor ID
        with open("appointments.txt", "r") as file:
            print("  Appointment ID  |  Patient ID  |  Doctor ID  |  Date  |  Time  ")
            for line in file:
                parts = line.strip().split(",")
                if parts[2] == doctor_id:
                    print(f"      {parts[0]}      |    {parts[1]}    |     {parts[2]}    |{parts[3]}|  {parts[4]}     ")
                    found = True

        # Step 3: If no appointments found
        if not found:
            print("No appointments found for Doctor ID:", doctor_id)

    except FileNotFoundError:
        # Step 4: Handle missing file
        print("❌ Error 102: appointments.txt not found.")

# ============================
# Option 2: Write patient observations
# ============================
def write_observations():
    """
    Records new patient observations.
    """
    # Step 1: Get patient ID
    print("\n--- Record Observations ---")
    patient_id = input("Enter patient ID: ").strip()

    try:
        # Step 2: Check if patient exists
        with open(PATIENTS_FILE, 'r') as file:
            existing_ids = [line.split(',')[0].replace("Patient ID:", "").strip() for line in file.readlines()]
            if patient_id not in existing_ids:
                print("❌ Error 103: Patient ID not found. Please try again.")
                return
    except FileNotFoundError:
        # Step 3: Handle missing patient file
        print("❌ Error 102: patients.txt file not found.")
        return

    # Step 4: Get observation details
    date = input("Enter date (DDMMYYYY): ").strip()
    bp = input("Enter blood pressure (e.g., 120/80): ").strip()
    pulse = input("Enter pulse: ").strip()
    temp = input("Enter temperature (°C): ").strip()

    # Step 5: Validate numeric inputs
    try:
        float(pulse)
        float(temp)
    except ValueError:
        print("❌ Error  101: Invalid input. Pulse and temperature must be numeric.")
        return

    try:
        # Step 6: Save observation to file
        with open("observations.txt", "a") as file:
            file.write(f"{patient_id},{date},{bp},{pulse},{temp}\n")
        print("✅ Observation saved.")
    except Exception as e:
        # Step 7: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

# ============================
# Option 3: Show prescriptions
# ============================
def show_prescriptions():
    """
    Displays prescriptions given to a patient.
    """
    # Step 1: Get patient ID
    patient_id = input("Enter patient ID: ").strip()
    print("\n--- Doctor Prescriptions ---")
    found = False

    try:
        # Step 2: Read medical records and filter by patient ID
        with open(MEDICAL_RECORDS_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if parts[0] == patient_id:
                    print(f"Doctor ID: {parts[1]}")
                    print(f"Date: {parts[2]}")
                    print(f"Diagnosis: {parts[3]}")
                    print(f"Medicine(s): {parts[4]}")
                    print(f"Treatment Plan: {parts[5]}")
                    found = True

        # Step 3: If no prescriptions found
        if not found:
            print("No prescriptions found for this patient.")
    except FileNotFoundError:
        print("❌ Error 102: medrecords.txt file not found.")

    except Exception as e:
        # Step 4: Handle read errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

# ============================
# Option 4: Write medicine given
# ============================
def write_medicine_given():
    """
    Records medicine administered to a patient.
    """
    # Step 1: Get input details
    print("\n--- Administer Medicine ---")
    patient_id = input("Enter patient ID: ").strip()
    medicine = input("Enter medicine name: ").strip()
    date = input("Enter date (DDMMYYYY): ").strip()

    try:
        # Step 2: Save medicine record
        with open(MEDADMIN_FILE, "a") as file:
            file.write(f"{patient_id},{medicine},{date}\n")
        print("✅ Medicine given recorded.")
    except FileNotFoundError:
        # Step 3: Handle missing file
        print("❌ Error 102: medadmin.txt file not found.")
    except Exception as e:
        # Step 4: Handle write errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

# ============================
# Option 5: Show medicine given
# ============================
def show_medicine():
    """
    Displays medicine given to a patient on a specific date.
    """
    # Step 1: Get patient ID and date
    patient_id = input("Enter patient ID: ").strip()
    date = input("Enter date (DDMMYYYY): ").strip()
    print("\n--- Medicine(s) Given ---")
    found = False

    try:
        # Step 2: Read medicine records and filter
        with open(MEDADMIN_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if parts[0] == patient_id and parts[2] == date:
                    print(f"Medicine(s) given: {parts[1]}")
                    found = True

        # Step 3: If no records found
        if not found:
            print("No medicines given to this patient.")
    except FileNotFoundError:
        # Step 4: Handle missing file
        print("❌ Error 102: medadmin.txt file not found.")

    except Exception as e:
        # Step 4: Handle read errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

# ============================
# Option 6: Update observation
# ============================
def update_observation():
    """
    Updates an existing observation record for a patient on a specific date.
    """
    # Step 1: Prompt for patient ID and date
    print("\n--- Update Observation ---")
    patient_id = input("Enter patient ID to update: ").strip()
    date = input("Enter date (DDMMYYYY): ").strip()

    try:
        # Step 2: Read all existing observation records
        with open("observations.txt", "r") as file:
            lines = file.readlines()

        updated = False  # Flag to track if update was successful

        # Step 3: Open the file in write mode to overwrite with updated data
        with open("observations.txt", "w") as file:
            for line in lines:
                parts = line.strip().split(",")
                # Step 4: Check if this line matches the patient ID and date
                if parts[0] == patient_id and parts[1] == date:
                    # Step 5: Show current values and prompt for new ones
                    print(f"Current: BP={parts[2]}, Pulse={parts[3]}, Temp={parts[4]}")
                    new_bp = input("Enter new BP: ").strip()
                    new_pulse = input("Enter new Pulse: ").strip()
                    new_temp = input("Enter new Temperature: ").strip()

                    # Step 6: Validate numeric inputs
                    try:
                        float(new_pulse)
                        float(new_temp)
                    except ValueError:
                        print("❌ Error 101: Invalid input. Pulse and temperature must be numeric.")
                        file.write(line)  # Write original line back
                        continue

                    # Step 7: Write updated observation
                    file.write(f"{patient_id},{date},{new_bp},{new_pulse},{new_temp}\n")
                    updated = True
                else:
                    # Step 8: Write unchanged lines
                    file.write(line)

        # Step 9: Show result message
        if updated:
            print("✅ Observation updated successfully.")
        else:
            print("❌ Observation not found.")

    except FileNotFoundError:
        # Step 10: Handle missing file
        print("❌ Error 102: observations.txt file not found.")

    except Exception as e:
        # Step 11: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

# Option 7: Delete observation
def delete_observation():
    """
    Deletes an observation record for a patient on a specific date.
    """
    # Step 1: Prompt for patient ID and date
    print("\n--- Delete Observation ---")
    patient_id = input("Enter patient ID to delete: ").strip()
    date = input("Enter date (DDMMYYYY): ").strip()

    try:
        # Step 2: Read all existing observation records
        with open("observations.txt", "r") as file:
            lines = file.readlines()

        deleted = False  # Flag to track if deletion occurred

        # Step 3: Open the file in write mode to overwrite with filtered data
        with open("observations.txt", "w") as file:
            for line in lines:
                parts = line.strip().split(",")
                # Step 4: If record matches patient ID and date, skip writing it
                if parts[0] == patient_id and parts[1] == date:
                    deleted = True
                    continue  # Skip this line (delete it)
                # Step 5: Write all other lines back to the file
                file.write(line)

        # Step 6: Show result message
        if deleted:
            print("✅ Observation deleted successfully.")
        else:
            print("❌ Observation not found.")

    except FileNotFoundError:
        # Step 7: Handle missing file
        print("❌ Error 102: observations.txt file not found.")

    except Exception as e:
        # Step 8: Handle unexpected errors
        print(f"❌ Error 999: Unexpected error occurred - {e}")

