
value = input("Enter a value to convert: ")
unit = input("Enter your choice (1 for Celsius to Fahrenheit, " 
                                "2 for Fahrenheit to Celsius): ")
try:
    value = float(value)
    if unit == "1":
        converted = (value * 9/5) + 32
        print(f"The temperature {value}°C is {converted}°F")
    elif unit == "2":
        converted = (value - 32) * 5/9
        print(f"The temperature {value}°F is {converted}°C")
    else:
        print("Invalid choice. Please enter '1' or '2'.")

except ValueError:
    print("Invalid value. Please enter a valid number.")