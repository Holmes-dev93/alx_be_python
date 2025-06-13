#!/usr/bin/env python3

import sys
from bank_account import BankAccount

def main():
    """
    Interacts with the BankAccount class through command line arguments for banking operations.
    """
    # Initialize the account with an example starting balance
    # The project description shows this line in main-0.py
    account = BankAccount(100)

    # Check for minimum number of arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    try:
        command_arg = sys.argv[1]
        command_parts = command_arg.split(':', 1)
        command = command_parts[0]
        amount = None

        if len(command_parts) > 1:
            try:
                amount = float(command_parts[1])
            except ValueError:
                print("Error: Invalid amount. Please provide a numeric value.")
                sys.exit(1)

        if command == "deposit":
            if amount is not None:
                account.deposit(amount)
                print(f"Deposited: ${amount:.2f}")
            else:
                print("Error: Deposit command requires an amount.")
                print("Usage: python main-0.py deposit:<amount>")
                sys.exit(1)
        elif command == "withdraw":
            if amount is not None:
                if account.withdraw(amount):
                    print(f"Withdrew: ${amount:.2f}")
                else:
                    print("Insufficient funds.")
            else:
                print("Error: Withdraw command requires an amount.")
                print("Usage: python main-0.py withdraw:<amount>")
                sys.exit(1)
        elif command == "display":
            if amount is not None:
                print("Warning: 'display' command does not take an amount. Ignoring.")
            account.display_balance()
        else:
            print("Invalid command.")
            print("Commands: deposit, withdraw, display")
            sys.exit(1)

    except ValueError as e:
        # Catch value errors potentially from BankAccount methods
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
