def printKwagrs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

printKwagrs(power="No", name="Rahat")
printKwagrs(power="No", name="Rahat", enimy="hello")