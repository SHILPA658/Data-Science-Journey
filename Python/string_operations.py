
# Python String Operations

# Creating a string
text = "Data Science and Artificial Intelligence"

print("Original string:", text)

# Finding the length
print("Length:", len(text))

# Changing case
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())

# Replacing text
print("After replacement:", text.replace("Data Science", "Machine Learning"))

# Checking whether a word exists
print("Is Science present?", "Science" in text)

# Splitting a string
sentence = "Python is easy to learn"
print("Split words:", sentence.split())

# Joining strings
words = ["Python", "is", "powerful"]
print("Joined sentence:", " ".join(words))

# Accessing characters
print("First character:", text[0])
print("Last character:", text[-1])
