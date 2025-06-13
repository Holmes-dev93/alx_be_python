#!/usr/bin/env python3

class BankAccount:
    """
    A simple BankAccount class to encapsulate banking operations.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float): The initial balance of the account. Defaults to 0.
        """
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Deducts the amount from account_balance if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if withdrawal is successful, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
