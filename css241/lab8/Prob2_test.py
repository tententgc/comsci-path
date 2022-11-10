import Prob2 as p2
import numpy as np

def test_1():
    Aa = [[2,-1,0],[-1,3,-1],[0,-1,2]]
    bb = [1,8,-5]
    A = np.array(Aa,dtype=np.float64)
    b = np.array(bb, dtype=np.float64)
    x = p2.Problem2(A,b)
    assert ( np.absolute(x - np.array([ 2.,  3., -1.]) )<1e-3).all()


