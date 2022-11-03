import numpy as np


# A,b are numpy array of size (n,n) and n for equation Ax=b
def GaussianForwardElimination(A, b):
    m, n = A.shape
    bn, = b.shape
    assert n == m == bn
    Aans = A.copy()
    bans = b.copy()
    l = list(range(n))
    sl = np.abs(A).max(axis=1)

    #Your Code Here
    for i in range(n):
        if Aans[i,i] == 0:
            for j in range(i+1,n):
                if Aans[j,i] != 0:
                    Aans[[i,j]] = Aans[[j,i]]
                    bans[[i,j]] = bans[[j,i]]
                    break
        for j in range(i+1,n):
            mult = Aans[j,i]/Aans[i,i]
            Aans[j,:] = Aans[j,:] - mult*Aans[i,:]
            bans[j] = bans[j] - mult*bans[i]
    # End your code

    return Aans, bans


def GaussianBacksubstitution(A, b):
    m, n = A.shape
    bn, = b.shape
    assert n == m == bn
    x = np.zeros(n, dtype=np.float64)
    #Your Code Here
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i+1,n):
            sum += A[i,j]*x[j]
        x[i] = (b[i]-sum)/A[i,i]
    # End your code
    return x




def Problem1(A, b):
    Aelem, belem = GaussianForwardElimination(A, b)
    x = GaussianBacksubstitution(Aelem, belem)
    return x
