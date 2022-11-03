import numpy as np

def GaussianSwapForwardElimination(A,b):
    m,n = A.shape
    bn, = b.shape
    assert n==m==bn
    Aans = A.copy()
    bans = b.copy()
    l = list(range(n))
    sl = np.abs(A).max(axis=1)

    for i in range(n):
        if Aans[i,i] == 0:
            for j in range(i+1,n):
                if Aans[j,i] != 0:
                    Aans[[i,j]] = Aans[[j,i]]
                    bans[[i,j]] = bans[[j,i]]
                    l[i],l[j] = l[j],l[i]
                    break
        for j in range(i+1,n):
            mult = Aans[j,i]/Aans[i,i]
            Aans[j,:] = Aans[j,:] - mult*Aans[i,:]
            bans[j] = bans[j] - mult*bans[i]

    
    return Aans,bans,l

def GaussianSwapBacksubstitution(A,b,l):
    m,n = A.shape
    bn, = b.shape
    assert n==m==bn
    x = np.zeros(n,dtype=np.float64)
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i+1,n):
            sum += A[i,j]*x[j]
        x[l[i]] = (b[i]-sum)/A[i,i]
    return x


def Problem2(A,b):
    Aselem,bselem,l = GaussianSwapForwardElimination(A,b)
    x = GaussianSwapBacksubstitution(Aselem,bselem,l)
    return x
