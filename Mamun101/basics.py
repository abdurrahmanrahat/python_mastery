print("I love BD")

# variables -----------------------
a = 10
b = 12

myName = 'Rahat'

print(a + b)
print(myName)

# data types ------------------

# 10 - int 
# 2.4 - float
# "hello" - string

#Type Casting: take input from user ---------------
firstNum = 10
# secondNum = input("Enter a number: ")

# print(firstNum + int(secondNum))

# operators -----------------------
# arithmetic = +, -, *, /, %
# comparator = <, >, <=, >=
# logical = and, or, not

# conditional statement --------------------
# if condition:
#     statement

age = 22
if age > 21:
    print("Legal for marriage.")
else: 
    print("Not legal for marriage.")
    
# loop ----------------------------
for i in range(5):
    print(i)

# to start from 1 
for i in range(1, 5):
    print(i)

# to skip: start - end - skip
for i in range(1, 6, 2):
    print(i)
    
# 1 + 2 + 3 + 4 ... + 100 = ?
sum = 0
for i in range(1, 101):
    sum = sum + i
    
print(sum)

# while loop ------------------------
# while condition:
#     statement

i = 1
sum2 = 0
while i < 102:
    sum2 = sum2 + i
    i = i + 1
    
print(sum2)