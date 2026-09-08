"""
Problem 35 [Conditional Statements / Mixed / Applied]
Check if a given character is an alphabet, digit, or special character
"""
def char_category(ch):
    if ch.isalpha():
        return "Alphabet"
    elif ch.isdigit():
        return "Digit"
    else:
        return "Special character"

if __name__ == "__main__":
    for ch in ["A", "9", "@"]:
        print(f"'{ch}': {char_category(ch)}")
