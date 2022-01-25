import random
queue = []
while len(queue) < 10:
    j = random.randint(0, 9)
    if j not in queue:
        queue.append(j)
print(*queue)


while True:
    a = int(input('>'))
    if a < 0:
        break
    queue.remove(a)
    queue.insert(0, a)
    print(*queue)
