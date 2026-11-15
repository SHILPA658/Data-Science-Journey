# Python Exception Handling
# 1. Basic try and except

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Invalid input! Please enter a number.")


# 2. Handling division by zero

try:
    num1 = 10
    num2 = 0

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide a number by zero.")

# 3. Using multiple except blocks

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")


# 4. Using else

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("Valid number:", number)


# 5. Using finally

try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("The file does not exist.")

finally:
    print("File operation completed.")


# 6. Raising an exception

age = 15

try:
    if age < 18:
        raise ValueError("You must be at least 18 years old.")

    print("You are eligible.")

except ValueError as error:
    print("Error:", error)


# 7. Creating a custom exception

class InvalidAgeError(Exception):
    pass


try:
    age = 16

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("Registration successful.")

except InvalidAgeError as error:
    print("Registration failed:", error)
