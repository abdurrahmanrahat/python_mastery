# Write a program that:

# Stores the names and ages of 3 people in a dictionary.

# Prints each person's name and age in this format:
# "Alice is 25 years old."

people = {
    "rahat": 22,
    "mahtab": 24,
    "yasin": 21
}

for key, value in people.items():
    print(f"{key} is {value} years old.")