def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()

        user_choice = input("Enter choice from the above: ")

        if user_choice == "1":
            added_item = input("Enter the item to add: ")
            shopping_list.append(added_item)
            print(f"You have added: {added_item}")
        elif user_choice == "2":
            removed_item = input("Enter the item to remove: ")
            shopping_list.remove(removed_item)
            print(f"You have removed: {removed_item}")
        elif user_choice == "3":
            print(f"Your shopping list has: {shopping_list}")
        elif user_choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")
            


main()