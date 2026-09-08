"""
Problem 33 [Conditional Statements / Nested if & switch-case]
Given 3 numbers, print them in ascending order using only if-else
"""
def ascending_order(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

if __name__ == "__main__":
    print(ascending_order(5, 2, 8))
    print(ascending_order(9, 1, 4))
