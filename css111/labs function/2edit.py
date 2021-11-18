import math


def trigonometry(x):
    # sinx = math.sin(x)
    # cosx = math.cos(x)
    sinx = math.sin(math.radians(x))
    cosx = math.cos(math.radians(x))
    # sinx = math.sin(math.degrees(x))
    # cosx = math.cos(math.degrees(x))
    return sinx, cosx


x = 0
while(x <= 360):
    result = trigonometry(x)
    print(f"{x} : sinx  = {result[0]:.2f}  cosx = {result[1]:.2f} ")
    x += 22.5


# for i in range(16):
#     print(" x = {}  :  sinx  ={:.2f} :  cosx  = {:.2f} ".format(x,trigonometry(x)[0], trigonometry(x)[1]))
#     x += 22.5


# while(x<=360):
#     print(" x = {}  :  sinx  ={:.2f} :  cosx  = {:.2f} ".format(x,trigonometry(x)[0], trigonometry(x)[1]))
#     x+=22.5
