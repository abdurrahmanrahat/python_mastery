import math

def circleStats(radius):
    area = round(math.pi * radius ** 2, 2)
    circumference = 2 * math.pi * radius

    return area, circumference

a, c = circleStats(3)

print("area ", a)
print("circumference ", c)