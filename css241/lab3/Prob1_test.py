import Prob1Newton as p1;

def test_1():
    eps =1e-6
    ans = 12.0
    a=(1,2,3,-4,5)
    fa = (2,48,272,1182,2262)
    x = -1
    assert ans-eps <= p1.newton(x,a,fa) <= ans+eps

def test_2():
    eps =1e-6
    ans = 0.5
    a=(0,2/3,1)
    fa = (1,0.5,0)
    x=-1
    assert ans-eps <= p1.newton(x,a,fa) <= ans+eps
