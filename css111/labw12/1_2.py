def mypi(n):
    answer = 3
    waitnum = 2
    for i in range(1, n+1):
        check = (4/(waitnum * (waitnum+1) * (waitnum + 2)))
        answer += check if i % 2 == 1 else -check
        waitnum += 2
    return (f'{i:2}  {answer}')

for i in range(1,31):
    print(mypi(i))

