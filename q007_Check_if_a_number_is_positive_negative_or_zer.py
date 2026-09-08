"""
Problem 7 [Operators / Relational & Logical Operators]
Check if a number is positive, negative, or zero
"""
def sign_check(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

if __name__ == "__main__":
    for n in [5, -3, 0]:
        print(f"{n}: {sign_check(n)}")
