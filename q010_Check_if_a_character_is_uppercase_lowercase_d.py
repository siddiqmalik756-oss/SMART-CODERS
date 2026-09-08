"""
Problem 10 [Operators / Relational & Logical Operators]
Check if a character is uppercase, lowercase, digit, or special character
"""
def char_type(ch):
    if ch.isupper():
        return "Uppercase"
    elif ch.islower():
        return "Lowercase"
    elif ch.isdigit():
        return "Digit"
    else:
        return "Special character"

if __name__ == "__main__":
    for ch in ["A", "z", "7", "#"]:
        print(f"'{ch}': {char_type(ch)}")
