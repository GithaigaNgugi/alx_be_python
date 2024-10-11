# shopping_list_manager.py

# Initialize an empty shopping list
shopping_list = []

def display_menu():
    """Display the main menu with options."""
    print("\n--- Shopping List Manager ---")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

def add_item():
    """Prompt the user to add an item to the shopping list."""
    item = input("Enter the name of the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the list.")
    else:
        print("Item name cannot be empty.")

def remove_item():
    """Prompt the user to remove an item from the shopping list."""
    item = input("Enter the name of the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' not found in the shopping list.")

def view_list():
    """Display all items currently in the shopping list."""
    if shopping_list:
        print("\nCurrent Shopping List:")
        for idx, item in enumerate(shopping_list, 1):
            print(f"{idx}. {item}")
    else:
        print("\nYour shopping list is empty.")

def shopping_list_manager():
    """Main function to run the shopping list manager."""
    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            view_list()
        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    shopping_list_manager()