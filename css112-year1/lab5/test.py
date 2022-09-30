n = int(input())


if n % 2 == 1:
    for i in range(n):
        print(" "*i+"*")
else:
    for i in range(n, -1, -1):
        print(" "*i+"*")
