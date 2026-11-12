
# Python Set Operations

# Creating sets
numbers = {10, 20, 30, 40, 50}
another_numbers = {40, 50, 60, 70}

print("First set:", numbers)
print("Second set:", another_numbers)

# Adding an element
numbers.add(60)
print("After adding:", numbers)

# Removing an element
numbers.remove(20)
print("After removing:", numbers)

# Union
print("Union:", numbers.union(another_numbers))

# Intersection
print("Intersection:", numbers.intersection(another_numbers))

# Difference
print("Difference:", numbers.difference(another_numbers))

# Checking membership
print("Is 30 present?", 30 in numbers)

# Finding the length
print("Set length:", len(numbers))
