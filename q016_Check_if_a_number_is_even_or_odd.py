"""
Problem 16 [Conditional Statements / if / if-else]
Check if a number is even or odd
"""
def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

if __name__ == "__main__":
    for n in [4, 7]:
        print(f"{n}: {even_or_odd(n)}")
