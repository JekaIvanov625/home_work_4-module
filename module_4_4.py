def parse_input(user_input):
    parts = user_input.strip().lower().split(maxsplit=2)
    command = parts[0]
    args = parts[1:] if len(parts) > 1 else []
    return command, args

def add_contact(contacts, args):
    if len(args) < 2:
        return "Usage: add [name] [phone number]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(contacts, args):
    if len(args) < 2:
        return "Usage: change [name] [new phone number]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(contacts, args):
    if len(args) < 1:
        return "Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {"Женя": "666948981"}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(contacts, args))
        elif command == "change":
            print(change_contact(contacts, args))
        elif command == "phone":
            print(show_phone(contacts, args))
        elif command == "all":
            print(show_all(contacts))
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
