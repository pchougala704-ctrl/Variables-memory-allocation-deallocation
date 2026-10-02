def check_eligibility(marks, attendance, backlog):
    """
    Accepts student marks, attendance percentage, and backlog status.
    A student is eligible only when:
      - marks >= 60
      - attendance >= 75
      - backlog is False
    Returns 'Eligible' or 'Not Eligible'.
    """
    if marks >= 60 and attendance >= 75 and backlog == False:
        return "Eligible"
    else:
        return "Not Eligible"


# --- Example usage ---
if __name__ == "__main__":
    marks      = float(input("Enter marks           : "))
    attendance = float(input("Enter attendance (%)  : "))
    backlog    = input("Any backlog? (yes/no) : ").strip().lower() == "yes"

    result = check_eligibility(marks, attendance, backlog)
    print(f"\nStudent is: {result}")
