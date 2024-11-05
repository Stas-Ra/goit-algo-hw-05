
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return """
            if you want to add or change a contact, enter name
            and phone for the command.
            And if you want to view a phone, enter a name for the command.
            """
        except KeyError:
            return "This key is not relevant for the command"
        except IndexError:
            return """
            I have no idea under what conditions the IndexError
            can be called in this bot, but so be it
            """
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated"
    else:
        return "This name not found"

@input_error
def show_phone(args, contacts):
    name, *_ = args
    if name in contacts: 
        result = contacts.get(name)
        return result
    else:
        return "This name is not in contacts"

@input_error
def show_all(contacts):     
    result = ""
    for key, value in contacts.items():
        result = result + f"{key}: {value}\n"
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
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("I am a loser bot, and not understand this command.")

if __name__ == "__main__":
    main()
    