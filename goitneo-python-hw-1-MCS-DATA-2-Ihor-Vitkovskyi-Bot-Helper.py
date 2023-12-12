def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_phone(args, contacts):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return f"{name}'s phone updated to {new_phone}."
        else:
            return f"Contact {name} not found."
    else:
        return "Invalid input"
    
def phone_username(search_name, contacts):
    return contacts.get(search_name, "Contact not found")   
        
def all_contacts(contacts):
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result       

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))    
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "phone":
            search_name = args[0]
            print(phone_username(search_name, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()