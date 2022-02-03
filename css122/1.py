

i = []
while True: 
    a = input()
    if (a=="q"):
        break
    else: 
        i.append(float(a))
        avg = sum(i)/len(i)

if len(i)<1:
    print("No Data")
else:
    print(round(avg,2))