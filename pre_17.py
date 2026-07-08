
def celsius_to_fahrenheit(*args):
    fahrenheit_values = []
    for celsius in args:
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_values.append(fahrenheit)
    return fahrenheit_values

def fahrenheit_to_celsius(*args):
    celsius_values = []
    for fahrenheit in args:
        celsius = (fahrenheit - 32) * 5/9
        celsius_values.append(celsius)
    return celsius_values

# usage:
celsius_values = [0, 25, 100]
fahrenheit_values = celsius_to_fahrenheit(*celsius_values)
print("Celsius to Fahrenheit:", fahrenheit_values)

fahrenheit_values = [32, 77, 212]
celsius_values = fahrenheit_to_celsius(*fahrenheit_values)
print("Fahrenheit to Celsius:", celsius_values)

