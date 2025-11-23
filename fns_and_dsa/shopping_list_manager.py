def display_menu():
    """Prints the menu options for the shopping list manager."""
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("----------------------------")

def main():
    """
    Main function to run the shopping list manager loop.
    """
    # Initialize an empty list to store the shopping items
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # 1. Add Item
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add:
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' has been added to the list.")
            else:
                print("Item name cannot be empty.")

        elif choice == '2':
            # 2. Remove Item
            if not shopping_list:
                print("The shopping list is already empty. Nothing to remove.")
                continue
                
            item_to_remove = input("Enter the item to remove: ").strip()
            
            try:
                # Use the list's remove method. It raises a ValueError if the item is not found.
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from the list.")
            except ValueError:
                # Handle the case where the item is not in the list
                print(f"Error: '{item_to_remove}' was not found in the list.")

        elif choice == '3':
            # 3. View List
            print("\n*** Your Current Shopping List ***")
            if not shopping_list:
                print("The list is empty!")
            else:
                # Iterate through the list and display each item with a number
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            print("**********************************")

        elif choice == '4':
            # 4. Exit
            print("\nGoodbye! Happy Shopping!")
            break
        
        else:
            # Handle invalid input
            print("\nInvalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
