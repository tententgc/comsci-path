def mypi(n):
    ans = 3
    waitnum = 2
    for i in range(1, n+1):
        if i % 2 == 1:
            ans += (4/(waitnum * (waitnum+1) * (waitnum + 2)))
        else:
            ans -= (4/(waitnum * (waitnum+1) * (waitnum + 2)))
        waitnum += 2
        print(f'{i:2}  {ans}')

mypi(30)
