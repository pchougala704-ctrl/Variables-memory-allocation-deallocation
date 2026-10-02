def calculate(a, operator, b):
    """
    Accepts two numbers and an operator.
    Supported operators: +, -, *, /, //, %
    Handles invalid operators and division by zero.
    """
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Error: Division by zero is not allowed"
        return a / b
    elif operator == "//":
        if b == 0:
            return "Error: Division by zero is not allowed"
        return a // b
    elif operator == "%":
        if b == 0:
            return "Error: Division by zero is not allowed"
        return a % b
    else:
        return f"Error: Invalid operator '{operator}'. Supported: +, -, *, /, //, %"


# --- Example usage ---
if __name__ == "__main__":
    a        = float(input("Enter first number  : "))
    operator = input("Enter operator (+, -, *, /, //, %): ").strip()
    b        = float(input("Enter second number : "))

    result = calculate(a, operator, b)
    print(f"\n{a} {operator} {b} = {result}")
