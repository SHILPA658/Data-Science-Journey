# Python Modules and Packages

# 1. Importing the math module
import math

number = 25

print("Square root:", math.sqrt(number))
print("Factorial:", math.factorial(5))
print("Value of pi:", math.pi)


# 2. Importing specific functions
from math import pow, ceil, floor

print("Power:", pow(2, 3))
print("Ceiling:", ceil(4.3))
print("Floor:", floor(4.8))


# 3. Importing with an alias
import random as rd

print("Random number:", rd.randint(1, 10))


# 4. Using the datetime module
import datetime

current_date = datetime.date.today()

print("Today's date:", current_date)


# 5. Creating and using our own module
# Suppose another file is named calculator.py

# calculator.py:
# def add(a, b):
#     return a + b

# In another Python file:
# import calculator
# print(calculator.add(10, 20))
