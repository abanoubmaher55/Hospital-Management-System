from department import Department


class Hospital:
    """
     The Hospital class represent a hospital containing multiple departments

    """

    def __init__(self, name: str, location: str):
        """
        Initialize a new hospital with its name and location

        Args:
            name (str): The name of the hospital
            location (str): The location where the hospital is located
        """
        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department: Department) -> None:
        """
        Add a department to the hospital's list of departments

        Args:
            department (Department): The department that will be
            added to the hospital
        """
        self.departments.append(department)

    def view_info(self) -> str:
        """
        Return general information about the hospital
        Returns:
            str: A formatted string containing the hospital information
        
        """
        return (
            f"\nHospital: {self.name}"
            f"\nLocation: {self.location}"
            f"\nDepartments: {len(self.departments)}"
        )