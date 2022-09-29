f = open("Input_IO/test.txt", "a")
f.write("This is a new line")
f.close()

f = open("Input_IO/test.txt", "r")
print(f.read())
f.close()