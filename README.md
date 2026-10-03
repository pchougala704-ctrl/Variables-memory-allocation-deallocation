# Python Operators — Project Guide

This project demonstrates the core Python operators through 9 practical programs. Each file focuses on a specific use case and shows how different operators work together in real scenarios.

---

## Table of Contents

1. [Operators Overview](#operators-overview)
2. [Project Files](#project-files)
3. [Arithmetic Operators](#1-arithmetic-operators)
4. [Comparison Operators](#2-comparison-operators)
5. [Logical Operators](#3-logical-operators)
   - [and](#and-operator)
   - [or](#or-operator)
   - [not](#not-operator)
   - [is](#is-operator)
6. [Assignment Operators](#4-assignment-operators)
7. [Modulus Operator](#5-modulus-operator)
8. [File-by-File Breakdown](#file-by-file-breakdown)

---

## Operators Overview

| Operator Type | Symbols Used | Files Using It |
|---|---|---|
| Arithmetic | `+` `-` `*` `/` `//` `%` | `calculator.py`, `arithmetic_operations.py`, `discount_calculator.py` |
| Comparison | `==` `!=` `>=` `<=` `>` `<` | All files |
| Logical | `and` `or` `not` `is` | `eligibility_checker.py`, `placement_eligibility.py`, `user_login.py`, `access_control.py` |
| Assignment | `=` | All files |
| Modulus | `%` | `number_checker.py`, `calculator.py`, `arithmetic_operations.py` |

---

## Project Files

| File | Description |
|---|---|
| `calculator.py` | Basic arithmetic using all math operators |
| `arithmetic_operations.py` | User-selected operator applied to two numbers |
| `number_checker.py` | Even/odd and divisibility checks using `%` |
| `student_result1.py` | Grade classification using comparison operators |
| `discount_calculator.py` | Discount slabs using `>=` and arithmetic |
| `eligibility_checker.py` | Multi-condition check using `and` / `==` |
| `user_login.py` | Login validation using `==` and `and` |
| `access_control.py` | Access rules using `and`, `or` operators |
| `placement_eligibility.py` | Placement check combining comparison + logical operators |

---

## 1. Arithmetic Operators

Arithmetic operators perform mathematical calculations between two numbers.

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.333...` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus (Remainder) | `10 % 3` | `1` |

**Used in:** `calculator.py`, `arithmetic_operations.py`, `discount_calculator.py`

```python
# calculator.py
addition       = a + b
subtraction    = a - b
multiplication = a * b
division       = a / b
floor_division = a // b
remainder      = a % b
```

```python
# discount_calculator.py
discount_amount = (discount_rate / 100) * amount
final_amount    = amount - discount_amount
```

---

## 2. Comparison Operators

Comparison operators compare two values and return `True` or `False`.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `3 <= 5` | `True` |

**Used in:** `student_result1.py`, `discount_calculator.py`, `eligibility_checker.py`, `placement_eligibility.py`

```python
# student_result1.py
if marks >= 75:
    return "Distinction"
elif marks >= 35:
    return "Passed"
else:
    return "Fail"
```

```python
# discount_calculator.py
if amount >= 5000:
    discount_rate = 20
elif amount >= 3000:
    discount_rate = 10
else:
    discount_rate = 5
```

---

## 3. Logical Operators

Logical operators combine multiple conditions into a single expression and always return `True` or `False`.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `and` | Both conditions must be True | `True and False` | `False` |
| `or` | At least one condition must be True | `True or False` | `True` |
| `not` | Inverts the boolean value | `not True` | `False` |
| `is` | Checks identity (same object in memory) | `x is None` | `True` / `False` |

**Used in:** `user_login.py`, `eligibility_checker.py`, `access_control.py`, `placement_eligibility.py`

---

### `and` Operator

The `and` operator returns `True` only when **all** conditions are `True`. If any one condition is `False`, the whole expression is `False`.

**Truth Table:**

| Condition A | Condition B | A `and` B |
|---|---|---|
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

**Real-world meaning:** "This AND that both must pass."

**Examples from this project:**

```python
# user_login.py — username AND password both must be correct
if username == "Admin" and password == "python123":
    return "Valid User"
else:
    return "Invalid User"
```

```python
# eligibility_checker.py — all three conditions must be True together
if marks >= 60 and attendance >= 75 and backlog == False:
    return "Eligible"
else:
    return "Not Eligible"
```

```python
# placement_eligibility.py — marks AND attendance AND no backlog
if marks >= 60 and attendance >= 75 and has_backlog == False:
    eligible = "Yes"
```

---

### `or` Operator

The `or` operator returns `True` when **at least one** condition is `True`. It only returns `False` when all conditions are `False`.

**Truth Table:**

| Condition A | Condition B | A `or` B |
|---|---|---|
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |

**Real-world meaning:** "This OR that — either one is enough."

**Example from this project:**

```python
# access_control.py — employee gets in OR adult with valid ID gets in
if (age >= 18 and has_id) or is_employee:
    return "Access Granted"
else:
    return "Access Denied"
```

Here:
- An adult (`age >= 18`) with a valid ID (`has_id = True`) gets access.
- **OR** an employee (`is_employee = True`) gets access regardless of age/ID.
- Both paths lead to "Access Granted".

---

### `not` Operator

The `not` operator **flips** a boolean value. `True` becomes `False` and `False` becomes `True`.

**Truth Table:**

| Condition | `not` Condition |
|---|---|
| `True` | `False` |
| `False` | `True` |

**Real-world meaning:** "The opposite of this condition."

**Examples from this project:**

```python
# eligibility_checker.py — backlog must NOT be present
if marks >= 60 and attendance >= 75 and backlog == False:
    return "Eligible"

# Same logic can be written with 'not':
if marks >= 60 and attendance >= 75 and not backlog:
    return "Eligible"
```

```python
# access_control.py — has_id used as boolean (not False means has_id is True)
if (age >= 18 and has_id) or is_employee:
    return "Access Granted"

# Denying explicitly with 'not':
if not has_id:
    print("ID required for entry")
```

---

### `is` Operator

The `is` operator checks whether two variables point to the **exact same object** in memory — not just equal values, but the same identity. It is most commonly used to compare against `None`, `True`, or `False`.

| Expression | Meaning |
|---|---|
| `x is None` | x has no value assigned |
| `x is True` | x is exactly the boolean True |
| `x is False` | x is exactly the boolean False |
| `x is not None` | x has some value |

> **Note:** Use `==` to compare values (e.g., `5 == 5`). Use `is` to compare identity (e.g., `x is None`).

**Examples from this project:**

```python
# eligibility_checker.py — comparing backlog directly to False
if marks >= 60 and attendance >= 75 and backlog == False:
    return "Eligible"

# Same check using 'is':
if marks >= 60 and attendance >= 75 and backlog is False:
    return "Eligible"
```

```python
# placement_eligibility.py — has_backlog identity check
if marks >= 60 and attendance >= 75 and has_backlog is False:
    eligible = "Yes"
```

```python
# Practical use — checking if a value was ever set
result = None
if result is None:
    print("No result yet")
```

**`is` vs `==` — key difference:**

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True  — same values
print(a is b)   # False — different objects in memory

c = a
print(a is c)   # True  — same object
```

---

## 4. Assignment Operators

Assignment operators store values into variables.

| Operator | Meaning | Example |
|---|---|---|
| `=` | Assign a value | `x = 10` |
| `+=` | Add and assign | `x += 5` → `x = x + 5` |
| `-=` | Subtract and assign | `x -= 5` → `x = x - 5` |
| `*=` | Multiply and assign | `x *= 2` → `x = x * 2` |
| `/=` | Divide and assign | `x /= 2` → `x = x / 2` |

**Used across all files** to store computed results:

```python
# placement_eligibility.py
eligible = "Yes"
category = "Fresher"
```

```python
# discount_calculator.py
discount_amount = (discount_rate / 100) * amount
final_amount    = amount - discount_amount
```

---

## 5. Modulus Operator

The `%` operator returns the **remainder** after division. It is heavily used for divisibility checks.

| Expression | Result | Meaning |
|---|---|---|
| `10 % 2` | `0` | 10 is divisible by 2 (even) |
| `10 % 3` | `1` | 10 is not divisible by 3 |
| `10 % 5` | `0` | 10 is divisible by 5 |

**Used in:** `number_checker.py`, `calculator.py`, `arithmetic_operations.py`

```python
# number_checker.py
if n % 2 == 0:
    print(f"{n} is Even")
else:
    print(f"{n} is Odd")

if n % 3 == 0:
    print(f"{n} is divisible by 3")

if n % 5 == 0:
    print(f"{n} is divisible by 5")
```

---

## File-by-File Breakdown

### `calculator.py`
Demonstrates all six arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`) in a single function. Also uses a comparison (`b == 0`) to guard against division by zero.

### `arithmetic_operations.py`
Lets the user pick an operator at runtime. Uses `==` comparison inside `if/elif` blocks to match the chosen operator and applies it to two numbers.

### `number_checker.py`
Uses the `%` (modulus) operator to check if a number is even/odd and whether it is divisible by 3 or 5. Combines `%` with `==` (comparison).

### `student_result1.py`
Uses `>=` (comparison) to classify a student's marks into Distinction, Passed, or Fail grades.

### `discount_calculator.py`
Uses `>=` (comparison) to determine the discount slab, then arithmetic operators `/`, `*`, and `-` to compute the final payable amount.

### `eligibility_checker.py`
Uses `>=` (comparison) and `and` (logical) to check three conditions simultaneously: marks, attendance, and backlog status.

### `user_login.py`
Uses `==` (comparison) and `and` (logical) to validate a username and password together.

### `access_control.py`
Uses `>=` and `and` together inside an `or` expression — showing how logical operators can be combined to represent complex real-world rules.

### `placement_eligibility.py`
The most comprehensive file. Combines `>=`, `==`, `<=` (comparison) with `and` (logical) to determine both eligibility and candidate category (Fresher / Junior / Experienced).

---

## How to Run Any File

```bash
python calculator.py
python arithmetic_operations.py
python number_checker.py
python student_result1.py
python discount_calculator.py
python eligibility_checker.py
python user_login.py
python access_control.py
python placement_eligibility.py
```

> Requires Python 3.x
