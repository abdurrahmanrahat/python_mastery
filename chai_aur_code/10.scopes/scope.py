username = "rahat"

def func():
    username = "inside"

print("username", username)

x = 99
def func1():
    x = 88

print(x)

def func2():
    global x
    x = 1

func2()

print(x)

def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()


def chaicoder(num):
    def actual(x):
        return x ** num
    return actual



f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))