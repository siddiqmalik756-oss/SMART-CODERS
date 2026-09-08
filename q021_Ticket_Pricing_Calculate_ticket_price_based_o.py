"""
Problem 21 [Conditional Statements / if / if-else]
Ticket Pricing : Calculate ticket price based on the customer's age.
"""
def ticket_price(age):
    if age < 5:
        return 0
    elif age < 12:
        return 50
    elif age < 60:
        return 100
    else:
        return 60

if __name__ == "__main__":
    for age in [3, 8, 30, 65]:
        print(f"Age {age}: Ticket price = {ticket_price(age)}")
