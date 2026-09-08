"""
Problem 19 [Conditional Statements / if / if-else]
Find the largest of three numbers
"""
def largest_of_three(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

if __name__ == "__main__":
    a, b, c = 12, 45, 33
    print(f"Largest of {a}, {b}, {c} is {largest_of_three(a, b, c)}")
