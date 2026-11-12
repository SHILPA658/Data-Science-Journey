
# Python Dictionary Operations

# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Computer Science",
    "marks": 85
}

print("Student details:", student)

# Accessing values
print("Student name:", student["name"])
print("Student age:", student["age"])

# Adding a new key-value pair
student["city"] = "Bangalore"
print("After adding city:", student)

# Updating a value
student["marks"] = 90
print("After updating marks:", student)

# Removing an item
student.pop("age")
print("After removing age:", student)

# Displaying keys
print("Dictionary keys:", student.keys())

# Displaying values
print("Dictionary values:", student.values())

# Iterating through a dictionary
for key, value in student.items():
    print(key, ":", value)
