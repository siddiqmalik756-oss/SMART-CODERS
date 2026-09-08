"""
Problem 12 [Operators / Bitwise Operators]
Swap two numbers using XOR
"""
def swap_using_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

if __name__ == "__main__":
    a, b = 5, 9
    print(f"Before swap: a={a}, b={b}")
    a, b = swap_using_xor(a, b)
    print(f"After swap:  a={a}, b={b}")
