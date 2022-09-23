def multiply(a, b):
    if b<=12: 
        print(f"{a} x {b} = {a*b}")
        multiply(a,b+1)

    

num = int(input("Enter a number: ")) 
print("Multiplication table for",num) 
multiply(num, 1)