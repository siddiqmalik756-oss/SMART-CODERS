"""
Problem 9 [Operators / Relational & Logical Operators]
Read age and check eligibility to vote (age ≥ 18)
"""
def voting_eligibility(age):
    if age >= 18:
        return "Eligible to vote"
    return "Not eligible to vote"

if __name__ == "__main__":
    for age in [17, 18, 25]:
        print(f"Age {age}: {voting_eligibility(age)}")
