"""
Problem 4 [Operators / Arithmetic Operators]
Convert temperature from Celsius to Fahrenheit and vice versa
"""
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

if __name__ == "__main__":
    c = 37
    f = 98.6
    print(f"{c} C = {celsius_to_fahrenheit(c):.2f} F")
    print(f"{f} F = {fahrenheit_to_celsius(f):.2f} C")
