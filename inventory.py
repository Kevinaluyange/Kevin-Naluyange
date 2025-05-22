current_inventory = {
    "Sacks of sugar" : 10,
    "Bags of wheat" : 5,
    "Sackets of salt" : 6,
    "Books" : 12
}
def display_inventory():
    print("\nCurrent Inventory: ")
    for item, quantity in current_inventory.items():
        print(f"{item}: {quantity}")

def add_item():
    item = input("Enter item to add: ").capitalize()
    quantity = int(input(f"Enter quantity for {item}: "))
    if item in current_inventory:
        current_inventory[item] += quantity
    else:
        current_inventory[item] = quantity
    print(f"{item} added successfully.\n")

def update_item():
    item = input("Enter item name to update: ").capitalize()
    if item in current_inventory:
        quantity = int(input(f"Enter new quantity for {item}: "))
        current_inventory[item] = quantity
        print(f"{item} updated successfully.\n")
    else:
        print("Item not found.\n")

def delete_item():
    item = input("Enter item name to delete: ").capitalize()
    if item in current_inventory:
        del current_inventory[item]
        print(f"{item} deleted from inventory sucessfully.\n")
    else:
        print("Item not found.\n")

def main():
    while True:
        print("My Inventory Management System")
        print("1. Display Current Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            display_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.\n")

main()

