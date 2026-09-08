"""
Problem 5 [Operators / Arithmetic Operators]
Divisibility Check : Check whether a number is divisible by 3, 5, both, or neither.
"""
def divisibility_check(n):
    div3 = n % 3 == 0
    div5 = n % 5 == 0
    if div3 and div5:
        return "Divisible by both 3 and 5"
    elif div3:
        return "Divisible by 3"
    elif div5:
        return "Divisible by 5"
    else:
        return "Not divisible by 3 or 5"

if __name__ == "__main__":
    for n in [9, 10, 15, 7]:
        print(f"{n}: {divisibility_check(n)}")
