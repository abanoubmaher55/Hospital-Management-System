from person import Person

class Staff(Person):
    """Class for hospital staff, inheriting from Person."""
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def view_info(self):
        """View staff information."""
        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"