def sumOfAll(*args):
    print("args", args) #args (1, 2, 3)
    print("*args", *args) # *args 1 2 3

    for i in args:
        print(i * 2)

    return sum(args)

print(sumOfAll(1, 2, 3))
# print(sumOfAll(1, 2, 3, 4, 5))