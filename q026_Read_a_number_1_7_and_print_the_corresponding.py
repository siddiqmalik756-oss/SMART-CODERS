"""
Problem 26 [Conditional Statements / if-else if-else (Ladder)]
Read a number (1–7) and print the corresponding day of the week
"""
def day_of_week(n):
    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday",
            5: "Friday", 6: "Saturday", 7: "Sunday"}
    return days.get(n, "Invalid day number")

if __name__ == "__main__":
    for n in [1, 5, 7, 9]:
        print(f"{n}: {day_of_week(n)}")
