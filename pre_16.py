

contact_book = {}
def add_contact(name, phone):
    contact_book[name] = phone
    print(f"Contact '{name}' added successfully.")

def search_contact(name):
    if name in contact_book:
        print(f"Contact '{name}': {contact_book[name]}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def display_contacts():
    if contact_book:
        print("Contact Book:")
        for name, phone in contact_book.items():
            print(f"{name}: {phone}")
    else:
        print("Contact book is empty.")