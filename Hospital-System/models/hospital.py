from models.department import Department

class Hospital:
    """Class for managing hospital operations."""
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department: Department):
        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")