# name : Ahmed Reda Mohamed
class BankAccount:
    """A simple bank account."""

    def __init__(self, balance=0):
        """Create an account with the given starting balance."""
        self.balance = balance

    def deposit(self, amount):
        """Add an amount to the account balance."""
        self.balance += amount
        print(f'Deposited {amount}. New balance: {self.balance}')

    def withdraw(self, amount):
        """Withdraw an amount when sufficient funds are available."""
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            print(f'Withdrew {amount}. New balance: {self.balance}')

    def check_balance(self):
        """Print the account's current balance."""
        print(f'Current balance: {self.balance}')