# name : Ahmed Reda Mohamed
from person import Person

class Staff(Person):
    """Represent a hospital staff member with a name, age, and position

    This class extends :class:`Person` with the staff member's job position
    and provides a formatted view of the staff member's information
    """

    def __init__(self , name: str, age: int, position: str):
        """Create a staff member with a name is a string , age is an integar, and position is a sting."""
        super().__init__(name, age)
        self.position = position

    def view_info(self) ->str:
        """Return the staff member's information as a string."""
        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"