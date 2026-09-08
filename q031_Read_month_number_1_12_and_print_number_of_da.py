"""
Problem 31 [Conditional Statements / Nested if & switch-case]
Read month number (1–12) and print number of days in that month
"""
def days_in_month(month, year=2024):
    days_map = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return 29
    return days_map.get(month, "Invalid month")

if __name__ == "__main__":
    for m in [2, 4, 12]:
        print(f"Month {m}: {days_in_month(m)} days")
