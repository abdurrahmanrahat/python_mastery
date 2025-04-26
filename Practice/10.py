#  Write a script that:

# Opens a file named notes.txt in write mode.
# Writes three separate lines of text into the file.
# Closes the file.
# Reopens the same file in read mode.
# Prints out all the content.

with open("notes.txt", "w") as f:
    f.write("Hello world!\n")
    f.write("2nd line!\n")
    f.write("3rd line!\n")

# read the file
with open("notes.txt") as f:
    print(f.read())