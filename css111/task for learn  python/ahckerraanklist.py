g=[]
for i in range(int(input())):
    a=input().split()
    if a[0]=="insert":
        g.insert(int(a[1]) , int(a[2]))
    elif a[0]=="print":
        print(g)
    elif a[0]=="remove":
        g.remove(int(a[1]))
    elif a[0]=="append":
        
        g.append(int(a[1]))
    elif a[0]=="sort":
        g.sort()
    elif a[0]=="reverse":
        g.reverse()
    elif a[0] == "pop":
        g.pop()