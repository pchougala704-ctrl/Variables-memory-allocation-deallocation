def check_result(marks):
    """
    Accepts a student's marks and returns:
      - 'Distinction' if marks >= 75
      - 'Passed'      if marks >= 35
      - 'Fail'        otherwise
    """
    if marks >= 75:
        return "Distinction"
    elif marks >= 35:
        return "Passed"
    else:
        return "Fail"


# --- Example usage ---
if __name__ == "__main__":
    marks = float(input("Enter student marks: "))
    result = check_result(marks)
    print(f"Result: {result}")
