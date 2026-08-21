
# name : omar mohamed fathy

"""
Calculator Module
-----------------
This module provides basic arithmetic operations and an interactive 
Console User Interface (CLI). Designed to be used as a standalone 
application or imported into larger systems (e.g., Hospital Cost Calculator).
"""

class calc:
    """
    A class to perform fundamental mathematical operations and manage user interactions.
    """
    def __init__(self):
        """Initializes the calculator instance."""
        pass


    def add(self,a,b):
        """
        Calculates the sum of two numbers.

        Args:
            a (int | float): The first number.
            b (int | float): The second number.

        Returns:
            int | float: The result of adding a and b.
        """
        return a+b

    def subtraction(self,a,b):
        """
        Calculates the difference between two numbers.

        Args:
            a (int | float): The minuend.
            b (int | float): The subtrahend.

        Returns:
            int | float: The result of subtracting b from a.
        """
        return a-b

    def multiplication(self,a,b):
        """
        Calculates the product of two numbers.

        Args:
            a (int | float): The first factor.
            b (int | float): The second factor.

        Returns:
            int | float: The result of multiplying a and b.
        """
        return a*b

    def division(self,a,b):
        """
        Divides the first number by the second number.

        Args:
            a (int | float): The numerator.
            b (int | float): The denominator.

        Returns:
            float | str: The result of a / b, or an error message if b is 0.
        """
        if b!=0:
            return a/b
        else:
            return "Error! Division by zero."


    def calculator(self):
        """
        Runs the interactive menu loop for the calculator in the terminal.
        Handles user input, validation, and executes selected operations.
        """

        print('''
        Welcome to the Simple Calculator! 
        Select an operation:
        1. Addition (+)
        2. Subtraction (-)
        3. Multiplication (*)
        4. Division (/)
        ''')

        while True:



            operation=input("Enter your choice (1/2/3/4) or 'exit' to quit : ")
            if operation=="1" or operation=="2" or operation=="3" or operation=="4" or operation.lower()=="exit":
                if operation.lower()=="exit":
                    break
                while True:
                    try:
                        one=float(input("Enter First Number : "))
                        break
                    except Exception as e:
                        print(f"Invalid Value, please try again")

                while True:
                    try:
                        two=float(input("Enter Second Number : "))
                        break
                    except Exception as e:
                        print(f"Invalid Value, please try again")
                
                if operation=="1":
                    result=self.add(one,two)
                    print(f"{one} + {two} = {result}")
                elif operation=="2":
                    result=self.subtraction(one,two)
                    print(f"{one} - {two} = {result}")
                elif operation=="3":
                    result=self.multiplication(one,two)
                    print(f"{one} * {two} = {result}")
                elif operation=="4":
                    while two==0:
                        print("division by zero not allowed , try again")
                        two=float(input("Enter Second Number : "))
                        
                    result=self.division(one,two)
                    print(f"{one} / {two} = {result}")
                
            else:
                print("Invalid Choice ,try again\n")    

        print("Exiting the Calculator. Goodbye!")    




if __name__=="__main__":

    ob1=calc()

    ob1.calculator()
