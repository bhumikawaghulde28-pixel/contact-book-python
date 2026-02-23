import json
import os

file_name = "contacts.json"

# load contacts from file
def load_contacts():
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return json.load(f)
    return {}

# save contacts to file
def save_contacts(contacts):
    with open(file_name, "w") as f:
        json.dump(contacts, f, indent=4)

contacts = load_contacts()

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    # ADD
    if choice == "1":
        name = input("Enter name: ")
        if name in contacts:
            print("Contact already exists")
        else:
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contacts[name] = {"phone": phone, "email": email}
            save_contacts(contacts)
            print("Contact added")

    # VIEW
    elif choice == "2":
        if not contacts:
            print("No contacts found")
        else:
            for name, info in contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")

    # SEARCH
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("Contact not found")

    # UPDATE
    elif choice == "4":
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            contacts[name] = {"phone": phone, "email": email}
            save_contacts(contacts)
            print("Contact updated")
        else:
            print("Contact not found")

    # DELETE
    elif choice == "5":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            save_contacts(contacts)
            print("Contact deleted")
        else:
            print("Contact not found")

    # EXIT
    elif choice == "6":
        print("Goodbye")
        break

    else:
        print("Invalid choice")