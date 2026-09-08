"""
Problem 34 [Conditional Statements / Nested if & switch-case]
Find the roots of a quadratic equation (check discriminant: real, equal, imaginary)
"""
import math

def quadratic_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2 * a)
        r2 = (-b - math.sqrt(d)) / (2 * a)
        return f"Two real roots: {r1:.2f}, {r2:.2f}"
    elif d == 0:
        r = -b / (2 * a)
        return f"One repeated real root: {r:.2f}"
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-d) / (2 * a)
        return f"Two imaginary roots: {real:.2f} + {imag:.2f}i, {real:.2f} - {imag:.2f}i"

if __name__ == "__main__":
    print(quadratic_roots(1, -3, 2))
    print(quadratic_roots(1, 2, 1))
    print(quadratic_roots(1, 0, 1))
