import math

x = 2
f = (math.pi*x) - (3/x) + (7*(x**5)) - (math.log(x,10)) - math.e**-x



print(f if x > 0 else "Error") 
