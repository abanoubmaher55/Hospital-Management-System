from person import Person


class Patient(Person):
    """Represent a patient in the hospital system

    A patient is a person who receives medical care in the hospital
    This class extends the Person class by storing the patient's
    medical record
    """

    def __init__(self, name: str, age: int, medical_record: str):
        """Initialize a patient with personal and medical information

        Args:
            name (str): The patient's full name
            age (int): The patient's age
            medical_record (str): The patient's medical record
        """
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_info(self) -> str:
        """Return the patient's personal and medical information

        Returns:
            str: A formatted string containing the patient's name,
                age, and medical record
        """
        return (
            f" Name: {self.name}, Age: {self.age}, Medical Record: {self.medical_record}"
        )