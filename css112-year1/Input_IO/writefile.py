f = open("Input_IO/test.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("Input_IO/test.txt", "r")
print(f.read())
