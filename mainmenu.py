# Import role-specific login and menu functions
from receptionist import receptionist_login, receptionist_menu
from doctor import doctor_login, doctor_menu
from nurse import nurse_login, nurse_menu
from patients import patients_login, patient_menu

def main_menu():
    """
    Displays the main menu for the Clinic Management System.
    Allows users to log in based on their role and access their respective menus.
    """
    while True:
        # Display role options
        print("\n*** Clinic Management System ***")
        print("1. Receptionist")
        print("2. Doctor")
        print("3. Nurse")
        print("4. Patient")

        # Get user role choice
        choice = input("Enter your role: ").strip()

        # Route to appropriate login and menu based on role
        if choice == '1':
            if receptionist_login():
                receptionist_menu()

        elif choice == '2':
            doctor_id = doctor_login()
            if doctor_id:
                doctor_menu(doctor_id)

        elif choice == '3':
            if nurse_login():
                nurse_menu()

        elif choice == '4':
            patient_id = patients_login()
            if patient_id:
                patient_menu(patient_id)

        else:
            print("❌ Error 101: Invalid choice. Please try again.")

# Run the main menu
main_menu()
