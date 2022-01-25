r = 10
n = 4
print('Period', end='  ')
for i in range(1, r+1):
    print('{:.0f}%'.format(i), end='     ')
print("")
for x in range(1, n+1):
    for i in range(r+1):
        if i == 0:
            print(x, end='     ')
        else:
            print('{:.3f}'.format((1+i*0.01)**x), end='  ')
    print()



