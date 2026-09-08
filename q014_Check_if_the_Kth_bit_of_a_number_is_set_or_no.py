"""
Problem 14 [Operators / Bitwise Operators]
Check if the Kth bit of a number is set or not
"""
def is_kth_bit_set(n, k):
    return (n & (1 << k)) != 0

if __name__ == "__main__":
    n, k = 10, 1  # 10 = 1010, bit 1 is set
    result = is_kth_bit_set(n, k)
    print(f"n={n} (binary {bin(n)}), k={k}: bit is {'set' if result else 'not set'}")
