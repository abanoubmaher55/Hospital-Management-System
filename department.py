
"""
Department Module
-----------------
This module defines the Department class for the Hospital Management System.
It encapsulates department-level operations, managing patient admissions and
staff employment in alignment with the Hospital UML specification.
"""

from patient import Patient
from staff import Staff


class Department:
    """
    Represents an organizational department within a hospital.

    Attributes:
        name (str): The name of the department (e.g., 'Cardiology', 'Neurology').
        patients (list[Patient]): Collection of Patient instances managed by this department.
        staff (list[Staff]): Collection of Staff instances employed by this department.
    """

    def __init__(self, name: str):
        """
        Initializes a new Department instance.

        Args:
            name (str): The name of the department.
        """
        self.name: str = name
        self.patients: list[Patient] = []
        self.staff: list[Staff] = []

    def add_patient(self, patient: Patient) -> None:
        """
        Adds a patient to the department's patient management registry.

        Args:
            patient (Patient): The patient instance to associate with the department.

        Raises:
            TypeError: If the provided argument is not an instance of Patient.

        Returns:
            None
        """
        if not isinstance(patient, Patient):
            raise TypeError(f"Expected a Patient object, got {type(patient).__name__}.")

        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")

    def add_staff(self, staff_member: Staff) -> None:
        """
        Adds a staff member to the department's employee roster.

        Args:
            staff_member (Staff): The staff instance to employ in the department.

        Raises:
            TypeError: If the provided argument is not an instance of Staff.

        Returns:
            None
        """
        if not isinstance(staff_member, Staff):
            raise TypeError(f"Expected a Staff object, got {type(staff_member).__name__}.")

        self.staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")

    def view_department_summary(self) -> str:
        """
        Generates a summary of the department, including staff and patient counts.

        Returns:
            str: A formatted overview of the department's current state.
        """
        return (
            f"Department: {self.name} | "
            f"Total Staff: {len(self.staff)} | "
            f"Total Patients: {len(self.patients)}"
        )