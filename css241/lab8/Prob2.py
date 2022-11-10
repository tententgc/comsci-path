import numpy as np

def Jacobi(A,b,kmax):
    n = len(A)
    x = np.zeros(n)
    for k in range(kmax):
        xnew = np.zeros(n)
        for i in range(n):
            xnew[i] = 1.0/A[i,i]*(b[i]-np.dot(A[i,:],x)+A[i,i]*x[i])
        x = xnew
    return x


def Problem2(A,b):
    return Jacobi(A,b,21)
