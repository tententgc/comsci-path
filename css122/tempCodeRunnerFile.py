import math

s  =int(input())
a  = math.log10(s)
if a.is_integer():
    print(a) 
print(f"{a:.5f}")