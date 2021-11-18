def adder(num1, num2):
    a= float(num1) + float(num2)
    if a%1 == 0:
        return int(a)
    else:
        return a

print("**** Adder function *****")
num1,num2 = input('Enter 2 numbers: ').split()
result = adder(num1, num2)

fstring = f"{num1} + {num2} = {result}"
print(fstring) 