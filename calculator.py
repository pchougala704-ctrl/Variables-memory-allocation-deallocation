def calculator(a, b):
    """Perform basic arithmetic operations on two numbers."""
    addition       = a + b
    subtraction    = a - b
    multiplication = a * b
    floor_division = a // b
    remainder      = a % b

    # Guard against division by zero
    if b == 0:
        division = "undefined (division by zero)"
    else:
        division = a / b

    print(f"Addition       : {a} + {b} = {addition}")
    print(f"Subtraction    : {a} - {b} = {subtraction}")
    print(f"Multiplication : {a} * {b} = {multiplication}")
    print(f"Division       : {a} / {b} = {division}")
    print(f"Floor Division : {a} // {b} = {floor_division}")
    print(f"Remainder      : {a} % {b} = {remainder}")


# --- Example usage ---
if __name__ == "__main__":
    num1 = float(input("Enter first number  : "))
    num2 = float(input("Enter second number : "))
    print()
    calculator(num1, num2)
