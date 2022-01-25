import math


def quadraticChecker(a:float, b:float, c:float):
    check = (b*b)-4*a*c
    if check > 0:
        x1 = ((-b + math.sqrt(check))/(2*a))
        x2 = ((-b - math.sqrt(check))/(2*a))
        print(str(round(x1, 5)) + ", " + str(round(x2, 5)))
    elif check == 0:
        x1 = ((-b + math.sqrt(check))/(2*a))
        print(x1)
    return check


print(" *** quadratic checker ***")
print("     ax^2 + bx + c = 0    ")
a, b, c = input("Enter a b c :").split()

a,b,c = float(a),float(b),float(c)

checker = quadraticChecker(a, b, c)

if checker < 0:
    print("there is NO VAID solution.")
elif checker == 0:
    print("there is only one solution.")
else:
    print("there are Two solution.")
