import math

r = float(input("Input the radius of the circle:"))
area = math.pi*r**2

print(f"The area of the circle with radius {r} is {area:.5f}" if r > 0 else "Error")
