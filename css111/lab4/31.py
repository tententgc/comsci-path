r = 10
n = 5
q_printer = []
q_name = ["period  "]
for i in range(1, r+1): q_name.append(f"{i}%     ")
print(*q_name)

for x in range(1, n+1):
    q_list = []
    q_list.append(f"{x}     ")
    for i in range(1, r+1):
        q_list.append('{:.3f}  '.format((1+i*0.01)**x))
    print(*q_list)
