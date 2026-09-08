"""
Problem 20 [Conditional Statements / if / if-else]
Check if a character is a vowel or consonant
"""
def vowel_or_consonant(ch):
    ch = ch.lower()
    if ch in "aeiou":
        return "Vowel"
    elif ch.isalpha():
        return "Consonant"
    return "Not an alphabet"

if __name__ == "__main__":
    for ch in ["a", "b", "E", "5"]:
        print(f"'{ch}': {vowel_or_consonant(ch)}")
