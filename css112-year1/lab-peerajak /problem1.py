def p1():
    x = input().split()
    c = input()
    
    #ในเคสถ้าไม่มีก็นับ
    ans = [i.count(x) for i in x] 
    
    #เคสมีก็นับจะใช้อันล่าง
    # ans = [i.count(c) for i in x if c in i]
    print(*ans)


p1()
