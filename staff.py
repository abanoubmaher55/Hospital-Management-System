# name : Ahmed Reda Mohamed
from person import Person

class Staff(Person):
    """Represent a hospital staff member."""

    def __init__(self, name, age, position):
        """Create a staff member with a name, age, and position."""
        super().__init__(name, age)
        self.position = position

    def view_info(self):
        """Return the staff member's information as a string."""
        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"