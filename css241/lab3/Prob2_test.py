import Prob2Lagrange as p2;

def test_secant1():
    eps =1e-6
    ans = 12.0
    a=(1,2,3,-4,5)
    fa = (2,48,272,1182,2262)
    x = -1
    assert ans-eps <= p2.Lagrange(x,a,fa) <= ans+eps

def test_secant2():
    eps =1e-6
    ans = 0.5
    a=(0,2/3,1)
    fa = (1,0.5,0)
    x=-1
    assert ans-eps <= p2.Lagrange(x,a,fa) <= ans+eps
    

