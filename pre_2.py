a = (float(input("Enter first number :")))
b = (float(input("Enter second number :")))

#sum 
sum = a + b
difference = a - b
product = a * b

# division and modulus
if b != 0:
    quotient = a / b
    remainder = a % b
else:
    quotient = "Undefined (cannot divide by zero)"
    remainder = "Undefined (cannot divide by zero)"


print("Sum: ", sum)
print("Difference: ", difference)
print("Product: ", product)
print("Quotient: ", quotient)
print("Remainder: ", remainder)















