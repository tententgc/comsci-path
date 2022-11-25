import numpy as np 

def Jacobi(A, b, kmax=20):
    x = np.zeros_like(b)
    for k in range(kmax):
        xnew = np.zeros_like(x)
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], xnew[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            xnew[i] = (b[i] - s1 - s2) / A[i, i]
        x = xnew
    return x

def Problem2(x, xi, yi):
    
    ti = np.array(xi)
    yi = np.array(yi)
    A = np.zeros((len(ti), len(ti)))
    
    A[0, 0] = 1
    A[-1, -1] = 1
    
    for i in range(1, len(ti)-1):
        A[i, i-1] = ti[i] - ti[i-1]
        A[i, i] = 2 * (ti[i+1] - ti[i-1])
        A[i, i+1] = ti[i+1] - ti[i]
        
    b = np.zeros(len(ti))
    b[1:-1] = 3 * (yi[2:] - yi[1:-1]) / (ti[2:] - ti[1:-1]) - 3 * (yi[1:-1] - yi[:-2]) / (ti[1:-1] - ti[:-2])
    z = Jacobi(A, b)
    eq_list = []
    ans = 0
    
    for i in range(len(ti) - 1):
        a = (z[i+1] - z[i]) / (3 * (ti[i+1] - ti[i]))
        b = z[i]
        c = (yi[i+1] - yi[i]) / (ti[i+1] - ti[i]) - (2 * z[i] + z[i+1]) * (ti[i+1] - ti[i]) / 3
        d = yi[i]
        eq_list.append((a, b, c, d))
        
        
    for i in range(len(ti) - 1):
        if ti[i] <= x <= ti[i+1]:
            ans = eq_list[i][0] * (x-ti[i])**3 + eq_list[i][1] * (x-ti[i])**2 + eq_list[i][2] * (x-ti[i]) + eq_list[i][3]
            break
        
    return ans
