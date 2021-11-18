def triangle(nline, diff):
    counter = 1
    for i in range(nline):
        print("*" * counter)
        counter += diff


# nline   = int(input())
# diff = int (input())
triangle(4, 4)
