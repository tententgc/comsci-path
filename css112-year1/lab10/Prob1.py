import numpy as np


def Problem1(n):
    onesk = np.ones((n, n))
    indx = [[i, j] for i in range(n) for j in range(n) if i < j]
    xyindx = tuple(zip(*indx))
    print(xyindx)
    onesk[xyindx] = 0
    return onesk

print(Problem1(5))