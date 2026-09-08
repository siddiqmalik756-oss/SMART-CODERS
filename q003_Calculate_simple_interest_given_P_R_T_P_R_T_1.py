"""
Problem 3 [Operators / Arithmetic Operators]
Calculate simple interest given P, R, T → (P × R × T) / 100
"""
def simple_interest(p, r, t):
    return (p * r * t) / 100

if __name__ == "__main__":
    p, r, t = 10000, 5, 2
    si = simple_interest(p, r, t)
    print(f"Principal = {p}, Rate = {r}%, Time = {t} years")
    print(f"Simple Interest = {si}")
