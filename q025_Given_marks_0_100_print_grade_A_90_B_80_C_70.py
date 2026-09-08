"""
Problem 25 [Conditional Statements / if-else if-else (Ladder)]
Given marks (0–100), print grade: A (≥90), B (≥80), C (≥70), D (≥60), F (<60)
"""
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    for m in [95, 82, 71, 60, 40]:
        print(f"Marks {m}: Grade {grade(m)}")
