import math

a, b, c = [int(x) for x in input().split()]

compareValue = (b**2) - (4*a*c)

if compareValue < 0:
    print("No Solution in real numbers")
else:
    ans = math.sqrt(compareValue)
    x1 = (-b + ans)/(2*a)
    x2 = (-b - ans)/(2*a)

    if compareValue == 0:
        print(x1)
    else:
        print(x1, x2)
