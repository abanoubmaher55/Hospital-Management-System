from abc import ABC, abstractmethod


class Person(ABC):
    """
    Abstract base class representing a person in the hospital.

    This class provides the common attributes shared by all people
    in the hospital, such as name and age. It also defines the
    abstract view_info() method that must be implemented by
    subclasses.

    Attributes:
        name (str): The person's name.
        age (int): The person's age.
    """

    def __init__(self, name, age):
        """
        Initialize a Person object.

        Args:
            name (str): The person's name.
            age (int): The person's age.
        """
        self.name = name
        self.age = age

    @abstractmethod
    def view_info(self):
        """
        Return basic information about the person.

        This method must be implemented by all subclasses.

        Returns:
            str: A string containing information about the person.
        """
        pass


class Patient(Person):
    """
    Represent a patient in the hospital.

    Inherits common person information from the Person class and
    adds a medical record specific to the patient.

    Attributes:
        name (str): The patient's name.
        age (int): The patient's age.
        medical_record (str): The patient's medical record.
    """

    def __init__(self, name, age, medical_record):
        """
        Initialize a Patient object.

        Args:
            name (str): The patient's name.
            age (int): The patient's age.
            medical_record (str): The patient's medical record.
        """
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_info(self):
        """
        Return basic information about the patient.

        Returns:
            str: The patient's name and age.
        """
        return f"Name: {self.name}, Age: {self.age}"

    def view_record(self):
        """
        Return the patient's medical record.

        Returns:
            str: The patient's medical record.
        """
        return f"Patient Record: {self.medical_record}"


class Staff(Person):
    """
    Represent a staff member working in the hospital.

    Inherits common person information from the Person class and
    adds the staff member's position.

    Attributes:
        name (str): The staff member's name.
        age (int): The staff member's age.
        position (str): The staff member's position in the hospital.
    """

    def __init__(self, name, age, position):
        """
        Initialize a Staff object.

        Args:
            name (str): The staff member's name.
            age (int): The staff member's age.
            position (str): The staff member's position.
        """
        super().__init__(name, age)
        self.position = position

    def view_info(self):
        """
        Return information about the staff member.

        Returns:
            str: The staff member's name, age, and position.
        """
        return (
            f"Staff Name: {self.name}, "
            f"Age: {self.age}, "
            f"Position: {self.position}"
        )


class Visitor(Person):
    """
    Represent a visitor visiting a patient in the hospital.

    Inherits common person information from the Person class and
    stores the name of the patient being visited.

    Attributes:
        name (str): The visitor's name.
        age (int): The visitor's age.
        name_of_patient (str): The name of the patient being visited.
    """

    def __init__(self, name, age, name_of_patient):
        """
        Initialize a Visitor object.

        Args:
            name (str): The visitor's name.
            age (int): The visitor's age.
            name_of_patient (str): The name of the patient being visited.
        """
        super().__init__(name, age)
        self.name_of_patient = name_of_patient

    def view_info(self):
        """
        Return information about the visitor.

        Returns:
            str: The visitor's name, age, and the patient being visited.
        """
        return (
            f"Visitor Name: {self.name}, "
            f"Age: {self.age}, "
            f"Visiting: {self.name_of_patient}"
        )


class Hospital:
    """
    Represent a hospital and manage its operations.

    The Hospital class stores information about the hospital and
    maintains collections of departments, patients, and staff.

    Attributes:
        name (str): The hospital's name.
        location (str): The hospital's location.
        departments (list): A list of hospital departments.
        patients (list): A list of registered patients.
        staff (list): A list of hospital staff members.
    """

    def __init__(self, name, location):
        """
        Initialize a Hospital object.

        Args:
            name (str): The hospital's name.
            location (str): The hospital's location.
        """
        self.name = name
        self.location = location
        self.departments = []
        self.patients = []
        self.staff = []

    def add_patient(self, patient):
        """
        Add a patient to the hospital's patient list.

        Args:
            patient (Patient): The patient object to be added.

        Returns:
            None
        """
        self.patients.append(patient)

