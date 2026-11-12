
# Python List Operations

# Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original list:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Adding an element
fruits.append("Grapes")
print("After adding:", fruits)

# Removing an element
fruits.remove("Banana")
print("After removing:", fruits)

# Sorting the list
fruits.sort()
print("Sorted list:", fruits)

# Finding the length
print("Number of fruits:", len(fruits))

# Iterating through a list
print("All fruits:")
for fruit in fruits:
    print(fruit)
