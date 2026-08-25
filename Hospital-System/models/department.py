from models.person import Patient, Staff

class Department:
    """Class representing a department in the hospital."""
    def __init__(self, name: str):
        self.name = name
        self.patients = []
        self.staff = []

    def add_patient(self, patient: Patient):
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")

    def add_staff(self, staff_member: Staff):
        self.staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")