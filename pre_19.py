

input_data = input("Enter data in the format 'Name,Age,Score': ")
name, age, score = input_data.split(",")
# Convert the input data to integers
age = int(age)
score = int(score)
print("The name is", name)
print("The age is", age)
print("The score is", score)
name, age, score = input_data.split(",")

data = [(name, age, score)]

# Sort by name
sorted_by_name = sorted(name, key=lambda x: x[0])

# Sort by age
sorted_by_age = sorted(age, key=lambda x: x[1])

# Sort by score
sorted_by_score = sorted(score, key=lambda x: x[2])
print("Sorted by name:", sorted_by_name)
print("Sorted by age:", sorted_by_age)
print("Sorted by score:", sorted_by_score)

