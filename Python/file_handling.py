# Python File Handling

# 1. Writing data into a file
file = open("sample.txt", "w")
file.write("Hello! I am learning Python.\n")
file.write("This is my file handling practice.")
file.close()

print("Data written successfully.")

# 2. Reading data from a file
file = open("sample.txt", "r")
content = file.read()
print("\nFile content:")
print(content)
file.close()

# 3. Appending data to a file
file = open("sample.txt", "a")
file.write("\nI am practising Python every day.")
file.close()

print("\nNew data appended successfully.")

# 4. Reading line by line
file = open("sample.txt", "r")
print("\nReading line by line:")

for line in file:
    print(line.strip())

file.close()

# 5. Using the with statement
with open("sample.txt", "r") as file:
    content = file.read()
    print("\nUsing with statement:")
    print(content)
