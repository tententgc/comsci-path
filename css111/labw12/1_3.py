import random

# mylist = list(range(10))
# random.shuffle(mylist)


mylist = []
while len(mylist) < 10:
    number = random.randint(0, 9)
    if number not in mylist:
        mylist.append(number)

print(mylist)
while True:
    x = int(input('Enter a number: '))
    if x < 0:
        break
    mylist.pop(mylist.index(x))
    mylist.insert(0, x)
    print(mylist)
