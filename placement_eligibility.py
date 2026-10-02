def placement_eligibility(age, marks, attendance, experience, has_backlog):
    """
    Determines placement eligibility and candidate category.

    Eligibility criteria:
      - marks >= 60
      - attendance >= 75
      - has_backlog is False

    Category based on experience (in years):
      - 0          --> Fresher
      - 1 to 2     --> Junior
      - more than 2 --> Experienced
    """
    # Check eligibility
    if marks >= 60 and attendance >= 75 and has_backlog == False:
        eligible = "Yes"
    else:
        eligible = "No"

    # Determine category
    if experience == 0:
        category = "Fresher"
    elif 1 <= experience <= 2:
        category = "Junior"
    else:
        category = "Experienced"

    # Display results
    print(f"Age                 : {age}")
    print(f"Marks               : {marks}")
    print(f"Attendance          : {attendance}%")
    print(f"Experience          : {experience} year(s)")
    print(f"Has Backlog         : {'Yes' if has_backlog else 'No'}")
    print("-" * 35)
    print(f"Placement Eligible  : {eligible}")
    print(f"Candidate Category  : {category}")


# --- Example usage ---
if __name__ == "__main__":
    age         = int(input("Enter age                        : "))
    marks       = float(input("Enter marks                      : "))
    attendance  = float(input("Enter attendance (%)             : "))
    experience  = int(input("Enter experience (years)         : "))
    has_backlog = input("Has backlog? (yes/no)            : ").strip().lower() == "yes"

    print()
    placement_eligibility(age, marks, attendance, experience, has_backlog)
