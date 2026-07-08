#Password Generator: Use the random and string modules to write a function
#generate_password(length=12, include_symbols=True).

import random
import string
def generate_password(length=12, include_symbols=True):
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#Example usage
print(generate_password())
print(generate_password(length=16, include_symbols=False))

