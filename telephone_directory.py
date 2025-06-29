# Telephone Directory System

directory = {}  # {phone_number: {'name': ..., 'address': ...}}

def show_menu():
    print("\n=== Telephone Directory Menu ===")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Modify Record")
    print("4. Delete Record")
    print("5. List All Records")
    print("6. Exit")

def add_record():
    phone = input("Enter phone number: ")
    if phone in directory:
        print("Record already exists.")
    else:
        name = input("Enter name: ")
        address = input("Enter address: ")
        directory[phone] = {'name': name, 'address': address}
        print("Record added successfully.")

def search_record():
    phone = input("Enter phone number to search: ")
    if phone in directory:
        print(f"Name: {directory[phone]['name']}")
        print(f"Address: {directory[phone]['address']}")
    else:
        print("Record not found.")

def modify_record():
    phone = input("Enter phone number to modify: ")
    if phone in directory:
        name = input("Enter new name: ")
        address = input("Enter new address: ")
        directory[phone] = {'name': name, 'address': address}
        print("Record updated.")
    else:
        print("Record not found.")

def delete_record():
    phone = input("Enter phone number to delete: ")
    if phone in directory:
        del directory[phone]
        print("Record deleted.")
    else:
        print("Record not found.")

def list_all_records():
    if not directory:
        print("No records found.")
    else:
        print("\n=== All Directory Records ===")
        for phone, info in directory.items():
            print(f"Phone: {phone}, Name: {info['name']}, Address: {info['address']}")

# Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_record()
    elif choice == '2':
        search_record()
    elif choice == '3':
        modify_record()
    elif choice == '4':
        delete_record()
    elif choice == '5':
        list_all_records()
    elif choice == '6':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
