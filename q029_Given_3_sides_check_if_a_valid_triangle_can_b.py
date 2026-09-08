"""
Problem 29 [Conditional Statements / if-else if-else (Ladder)]
Given 3 sides, check if a valid triangle can be formed
"""
def is_valid_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return "Valid triangle"
    return "Not a valid triangle"

if __name__ == "__main__":
    print(is_valid_triangle(3, 4, 5))
    print(is_valid_triangle(1, 2, 10))
