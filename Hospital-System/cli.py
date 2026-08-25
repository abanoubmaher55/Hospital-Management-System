from models.hospital import Hospital
from models.department import Department
from models.person import Patient, Staff

class HospitalCLI:
    """Class to manage User Interface and interactions via terminal."""
    def __init__(self):
        self.hospital = None

    def setup_hospital(self):
        print("=== Setup Hospital System ===")
        name = input("Enter Hospital Name: ")
        location = input("Enter Hospital Location: ")
        self.hospital = Hospital(name, location)
        print(f"Hospital '{name}' created successfully!\n")

    def run(self):
        if not self.hospital:
            self.setup_hospital()

        while True:
            print(f"\n--- {self.hospital.name} Management Menu ---")
            print("1. Add Department")
            print("2. Add Patient to Department")
            print("3. Add Staff to Department")
            print("4. View All Departments & Records")
            print("5. Exit")
            
            choice = input("Select an option (1-5): ")

            if choice == "1":
                dept_name = input("Enter Department Name: ")
                dept = Department(dept_name)
                self.hospital.add_department(dept)

            elif choice == "2":
                if not self.hospital.departments:
                    print("No departments available. Create one first!")
                    continue
                dept_name = input("Enter Department Name to add patient into: ")
                dept = next((d for d in self.hospital.departments if d.name == dept_name), None)
                if dept:
                    name = input("Enter Patient Name: ")
                    age = int(input("Enter Patient Age: "))
                    record = input("Enter Medical Record: ")
                    patient = Patient(name, age, record)
                    dept.add_patient(patient)
                else:
                    print("Department not found!")

            elif choice == "3":
                if not self.hospital.departments:
                    print("No departments available. Create one first!")
                    continue
                dept_name = input("Enter Department Name to add staff into: ")
                dept = next((d for d in self.hospital.departments if d.name == dept_name), None)
                if dept:
                    name = input("Enter Staff Name: ")
                    age = int(input("Enter Staff Age: "))
                    position = input("Enter Staff Position (e.g., Doctor, Nurse): ")
                    staff = Staff(name, age, position)
                    dept.add_staff(staff)
                else:
                    print("Department not found!")

            elif choice == "4":
                print(f"\n=== {self.hospital.name} Overview ===")
                for dept in self.hospital.departments:
                    print(f"\nDepartment: {dept.name}")
                    print(" Patients:")
                    for p in dept.patients:
                        print(f"  - {p.view_info()} | {p.view_record()}")
                    print(" Staff:")
                    for s in dept.staff:
                        print(f"  - {s.view_info()}")

            elif choice == "5":
                print("Exiting System. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")