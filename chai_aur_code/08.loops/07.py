while True:
    number = int(input("Enter a number b/w 1 to 10: "))

    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again!")