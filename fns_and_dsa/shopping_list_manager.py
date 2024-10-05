# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty shopping list

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add an item to the shopping list
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("Item cannot be empty.")

        elif choice == '2':
            # Remove an item from the shopping list
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' is not in the shopping list.")

        elif choice == '3':
            # View the current shopping list
            if shopping_list:
                print("\nShopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
            else:
                print("\nYour shopping list is empty.")

        elif choice == '4':
            # Exit the loop and end the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
