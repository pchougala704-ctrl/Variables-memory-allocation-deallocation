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
