# Write a script that:

# Asks the user for an integer.
# Tries to calculate and print the square root.
# If a negative number is entered, catch the exception and print "Cannot take square root of a negative number."

import math

try:
    number = int(input("Enter an integer: "))
    if number < 0:
        raise ValueError("Cannot take square root of a negative number.")
    result = math.sqrt(number)
    print(f"The square root of {number} is {result}")
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("Program execution completed.")
