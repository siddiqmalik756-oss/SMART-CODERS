"""
Problem 23 [Conditional Statements / if / if-else]
Time Greeting : Given an hour, print Morning, Afternoon, Evening, or Night.
"""
def time_greeting(hour):
    if 5 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    elif 17 <= hour < 21:
        return "Good Evening"
    else:
        return "Good Night"

if __name__ == "__main__":
    for h in [7, 14, 19, 23]:
        print(f"Hour {h}: {time_greeting(h)}")
