text = input("Enter a string: ")
a =  int(input("Enter a number for encoding: ")) 

def encoding(text,a):
    result = ""
    for i in range(len(text)):
        result += chr(((ord(text[i].upper()) + a - 65) % 26) + 65)
    return result

def decoding(text,a):
    result = ""
    for i in range(len(text)):
        result += chr(((ord(text[i].upper()) - a - 65) % 26) + 65)
    return result

print(encoding(text,a))

g = encoding(text,a) 
print(decoding(g,a)) 