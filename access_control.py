def check_access(age, has_id, is_employee):
    """
    Accepts age, has_id, and is_employee.
    Access is granted when:
      - age >= 18 AND has_id is True
      OR
      - is_employee is True
    Returns 'Access Granted' or 'Access Denied'.
    """
    if (age >= 18 and has_id) or is_employee:
        return "Access Granted"
    else:
        return "Access Denied"


# --- Example usage ---
if __name__ == "__main__":
    age         = int(input("Enter age               : "))
    has_id      = input("Has valid ID? (yes/no)  : ").strip().lower() == "yes"
    is_employee = input("Is employee? (yes/no)   : ").strip().lower() == "yes"

    result = check_access(age, has_id, is_employee)
    print(f"\n{result}")
