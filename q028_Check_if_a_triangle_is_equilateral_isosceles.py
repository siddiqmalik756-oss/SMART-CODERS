"""
Problem 28 [Conditional Statements / if-else if-else (Ladder)]
Check if a triangle is equilateral, isosceles, or scalene given 3 sides
"""
def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

if __name__ == "__main__":
    print(triangle_type(5, 5, 5))
    print(triangle_type(5, 5, 8))
    print(triangle_type(3, 4, 5))
