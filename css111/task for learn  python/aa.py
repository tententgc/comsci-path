def slope(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        m = -a / b
        if m % 1 == 0:
            return str(int(m))
        else:
            return str(round(m, 2))
    except:
        return "Not Availble"


def xIntercept(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        x = -c/a
        if x % 1 == 0:
            return str(int(x))
        else:
            return str(round(x, 2))
    except:
        return "Not Availble"


def yIntercept(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        y = -c / b
        if y % 1 == 0:
            return str(int(y))
        else:
            return str(round(y, 2))
    except:
        return "Not Availble"


print(" *** XY Intercept ***\n -- ax + by + c = 0 --")
a, b, c = input("Enter a b c : ").split()
print("Slope = " + slope(a, b, c))
print(" x-intercept => " + xIntercept(a, b, c))
print(" y-intercept => " + yIntercept(a, b, c))
