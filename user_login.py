def validate_user(username, password):
    """
    Accepts a username and password.
    The user is valid only when:
      - username == "Admin"
      - password == "python123"
    Returns 'Valid User' or 'Invalid User'.
    """
    if username == "Admin" and password == "python123":
        return "Valid User"
    else:
        return "Invalid User"


# --- Example usage ---
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")

    result = validate_user(username, password)
    print(f"\n{result}")
