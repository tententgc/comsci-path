import numpy as np


def BisectionInterest(M, L, m):

    accurate = 0.0000000001
    epsilon = 1e-4
    b = 10

    def findR(r):
        return (((12*M)/r)*(1-(1+r/12)**(-12*m))) - L

    while (abs(findR(accurate) - findR(b)) > epsilon):
        mid = (accurate+b)/2
        if (np.sign(findR(accurate)) == np.sign(findR(mid))):
            accurate = mid
        else:
            b = mid

    return mid

print(BisectionInterest(600, 150000, 30))

# 64090500404 ธัญพิสิษฐ์ บัวประคอง