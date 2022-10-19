import BisectionInterest;

def test_BisectionInterest():
    M = 600
    L = 150000
    m = 30
    eps =1e-4
    ans = 0.0259355
    assert ans-eps <= BisectionInterest.BisectionInterest(M,L,m) <= ans+eps
