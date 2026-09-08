"""
Problem 32 [Conditional Statements / Nested if & switch-case]
Check if a number is positive, negative, or zero — then if positive check even/odd
"""
def check_number(n):
    if n > 0:
        parity = "Even" if n % 2 == 0 else "Odd"
        return f"Positive and {parity}"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

if __name__ == "__main__":
    for n in [8, 7, -3, 0]:
        print(f"{n}: {check_number(n)}")
