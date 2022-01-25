import math
# a, b, c = [int(x) for x in input().split()]


a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

check_ans = pow(b, 2)-4*a*c

if check_ans == 0:
    x1 = ((-b + math.sqrt(pow(b, 2)-4*a*c))/(2*a))
    print(round(x1, 5))

elif check_ans > 0:
    x1 = ((-b + math.sqrt(pow(b, 2)-4*a*c))/(2*a))
    x2 = ((-b - math.sqrt(pow(b, 2)-4*a*c))/(2*a))
    print(str(round(x1, 5)) + ", " + str(round(x2, 5)))

elif check_ans < 0:
    print("No Solution in real number.")
