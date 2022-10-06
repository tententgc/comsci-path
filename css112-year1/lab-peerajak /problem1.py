def p1():
    x = input().split()
    c = input()
    ans = []
    for i in x:
        if c in i:
            ans.append(i.count(c))
    print(*ans)


p1()
