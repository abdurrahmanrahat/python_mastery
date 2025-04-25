# Write a program that:

# Takes 5 integers from the user and stores them in a list.

# Converts that list to a set.

# Prints both the list and the set.

# num1 = int(input("Give number 01: "))
# num2 = int(input("Give number 02: "))
# num3 = int(input("Give number 03: "))
# num4 = int(input("Give number 04: "))
# num5 = int(input("Give number 05: "))

# myList = [num1, num2, num3, num4, num5]

myList = []

for i in range(5):
    num = int(input(f"Give number {i + 1}: "))

    myList.append(num)

print("myList", myList)

# conversion
mySet = set(myList)

print("mySet", mySet)