def gen5odds():
    a = 1
    while a < 100:
        yield [a, a+2, a+4, a+6, a+8]
        a += 10

def Problem1(): 
    return list(map(sum, gen5odds()))

