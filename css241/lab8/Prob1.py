import numpy as np
def LUdecomposition(A):
    m,n = A.shape
    U = A.copy()
    L = np.zeros_like(U)
    np.fill_diagonal(L, 1)
    for i in range(n):
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]
        
    return L,U

# Calculae Lz=b
def Lsubstitution(L,b):
    m,n = L.shape

    z = np.zeros(n,dtype=np.float64)
    z[0] = b[0] / L[0, 0]
    
    for i in range(1, n):
        z[i] = (b[i] - np.dot(L[i,:i], z[:i])) / L[i,i]
        
    return z

# Calculate Ux = z
def GaussianBacksubstitution(A,b):
    m,n = A.shape

    x = np.zeros(n,dtype=np.float64)
    x[n-1] = b[n-1] / A[n-1, n-1]
    
    for i in range(n-2, -1, -1):
        x[i] = (b[i] - np.dot(A[i,i+1:], x[i+1:])) / A[i,i]
        
    return x


def Problem1(A,b): 
    #Your code here.
    L,U = LUdecomposition(A)
    z = Lsubstitution(L,b)
    x = GaussianBacksubstitution(U,z)
    #1. Calculate A=LU. Given A is known, find L,U
    #2. Calculate Lz=b  Given L from 1., and b from the problem, find z
    #3. Calculate Ux=z  Given U from 1., and z from 2., find x
    return x