"""
Problem 1 [Operators / Arithmetic Operators]
Read two numbers and print their sum, difference, product, quotient, and remainder
"""
def sum_diff_prod_quot_rem(a, b):
    return a + b, a - b, a * b, a / b, a % b

if __name__ == "__main__":
    a, b = 15, 4
    s, d, p, q, r = sum_diff_prod_quot_rem(a, b)
    print(f"a = {a}, b = {b}")
    print(f"Sum       = {s}")
    print(f"Difference = {d}")
    print(f"Product   = {p}")
    print(f"Quotient  = {q}")
    print(f"Remainder = {r}")
