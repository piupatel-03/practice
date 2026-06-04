
num = int(input("Enter a number: "))
if num > 1:
    if num > 100:
        print("Number is out of range")
        for i in range (2, 100):
            if (num % i) == 0:
                print(num, " is not a prime number")
                break
    else:
        print(num, " is a prime number")


        
