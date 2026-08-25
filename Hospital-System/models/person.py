class Person:
    """Base class for all people in the hospital."""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def view_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"


class Patient(Person):
    """Class for hospital patients, inheriting from Person."""
    def __init__(self, name: str, age: int, medical_record: str):
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self) -> str:
        return f"Patient Record: {self.medical_record}"


class Staff(Person):
    """Class for hospital staff, inheriting from Person."""
    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age)
        self.position = position

    def view_info(self) -> str:
        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"