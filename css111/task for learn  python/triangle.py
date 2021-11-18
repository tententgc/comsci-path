def tri_check(a, b, c):
    z = [int(a), int(b), int(c)]
    z.sort()
    if z[0] < 0 or z[1] < 0 or z[2] < 0:
        print("negative ")
    elif 0 in z:
        print("zero")
    elif z[-1] >= z[0] + z[1]:
        print("not valid numbers")
    elif a == b == c:
        print("quailteral  ====== ")
    elif a == b or b == c or a == c:
        print("issoceles nha jao")
    elif z[-1]*z[-1] == ((z[0]*z[0] + z[1]*z[1])):
        print("retagorus ")
    else:
        print("traiangle")


print("*** Triangle check ***")
a, b, c = input("Enter side 1 side2 side3 : ").split()
tri_check(a, b, c)
