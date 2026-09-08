"""
Problem 13 [Operators / Bitwise Operators]
Find the value of n << 1 and n >> 1 — relate to multiply/divide by 2
"""
def shift_ops(n):
    return n << 1, n >> 1

if __name__ == "__main__":
    n = 10
    left, right = shift_ops(n)
    print(f"n = {n}")
    print(f"n << 1 = {left}  (multiply by 2)")
    print(f"n >> 1 = {right}  (divide by 2)")
