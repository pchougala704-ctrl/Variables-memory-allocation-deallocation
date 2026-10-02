# Python Functions — Interview Questions & Answers

---

## 1. What is a function?

A function is a **reusable block of code** that is written once and can be executed as many times as needed. It is designed to perform a specific task. Once defined, you can call it anywhere in your program without rewriting the same logic.

---

## 2. Why do we use functions?

We use functions to:

- **Avoid repetition** — write the logic once, use it many times
- **Organize code** — break a large program into smaller, manageable pieces
- **Improve readability** — a well-named function makes code self-explanatory
- **Easier maintenance** — fix a bug in one place instead of many
- **Easier testing** — test each function independently

---

## 3. How do you define a function?

A function is defined using the `def` keyword, followed by the function name, parentheses, and a colon. The body is indented below.

```python
def greet():
    print("hello")
```

Defining a function does **not** execute it — it only tells Python what the function should do when called.

---

## 4. How do you call a function?

A function is called by writing its name followed by parentheses.

```python
greet()
```

At this point Python jumps into the function body and executes it.

---

## 5. What is a parameter?

A parameter is a **variable listed in the function definition**. It acts as a placeholder for the value that will be passed when the function is called.

```python
def welcome(name):   # name is the parameter
    print("welcome", name)
```

---

## 6. What is an argument?

An argument is the **actual value passed to the function** when it is called.

```python
welcome("pooja")   # "pooja" is the argument
```

---

## 7. Parameter vs Argument?

| | Definition | Example |
|---|---|---|
| **Parameter** | Variable in the function definition | `name` in `def welcome(name)` |
| **Argument** | Actual value passed during the call | `"pooja"` in `welcome("pooja")` |

> Simple rule — parameter is in the **definition**, argument is in the **call**.

---

## 8. What is the difference between print() and return?

| | `print()` | `return` |
|---|---|---|
| Purpose | Displays a value on screen | Sends a value back to the caller |
| Can be stored? | No | Yes |
| Ends function? | No | Yes |

```python
def add(a, b):
    print(a + b)     # shows result, but caller gets nothing back

def add(a, b):
    return a + b     # caller receives the result and can use it

result = add(2, 3)   # result = 5
```

---

## 9. What happens if a function doesn't have return?

If a function has no `return` statement, Python automatically returns `None`.

```python
def greet():
    print("hello")

x = greet()
print(x)    # None
```

> `None` means the function completed but returned no value.

---

## 10. Can a function return multiple values?

Yes. Python allows returning multiple values separated by commas. They are returned as a **tuple**.

```python
def calculate(a, b):
    return a + b, a - b, a * b

x, y, z = calculate(10, 5)
print(x)   # 15
print(y)   # 5
print(z)   # 50
```

---

## 11. What are default arguments?

Default arguments are values assigned to parameters in the function definition. If the caller does not pass a value for that parameter, the default is used.

```python
def greet(name="pooja"):
    print("hello", name)

greet()          # hello pooja  (default used)
greet("ritika")  # hello ritika (default overridden)
```

> Default parameters make arguments optional.

---

## 12. What are positional arguments?

Positional arguments are values passed to a function **in the same order** as the parameters are defined. Position determines which value goes to which parameter.

```python
def student(name, age):
    print(name, age)

student("pooja", 20)   # name="pooja", age=20
```

---

## 13. What are keyword arguments?

Keyword arguments are passed by explicitly naming the parameter. This means order does not matter.

```python
student(age=20, name="pooja")   # same result, different order
```

> Keyword arguments make function calls more readable and flexible.

---

## 14. What is `*args`?

`*args` allows a function to accept **any number of positional arguments**. All extra positional values are collected into a **tuple**.

```python
def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add(1, 2, 3, 4, 5))   # 15
```

> The `*` is the syntax — `args` is just a naming convention, you could use any name.

---

## 15. What is `**kwargs`?

`**kwargs` allows a function to accept **any number of keyword arguments**. All extra keyword values are collected into a **dictionary**.

```python
def student(**details):
    print(details)

student(name="pooja", age=20, course="BCA")
# {'name': 'pooja', 'age': 20, 'course': 'BCA'}
```

> The `**` is the syntax — `kwargs` stands for "keyword arguments" by convention.

---

## 16. What is local scope?

Local scope means a variable is created **inside a function** and only exists within that function. It cannot be accessed from outside.

```python
def test():
    x = 10    # local variable
    print(x)

test()
print(x)   # NameError — x does not exist here
```

---

## 17. What is global scope?

Global scope means a variable is created **outside all functions**, at the top level of the program. It can be read from anywhere, including inside functions.

```python
x = 100   # global variable

def test():
    print(x)   # can read it

test()
```

> To **modify** a global variable inside a function, you must use the `global` keyword.

---

## 18. What is recursion?

Recursion is when a **function calls itself**. Every recursive function must have a **base case** — a condition that stops the recursion, otherwise it runs forever.

```python
def countdown(n):
    if n == 0:       # base case — stops here
        return
    print(n)
    countdown(n - 1) # function calls itself

countdown(5)
```

> Without a base case, recursion causes a `RecursionError` (stack overflow).

---

## 19. What is a lambda function?

A lambda function is an **anonymous function** — a function without a name, written in a single line. It is used for small, simple operations.

```python
square = lambda x: x * x
print(square(5))   # 25
```

> Equivalent to:
> ```python
> def square(x):
>     return x * x
> ```

Lambda functions are commonly used with `map()`, `filter()`, and `sorted()`.

---

## 20. What does it mean that functions are first-class objects in Python?

In Python, functions are **first-class objects**, which means they can be:

- **Assigned to a variable**
```python
x = greet
x()
```

- **Passed as an argument to another function**
```python
def process(func, value):
    return func(value)

print(process(square, 5))
```

- **Returned from a function**
```python
def outer():
    def inner():
        print("hello")
    return inner
```

> This is the foundation of **Higher Order Functions** and concepts like decorators in Python.
