try: 
    f = open("lab5/myFile.txt", "r")
    print(f.read()) 
    print("uccessfully print content in myFile.txt ")
except: 
    print("Unable to open file myFile.txt")
