a = input()
b = input()
al = len(a)
bl = len(b) 
q = 0
if al != bl:
    print("Incomplete answer")
else: 
    for i in range(len(a)):
        if a[i] == b[i]:
            q+=1
    print(q)