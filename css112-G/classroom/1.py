from re import I


n = int(input("Enter a number: "))
k = int(input("Enter another number: ")) 

def findNumber():
    i = k 
    while i<=n:
        print(i)
        i = i + k 

findNumber()