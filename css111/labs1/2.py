import math
r = float(input("Input the radius of the circle:"))
if r <= 0:
    print("Error please input number more 0 ")
else:
    print("~", round(math.pi*r**2, 5))
