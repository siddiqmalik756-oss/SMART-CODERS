"""
Problem 8 [Operators / Relational & Logical Operators]
Read three numbers and check if all three are equal (use && )
"""
def all_three_equal(a, b, c):
    if a == b and b == c:
        return "All three numbers are equal"
    return "Numbers are not all equal"

if __name__ == "__main__":
    print(all_three_equal(5, 5, 5))
    print(all_three_equal(5, 5, 6))
