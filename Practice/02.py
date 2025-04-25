# Write a script that:

# Takes an integer as input.

# Prints:
# "Positive" if it's greater than 0
# "Negative" if it's less than 0
# "Zero" if it's 0

number = int(input("Enter a int number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Neg")
else: 
    print("Zero")