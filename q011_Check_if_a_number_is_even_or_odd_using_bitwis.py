"""
Problem 11 [Operators / Bitwise Operators]
Check if a number is even or odd using bitwise AND ( n & 1 )
"""
def is_even_bitwise(n):
    return "Even" if (n & 1) == 0 else "Odd"

if __name__ == "__main__":
    for n in [4, 7, 10]:
        print(f"{n}: {is_even_bitwise(n)}")
