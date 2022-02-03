import math

a = float(input()) 
l = 0
u = a 

x = (l+u)/2
while not math.isclose(a, 10**x):
    if 10**x > a:
        u = x
    else:
        l = x
    x = (l+u)/2 
print(round(x, 6)) 
