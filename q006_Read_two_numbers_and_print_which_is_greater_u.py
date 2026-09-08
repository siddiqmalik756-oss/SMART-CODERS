"""
Problem 6 [Operators / Relational & Logical Operators]
Read two numbers and print which is greater (use relational operators)
"""
def greater_of_two(a, b):
    if a > b:
        return f"{a} is greater"
    elif b > a:
        return f"{b} is greater"
    else:
        return "Both numbers are equal"

if __name__ == "__main__":
    a, b = 23, 45
    print(greater_of_two(a, b))
