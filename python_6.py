contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contacts[name] = {"Phone": phone, "Email": email}
        print("Contact added successfully.")

    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Contact Details:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to update: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")

            contacts[name]["Phone"] = phone
            contacts[name]["Email"] = email
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "5":
        if contacts:
            print("\nContact Names:", list(contacts.keys()))
            print("Contact Records:", list(contacts.values()))
            print("All Contacts:", list(contacts.items()))

            names = [name for name in contacts.keys()]
            print("Directory:", names)
        else:
            print("No contacts available.")

    elif choice == "6":
        print("Exiting Phonebook.")
        break

    else:
        print("Invalid choice.")
