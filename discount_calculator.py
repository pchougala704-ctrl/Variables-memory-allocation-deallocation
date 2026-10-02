def calculate_discount(amount):
    """
    Accepts a purchase amount and applies discount based on slabs:
      - ₹5000 or more  : 20% discount
      - ₹3000 to ₹4999 : 10% discount
      - Below ₹3000    :  5% discount
    Returns discount amount and final payable amount.
    """
    if amount >= 5000:
        discount_rate = 20
    elif amount >= 3000:
        discount_rate = 10
    else:
        discount_rate = 5

    discount_amount  = (discount_rate / 100) * amount
    final_amount     = amount - discount_amount

    print(f"Purchase Amount  : ₹{amount:.2f}")
    print(f"Discount Rate    : {discount_rate}%")
    print(f"Discount Amount  : ₹{discount_amount:.2f}")
    print(f"Final Payable    : ₹{final_amount:.2f}")

    return discount_amount, final_amount


# --- Example usage ---
if __name__ == "__main__":
    amount = float(input("Enter purchase amount (₹): "))
    print()
    discount, final = calculate_discount(amount)
