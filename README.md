Clinic Management System
A command-line clinic management system written in Python for the CT108-3-1-PYP module. Built by Group 31, the application gives receptionists, doctors, nurses, and patients separate menus for their day-to-day tasks.
Features
Role	What you can do
Receptionist	Register and update patient records, schedule or update appointments, and record payments.
Doctor	View appointments, patient medical history, and nursing observations. Update patient records and manage availability.
Nurse	View appointments and prescriptions, write or edit observations, and record medication given.
Patient	View personal details, appointments, medical records, and billing history. Update contact information.


Run locally
1. Clone or download this repository.
2. Open a terminal in the folder containing mainmenu.py. Keep the project's .txt data files in that same folder.
3. Run the application with Python 3.
   python mainmenu.py
   On Windows, you can also use py mainmenu.py. The application uses Python's standard library.
4. Choose 1 for Receptionist, 2 for Doctor, 3 for Nurse, or 4 for Patient, then follow the login prompts.
Project structure
File	Purpose
mainmenu.py	Displays the main menu and routes users to the appropriate login and role menu.
receptionist.py	Handles registration, appointments, and payments.
doctor.py	Handles doctor appointments, availability, and patient records.
nurse.py	Handles observations, prescriptions, and medication administration records.
patients.py	Gives patients access to their information, appointments, medical records, and billing history.
*.txt	Stores local data such as accounts, schedules, appointments, and records.


About this project
This is a coursework prototype that uses local text files for storage. Use fictional patient records and demo credentials when running or sharing it.