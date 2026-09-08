"""
Problem 22 [Conditional Statements / if / if-else]
Age Category : Classify a person as a child, teenager, adult, or senior based on age.
"""
def age_category(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

if __name__ == "__main__":
    for age in [10, 16, 35, 70]:
        print(f"Age {age}: {age_category(age)}")
