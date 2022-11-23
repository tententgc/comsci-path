import Prob1 as p1


def test_1():
    g9 =   p1.gen5odds() 
    a1 = next(g9)
    for k in range(8):
        next(g9)
    a10 = next(g9)
    assert a1 == [1, 3, 5, 7, 9] and a10 == [91,93,95,97,99] 

def test_2():
    a = p1.Problem1()
    assert a == [25, 75, 125, 175, 225, 275, 325, 375, 425, 475]
