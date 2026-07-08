x = input ("Type a number:")
y = input("Type another number: ")
sum = int(x) + int(y)

print("The sum is:", sum)



# calculator module:

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    
def power(base, esp=2):
    return base ** esp

def calculator(*args, operation="add"):
    if operation not in ops:
        