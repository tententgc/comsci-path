import Prob3 as p3


def test_1():
    primes_odd_dict = p3.Problem3(100)
    assert primes_odd_dict == {1: 2, 3: 5, 5: 11, 7: 17, 9: 23,
                               11: 31, 13: 41, 15: 47, 17: 59, 19: 67, 21: 73, 23: 83, 25: 97}


def test_2():
    primes_odd_dict = p3.Problem3(50)
    assert primes_odd_dict == {1: 2, 3: 5, 5: 11,
                               7: 17, 9: 23, 11: 31, 13: 41, 15: 47}
