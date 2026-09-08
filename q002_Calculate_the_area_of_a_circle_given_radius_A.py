"""
Problem 2 [Operators / Arithmetic Operators]
Calculate the area of a circle given radius (A = πr²)
"""
import math

def area_of_circle(radius):
    return math.pi * radius ** 2

if __name__ == "__main__":
    r = 5
    print(f"Radius = {r}")
    print(f"Area of circle = {area_of_circle(r):.4f}")
