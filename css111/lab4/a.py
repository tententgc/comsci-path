r = 10
n = 4
q_name = ["period  "]
for i in range(1,r+1):q_name.append(f"{i}%    ")
print(*q_name)

for x in range(1, n+1):
    for i in range(r+1):
        if i == 0:
            print(x, end='       ')
        else:
           print('{:.3f}'.format((1+i*0.01)**x), end='  ')
    print()