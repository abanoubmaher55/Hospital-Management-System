from hospital import Hospital
from department import Department
from patient import Patient
from staff import Staff


def show_departments(hospital: Hospital) -> None:
    """Display all departments in the hospital."""
    if not hospital.departments:
        print("No departments available.")
        return

    print("\nDepartments:")

    for index, department in enumerate(hospital.departments, start=1):
        print(f"{index}. {department.name}")


def add_department(hospital: Hospital) -> None:
    """Create and add a new department to the hospital."""
    name = input("Enter department name: ")

    department = Department(name)
    hospital.add_department(department)

    print(f"Department '{name}' added successfully.")


def add_patient(hospital: Hospital) -> None:
    """Create a patient and add them to a selected department."""
    if not hospital.departments:
        print("No departments available.")
        print("Please add a department first.")
        return

    show_departments(hospital)

    try:
        department_number = int(
            input("Enter the department number to add the patient to: ")
        )
    except ValueError:
        print("Invalid department number.")
        return

    if not 1 <= department_number <= len(hospital.departments):
        print("Invalid department.")
        return

    name = input("Enter patient name: ")

    try:
        age = int(input("Enter patient age: "))
    except ValueError:
        print("Age must be a number.")
        return

    medical_record = input("Enter medical record: ")

    patient = Patient(
        name,
        age,
        medical_record
    )

    department = hospital.departments[department_number - 1]
    department.add_patient(patient)

    print(
        f"Patient '{name}' added to "
        f"'{department.name}' successfully."
    )


def add_staff(hospital: Hospital) -> None:
    """Create a staff member and add them to a selected department."""
    if not hospital.departments:
        print("No departments available.")
        print("Please add a department first.")
        return

    show_departments(hospital)

    try:
        department_number = int(
            input("Enter the department number to add the staff to: ")
        )
    except ValueError:
        print("Invalid department number.")
        return

    if not 1 <= department_number <= len(hospital.departments):
        print("Invalid department.")
        return

    name = input("Enter staff name: ")

    try:
        age = int(input("Enter staff age: "))
    except ValueError:
        print("Age must be a number.")
        return

    position = input("Enter staff position: ")

    staff_member = Staff(
        name,
        age,
        position
    )

    department = hospital.departments[department_number - 1]
    department.add_staff(staff_member)

    print(
        f"Staff member '{name}' added to "
        f"'{department.name}' successfully."
    )


def add_menu(hospital: Hospital) -> None:
    """Display and handle the menu for adding hospital data."""
    while True:
        print("\n========== ADD MENU ==========")
        print("1. Add Department")
        print("2. Add Patient")
        print("3. Add Staff")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_department(hospital)

        elif choice == "2":
            add_patient(hospital)

        elif choice == "3":
            add_staff(hospital)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


def view_departments(hospital: Hospital) -> None:
    """Display all departments with their patients and staff."""
    if not hospital.departments:
        print("No departments available.")
        return

    print("\n========== DEPARTMENTS ==========")

    for department in hospital.departments:
        print(f"\nDepartment: {department.name}")

def view_patients(hospital: Hospital) -> None:
    """Display all departments only"""
    if not hospital.departments:
        print("No departments available.")
        return

    found_patient = False

    print("\n========== PATIENTS ==========")

    for department in hospital.departments:
        for patient in department.patients:
            found_patient = True

            print(
                f"Department: {department.name}\n "
                f"+ {patient.view_info()}"
            )

    if not found_patient:
        print("No patients available.")


def view_staff(hospital: Hospital) -> None:
    """Display all staff members in all hospital departments."""
    if not hospital.departments:
        print("No departments available.")
        return

    found_staff = False

    print("\n========== STAFF ==========")

    for department in hospital.departments:
        for staff_member in department.staff:
            found_staff = True

            print(
                f"Department: {department.name} "
                f"{staff_member.view_info()}"
            )

    if not found_staff:
        print("No staff available.")


def run_cli() -> None:
    """Run the main command-line interface."""
    hospital_name = input("Enter hospital name: ")
    hospital_location = input("Enter hospital location: ")

    hospital = Hospital(
        hospital_name,
        hospital_location
    )

    while True:
        print("\n========================================")
        print("       HOSPITAL MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Add")
        print("2. View Departments")
        print("3. View Patients")
        print("4. View Staff")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_menu(hospital)

        elif choice == "2":
            view_departments(hospital)

        elif choice == "3":
            view_patients(hospital)

        elif choice == "4":
            view_staff(hospital)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again")