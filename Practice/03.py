# Problem 3:
# Write a script using a for loop that:

# Prints all even numbers from 1 to 20 (inclusive).

# After that, I’ll follow up with a while loop task. Let’s go!

for number in range(2, 21, 2):
    print(number)

number = 2
while number <= 20:
    print(number)

    number += 2


# (While Loop)
# Write a script using a while loop that:

# Takes numbers from the user repeatedly.

# Stops taking input when the user enters 0.

# Finally, prints the sum of all entered numbers (excluding the 0).

total = 0

while True:
    num = int(input("Enter a number: "))

    if num == 0:
        break

    total = total + num

print("total numbers sum", total)