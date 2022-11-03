import Prob1 as p1
import numpy as np

def test_1():
    n = 4
    Aa = [[6,-2,2,4],[12,-8,6,10],[3,-13,9,3],[-6,4,1,-18]]
    bb = [16,26,-19,-34]
    A = np.array(Aa,dtype=np.float64)
    b = np.array(bb, dtype=np.float64)
    x = p1.Problem1(A,b)
    assert ( np.absolute(x - np.array([ 3.,  1., -2.,  1.]) )<1e-5).all()


