#Safe Calculator: Build a calculator that catches ZeroDivisionError, ValueError, and any 
#unexpected exception separately. 

def safe_calculator():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            raise ValueError("Invalid operator. Please use +, -, *, or /.")

        print(f"The result is: {result}")

    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    safe_calculator()

