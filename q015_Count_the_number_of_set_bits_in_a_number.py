"""
Problem 15 [Operators / Bitwise Operators]
Count the number of set bits in a number
"""
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

if __name__ == "__main__":
    for n in [7, 10, 255]:
        print(f"{n} (binary {bin(n)}): {count_set_bits(n)} set bits")
