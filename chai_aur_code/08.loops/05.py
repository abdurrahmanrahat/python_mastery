input_string = "teeter"

for char in input_string:
    if input_string.count(char) == 1:
        print("Non repeated character ", char)
        break