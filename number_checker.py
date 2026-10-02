def check_number(n):
    """
    Accepts an integer and determines:
      - Whether the number is even or odd
      - Whether it is divisible by 3
      - Whether it is divisible by 5
    """
    # Even or Odd
    if n % 2 == 0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")

    # Divisible by 3
    if n % 3 == 0:
        print(f"{n} is divisible by 3")
    else:
        print(f"{n} is not divisible by 3")

    # Divisible by 5
    if n % 5 == 0:
        print(f"{n} is divisible by 5")
    else:
        print(f"{n} is not divisible by 5")


# --- Example usage ---
if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    print()
    check_number(number)
