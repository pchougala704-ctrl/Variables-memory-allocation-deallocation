# Python Functions — Complete Notes

---

## 1. Why Functions?

Without a function:

```python
print("pooja")
print("ritika")
print("reena")
```

With a function:

```python
def welcome(name):
    print("welcome:", name)

welcome("pooja")
welcome("ritika")
welcome("reena")
```

**What problem did the function solve?**

- Code reuse
- Less repetition
- Better organization
- Easier maintenance
- Easier testing

---

## 2. What Exactly is a Function?

A function is a **reusable block of code** that performs a specific task.

```python
def add(a, b):
    return a + b

add(2, 3)
```

---

## 3. Defining vs Calling a Function

**Defining** — this does NOT execute the function:

```python
def greet():
    print("hello")
```

**Calling** — now Python executes its body:

```python
greet()
```

---

## 4. Function Without Parameters

```python
def welcome():
    print("welcome to Nighan2 labs")

welcome()
```

> Use this to establish the simplest possible function.

---

## 5. Function With Parameters

```python
def welcome(name):
    print("welcome", name)

welcome("pooja")
```

- `name` is the **parameter**
- `"pooja"` is the **argument**

---

## 6. Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

---

## 7. Return — The Most Important Concept

**Using `print` inside:**

```python
def add(a, b):
    print(a + b)
```

**Using `return`:**

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

- `print` — displays something on screen
- `return` — sends a value back to the caller

---

## 8. What Happens After `return`?

```python
def test():
    return 10
    print("hello")   # this will NOT execute
```

> `return` exits the function immediately. Any code after it is unreachable.

---

## 9. Multiple Return Values

```python
def calculate(a, b):
    return a + b, a - b, a * b

x, y, z = calculate(10, 5)
print(x)   # 15
print(y)   # 5
print(z)   # 50
```

> Python is effectively returning a **tuple** of values.

---

## 10. Default Parameters ⭐

```python
def greet(name="pooja"):
    print("hello", name)

greet()          # uses default → "hello pooja"
greet("ritika")  # overrides default → "hello ritika"
```

**Why use default parameters?**
- Makes arguments optional
- Provides sensible fallback values
- Reduces the number of calls needed for common cases

---

## 11. Positional Arguments

```python
def student(name, age):
    print(name, age)

student("Pooja", 20)
```

> Arguments are matched by their **position**.

---

## 12. Keyword Arguments

```python
student(age=20, name="pooja")
```

> Order doesn't matter when using parameter names.

---

## 13. Positional and Keyword Arguments Together

```python
def student(name, age, course):
    print(name, age, course)

student("pooja", age=20, course="BCA")   # valid
```

**Invalid:**

```python
student(name="pooja", 21, course="BCA")  # SyntaxError
```

> A **positional argument cannot follow a keyword argument**.

---

## 14. `*args` — Variable Positional Arguments

```python
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(1, 2, 3, 4, 5))
```

> `*args` collects any number of positional arguments into a **tuple**.

---

## 15. `**kwargs` — Variable Keyword Arguments

```python
def student(**details):
    print(details)

student(name="pooja", age=20, course="BCA")
```

> `**kwargs` collects keyword arguments into a **dictionary**.

---

## 16. Combining All Argument Types

```python
def example(a, b=10, *args, **kwargs):
    pass
```

> Order must be: positional → default → `*args` → `**kwargs`

---

## 17. Scope — Local vs Global

**Local variable** (exists only inside the function):

```python
def test():
    x = 10
    print(x)

test()
```

**Global variable** (defined outside, readable inside):

```python
x = 100

def test():
    print(x)

test()
```

---

## 18. The `global` Keyword

```python
count = 0

def increment():
    global count
    count = 1

increment()
```

- `global` allows **assignment** to a global variable from inside a function
- Avoid global state unnecessarily
- Prefer **parameters and return values** when designing reusable functions

---

## 19. Local Scope — NameError Example

```python
def test():
    x = 10

test()
print(x)   # NameError: name 'x' is not defined
```

> `x` is local to `test()` — it doesn't exist outside it.

---

## 20. Functions Calling Other Functions

```python
def add(a, b):
    return a + b

def display():
    result = add(10, 20)
    print(result)

display()
```

> Functions can be composed together:
> `main()` → `calculate()` → `save()` → `display()`



---

## 21. Function Calling Flow

```python
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print(result)
```

**Flow explanation:**

1. `multiply(5, 4)` is called — Python jumps into the function body
2. `a = 5`, `b = 4` are assigned
3. `a * b` → `5 * 4` → `20` is computed
4. `return` sends `20` back to the caller
5. `result` stores `20`
6. `print(result)` prints `20`

---

## 22. Functions are Objects

```python
def greet():
    print("hello world")

x = greet
x()
```

> `x` now refers to the **function object** — it can be stored in a variable and called later.

---

## 23. Passing a Function to Another Function

```python
def square(x):
    return x * x

def process(function, value):
    return function(value)

print(process(square, 5))
```

> This introduces **Higher Order Functions** ⭐ — functions that accept other functions as arguments.

---

## 24. Lambda Functions

```python
square = lambda x: x * x
print(square(5))
```

> `lambda` is an **anonymous function expression**, commonly used for small operations.

**Example with `map`:**

```python
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)
```

---

## 25. Recursion

```python
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)
```

> A **recursive function** calls itself.
> Every recursion must have a **base case** (`n == 0` here) to stop.

---

## 26. Function Documentation

```python
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add.__doc__)
```

> This introduces **professional Python habits** — always document your functions with a docstring.

---

## 27. Type Hints

> For modern Python.

```python
def add(a: int, b: int) -> int:
    return a + b
```

> Type hints communicate **intended types** to developers and tools.
> Python generally does **not** enforce them automatically at runtime — they are for readability and tooling support.

---

## 28. A Practical Program — Smart Electricity Bill

```python
def calculate_bill(units):
    if units <= 100:
        amount = units * 2
    elif units <= 200:
        amount = 100 * 2 + (units - 100) * 4
    else:
        amount = 100 * 2 + 100 * 4 + (units - 200) * 6
    return amount + 100

units = int(input("enter units: "))
bill = calculate_bill(units)
print("bill", bill)
```

**Why did we create `calculate_bill` instead of writing everything in the main program?**

- Separation of responsibility
- Reusability
- Easier testing
- Readability
- Easier maintenance

---

## 29. Function Design

A good function generally has three parts: **input**, **processing**, and **output**.

> `calculate_bill` is a perfect example of this pattern.

---

## 30. Do Not Create Giant Functions

**Bad — one function doing everything:**

```python
def student_system():
    # 200 lines
    # input
    # validation
    # calculation
    # database
    # printing
    pass
```

**Better — one function, one responsibility:**

```python
def get_student():       ...
def calculate_student(): ...
def validate_student():  ...
def save_result():       ...
def display_result():    ...
```

> This introduces the **Single Responsibility Principle** — each function does one thing and does it well.
