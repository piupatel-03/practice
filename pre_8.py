
total = 0
count = 0

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input == 'done':
        break
    number = float(user_input)
    total += number
    count += 1

print(f"Total: {total}")
print(f"Count: {count}")