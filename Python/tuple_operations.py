
# Python Tuple Operations

# Creating a tuple
colors = ("Red", "Blue", "Green", "Yellow")

print("Original tuple:", colors)

# Accessing elements
print("First color:", colors[0])
print("Last color:", colors[-1])

# Finding the length
print("Number of colors:", len(colors))

# Checking whether an element exists
print("Is Blue present?", "Blue" in colors)

# Counting elements
numbers = (10, 20, 10, 30, 10, 40)
print("Count of 10:", numbers.count(10))

# Finding the index
print("Index of Green:", colors.index("Green"))

# Iterating through a tuple
print("All colors:")
for color in colors:
    print(color)
