"""
Person Module
-------------

This module defines the abstract Person class used as the base class
for people in the hospital system.

The Person class provides common attributes shared by all people in
the hospital, such as name and age. It also defines the abstract
view_info() method, which must be implemented by subclasses such as
Patient and Staff.

Classes:
    Person: Abstract base class representing a person in the hospital.
"""

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

    def __init__(self, name:str, age:int):
        """
        Initialize a Person object.

        Args:
            name (str): The person's name.
            age (int): The person's age.
        """
        self.name = name
        self.age = age

    @abstractmethod
    def view_info(self)->str:
        """
        Return basic information about the object.

        This method must be implemented by all subclasses.

        Returns:
            str: A string containing information about the object.
        """
        pass

