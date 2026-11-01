contacts = {}
while True:
    try:
        print(' 1 — add contact\n', '2 — find number\n', '3 — delete contact\n', '4 — show all\n', '5 — edit contact\n', '0 — exit')
        choice = int(input('Choose an option: '))

        if choice == 1:
            number = input('Enter phone number: ')
            name = input("Enter contact name: ").capitalize()
            if name not in contacts:
               contacts[name] = [number]
            else:
                contacts[name].append(number)
        elif choice == 2:
            search = input('Search by name: ').capitalize()
            if search in contacts:
                print("Contact's number:", ', '.join(contacts[search]), '\n')
            else:
                print("No contact with this name\n")
        elif choice == 3:
            to_delete = input("Enter the name of the contact to delete: ").capitalize()
            if to_delete in contacts:
                del contacts[to_delete]
                print('Contact deleted\n')
            else:
                print("This contact doesn't exist\n")
        elif choice == 4:
            if len(contacts) == 0:
                print('The phonebook is empty\n')
            else:
                for name, number in contacts.items():
                    print(name + ':', ', '.join(number))
        elif choice == 5:
            edit = input("Enter name of contact to edit: ").capitalize()
            if edit in contacts:
                edited_phone = input("Enter a new number: ")
                contacts[edit] = [edited_phone]
                print("Number updated\n")
            else:
                print("This contact doesn't exist\n")
        elif choice == 0:
            break
        else:
            print('Invalid option')
    except ValueError:
        print("That's not a number!\n")
print('Goodbye, Master!')