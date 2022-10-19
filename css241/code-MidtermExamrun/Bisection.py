# Python program for implementation
# of Bisection Method for
# solving equations

import math
from numpy import log as ln 

# An example function whose
# solution is determined using
# Bisection Method.
# The function is x^3 - x^2  + 2
def func(x):
    return math.e**(-3*x) +2*x -2

# Prints root of func(x) 
# with error of EPSILON


def bisection(a, b):

    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return

    c = a
    i = 0
    while ((b-a) >= 10**-5):
        # Find middle point
        c = (a+b)/2

        # Check if middle point is root
        if (func(c) == 0.0):
            break

        # Decide the side to repeat the steps
        if (func(c)*func(a) < 0):
            b = c
        else:
            a = c
            
        print(f"x{i}: {c}")
        
        i+=1

    print("The value of root is : ", "%.6f" % c)

# Driver code
# Initial values assumed
a = 0
b = 1.6
bisection(a, b)

# This code is contributed
# by Anant Agarwal.
