"""
Problem 18 [Conditional Statements / if / if-else]
Find the largest of two numbers
"""
def largest_of_two(a, b):
    return a if a > b else b

if __name__ == "__main__":
    a, b = 12, 45
    print(f"Largest of {a} and {b} is {largest_of_two(a, b)}")
