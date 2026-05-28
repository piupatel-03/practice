a = input("Enter a Weight in kg : ")
b = input("Enter a Height in feet : ")
try:
    weight = float(a)
    height = float(b)

    # convert height from feet to meters
    height = height * 0.3048

    bmi = weight / (height * height)
    print("BMI:", bmi)
except ValueError:
        print("Invalid input")

if bmi < 18.5 :
    print("Underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print("Healthy weight")
elif bmi >= 25 and bmi < 29.9:
    print("Overweight")
else:
    print("Obese")


