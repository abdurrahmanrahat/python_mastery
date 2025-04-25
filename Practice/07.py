# Takes a full name as input.

# Prints:

# The name in uppercase
# The number of characters (excluding spaces)
# A list of the name parts (split by space)

name = input("Enter your full name: ")

print(name.upper())
print(len(name.replace(" ", "")))
print(name.split(" "))


