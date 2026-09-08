"""
Problem 17 [Conditional Statements / if / if-else]
Check if a year is a leap year
"""
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == "__main__":
    for y in [2000, 1900, 2024, 2023]:
        print(f"{y}: {'Leap year' if is_leap_year(y) else 'Not a leap year'}")
