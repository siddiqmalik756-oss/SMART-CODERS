"""
Problem 30 [Conditional Statements / Nested if & switch-case]
Build a simple calculator (+, −, ×, ÷) using switch-case
"""
def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operator"

if __name__ == "__main__":
    print(calculator(10, 5, '+'))
    print(calculator(10, 5, '-'))
    print(calculator(10, 5, '*'))
    print(calculator(10, 5, '/'))
