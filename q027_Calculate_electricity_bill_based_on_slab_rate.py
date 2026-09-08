"""
Problem 27 [Conditional Statements / if-else if-else (Ladder)]
Calculate electricity bill based on slab rates
"""
def electricity_bill(units):
    if units <= 100:
        return units * 5
    elif units <= 300:
        return 100 * 5 + (units - 100) * 7
    else:
        return 100 * 5 + 200 * 7 + (units - 300) * 10

if __name__ == "__main__":
    for u in [80, 250, 400]:
        print(f"Units {u}: Bill = {electricity_bill(u)}")
