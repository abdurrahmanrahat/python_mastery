# Examine the following Python code for any potential issues. What type of error is likely to occur when executing this function? 

def find_max (numbers): 
    max_num = numbers[0] 
    
    for num in numbers: 
        if num > max_num: 
            max_num = num 
            
    return max_num 

print(find_max([])) # IndexError

print(10 / 0)  #ZeroDivisionError

def myfunc():
print("Hello") # IndentationError

myList = [1, 2, 3]
# print(myList[5])  # ➔ IndexError

if True print("hello")  # ➔ SyntaxError

int("abc")  # ➔ ValueError

print("hello" + 5)  # ➔ TypeError

print(x)  # ➔ NameError

my_dict = {"name": "Abdur"}
print(my_dict["age"])  # ➔ KeyError