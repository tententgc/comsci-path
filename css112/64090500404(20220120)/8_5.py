from math import *
x, y = map(float, input().split())
r = (x**2 + y**2 ) ** 0.5
theta= atan2(y,x) 
print(r, theta) 