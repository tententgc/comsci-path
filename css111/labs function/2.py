import math


def trigonometry(x):

    sinx = math.sin(math.radians(x))
    cosx = math.cos(math.radians(x))

    return sinx,cosx


x = 0
while(x <= 360):
    result = trigonometry(x)
    print(f"{x:5} : sinx = {result[0]:7.2f}  cosx = {result[1]:7.2f} ")
    x += 22.5




