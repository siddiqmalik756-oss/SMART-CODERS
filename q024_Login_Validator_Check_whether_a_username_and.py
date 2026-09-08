"""
Problem 24 [Conditional Statements / if / if-else]
Login Validator : Check whether a username and password combination is valid.
"""
VALID_USERNAME = "admin"
VALID_PASSWORD = "pass123"

def login_validator(username, password):
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return "Login successful"
    return "Invalid username or password"

if __name__ == "__main__":
    print(login_validator("admin", "pass123"))
    print(login_validator("admin", "wrong"))
