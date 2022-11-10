import Prob1 as p1
import numpy as np

'''test x'''
def test_1():
    n = 4
    Aa = [[6,-2,2,4],[12,-8,6,10],[3,-13,9,3],[-6,4,1,-18]]
    bb = [16,26,-19,-34]
    A = np.array(Aa,dtype=np.float64)
    b = np.array(bb, dtype=np.float64)
    x = p1.Problem1(A,b)
    assert ( np.absolute(x - np.array([ 3.,  1., -2.,  1.]) )<1e-5).all()

'''test L,U'''
def test_2():
    n = 4
    Aa = [[6,-2,2,4],[12,-8,6,10],[3,-13,9,3],[-6,4,1,-18]]
    A = np.array(Aa,dtype=np.float64)
    L,U = p1.LUdecomposition(A)
    Areconstruct = np.dot(L,U)
    Lans = np.array([[ 1.,   0.,   0.,   0. ], [ 2.,   1.,   0.,   0. ], [ 0.5 , 3.,   1.,   0. ], [-1.,  -0.5,  2.,   1. ]],dtype = np.float64)
    assert (np.absolute(A-Areconstruct) <1e-8).all() and (np.absolute(L-Lans) <1e-8).all()
    
    
def test_3():
    n = 4
    Aa = [[6,-2,2,4],[12,-8,6,10],[3,-13,9,3],[-6,4,1,-18]]
    bb = [16,26,-19,-34]
    A = np.array(Aa,dtype=np.float64)
    b = np.array(bb, dtype=np.float64) 
    L,U = p1.LUdecomposition(A)
    z = p1.Lsubstitution(L,b)
    zans = np.array([16., -6., -9., -3.])
    assert ( np.absolute(z - zans )<1e-5).all()