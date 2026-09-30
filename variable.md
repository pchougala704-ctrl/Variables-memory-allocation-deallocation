# Python Variables, Memory & Garbage Collection
### Date: 29-09-2026

---

## 1. What is a Variable in Python?

In Python, a variable is essentially a **name or reference bound to an object**.

When you write `x = 10`, Python does not create a box and put 10 inside it. Instead, it creates an integer object with the value 10 somewhere in memory, and the name `x` is bound to (points to) that object.

```
x  →  10 (object)
```

Python does not work like the simple "variable as a box containing a value" model seen in some other languages. The variable is just a label. The object exists independently in memory.

---

## 2. Everything in Python is an Object

This is an important concept, especially in interviews.

Every value you work with in Python — whether it is a number, text, a list, or anything else — is an **object** in memory.

```
x = 10          →   x points to an integer object
name = "pooja"  →   name points to a string object
marks = 85.5    →   marks points to a float object
numbers = [10, 20, 30]  →  numbers points to a list object
```

Every object in Python has three properties:

- **Identity** — the memory address where the object lives. You can see it using `id()`.
- **Type** — what kind of object it is (int, str, list, etc.). You can see it using `type()`.
- **Value** — the actual data stored in the object. You see it by printing the variable.

Think of it this way:
- `id()` → identity (where it lives in memory)
- `type()` → type (what kind of thing it is)
- the variable itself → value (what it contains)

---

## 3. Python Datatypes

Python has a rich set of built-in datatypes, organized into useful categories:

| Category | Types |
|----------|-------|
| Numeric | int, float, complex |
| Boolean | bool |
| Text | str |
| Sequence | list, tuple, range |
| Set | set, frozenset |
| Mapping | dict |
| Binary | bytes, bytearray, memoryview |
| Special | NoneType |

---

## 4. Numeric Types

Python has three numeric types:

- **int** — whole numbers, positive or negative, with no decimal point. Example: age = 25, count = -10.
- **float** — numbers with a decimal point. Example: price = 99.50, percentage = 85.75.
- **complex** — numbers with a real and imaginary part. Example: z = 3 + 4j.

---

## 5. Boolean

Boolean represents one of two values: True or False. It is a subtype of int in Python.

- `bool(0)` → False
- `bool(1)` → True
- `bool("")` → False (empty string is falsy)
- `bool("hello")` → True (non-empty string is truthy)

is_active = True and is_logged_in = False are examples of boolean variables.

---

## 6. String

A string is an **immutable sequence of characters**. Once created, its characters cannot be changed.

Because it is a sequence, you can access individual characters by their position (index). The first character is at index 0, the second at index 1, and so on.

name = "string" — here name[0] gives 's' and name[1] gives 't'.

---

## 7. List

A list is an ordered, mutable collection that can hold multiple items.

Properties:
- **Ordered** — items maintain the order in which they were added.
- **Mutable** — items can be added, removed, or changed after creation.
- **Allows duplicates** — the same value can appear more than once.
- **Can contain different types** — a single list can hold integers, strings, floats, booleans, and more together.

Example: data = [10, "python", 25.5, True]

---

## 8. Tuple

A tuple is an ordered, immutable collection.

Properties:
- **Ordered** — items maintain their position.
- **Immutable** — once created, it cannot be changed (no adding, removing, or modifying items).
- **Allows duplicates** — same value can appear more than once.

Note: Tuples use parentheses `()`, not curly braces. Example: points = (10, 20).

---

## 9. Set

A set is an unordered collection of unique elements.

Properties:
- **Unique elements** — duplicate values are automatically removed.
- **Mutable** — you can add or remove elements.
- **Not for positional indexing** — since sets are unordered, you cannot access elements by index like a list.

Example: numbers = {10, 20, 20, 30} — the duplicate 20 is kept only once, result is {10, 20, 30}.

---

## 10. Dictionary

A dictionary stores data in **key-value pairs**. Each key must be unique.

```
students = {
    "id": 101,
    "name": "pooja",
    "marks": 85
}
```

You access a value using its key, not a numeric index. Dictionaries are ordered (Python 3.7+) and mutable.

Note: Dictionary syntax uses `:` to separate key and value, not `=`.

---

## 11. None

`None` is a special value in Python that represents the **absence of a value**. It is the only value of the `NoneType` type.

Do not confuse `None` with:
- `0` — this is an integer with the value zero
- `False` — this is a boolean
- `""` — this is an empty string
- `[]` — this is an empty list

All of these are different objects with different meanings. None specifically means "no value" or "nothing here".

---

## 12. Mutable vs Immutable

**Immutable** — objects that cannot be changed after they are created.
Examples: int, float, bool, str, tuple, frozenset.

**Mutable** — objects that can be changed after they are created.
Examples: list, dict, set, bytearray.

This distinction is one of the most important concepts in Python because it affects how memory works and how variables behave when shared.

---

## 13. What Happens When You "Change" an Immutable Variable?

When you write `x = 10` and then `x = 20`, it looks like x changed from 10 to 20.

What actually happened:
- Before: `x → 10 (integer object)`
- After: `x → 20 (a different integer object)`

The integer object 10 was **not modified**. It still exists in memory. What changed is that `x` was **rebound** — it now points to a completely different object (20). The name moved, not the value.

---

## 14. Memory Sharing Between Variables (Immutable)

When you write:
```
a = 10
b = a
```

Both `a` and `b` point to the **same object** in memory. No copy is made.

```
a  →  10 (object)
b  ↗
```

Now if you write `a = 20`, Python creates a new integer object 20 and rebinds `a` to it. `b` is not affected — it still points to the original object 10.

```
a  →  20 (new object)
b  →  10 (original object, unchanged)
```

This is safe because integers are immutable — no one can secretly change the value of 10 through one variable and surprise the other.

---

## 15. Memory Sharing Between Variables (Mutable)

With mutable objects, sharing is more significant.

When you write:
```
a = [10, 20]
b = a
```

Both `a` and `b` point to the **same list object** in memory.

```
a  →  [10, 20] (list object)
b  ↗
```

Now if you do `b.append(30)`, you are modifying the actual list object. Since `a` and `b` both point to that same object, printing `a` will show `[10, 20, 30]`.

This is a common source of bugs. The variable did not copy the list — it copied the reference to the list.

---

## 16. == vs is

These are two different comparisons and are often confused.

- `==` checks whether two objects have the **same value**.
- `is` checks whether two variables point to the **same object in memory** (same identity, same `id()`).

Example:
- `a = [1, 2]` and `b = [1, 2]` are two separate list objects with the same values.
- `a == b` is True — same value.
- `a is b` is False — different objects in memory.

Use `==` when you care about value. Use `is` only when you want to check object identity (most commonly used with `None`, like `if x is None`).

---

## 17. Where is Memory Used?

At a conceptual level, a Python program uses memory to store all of its objects:

```
Program
  └── Objects
        ├── int objects
        ├── string objects
        ├── list objects
        ├── dict objects
        └── function objects
```

In CPython (the standard Python implementation), objects are managed in Python's own memory system. Python requests memory from the operating system and then allocates it to objects through its own internal allocator mechanisms.

The key principle is:
> Python names reference objects, and CPython manages object memory dynamically. The exact implementation details depend on the Python implementation being used.

---

## 18. Reference Counting in CPython

CPython primarily tracks object usage through **reference counting**.

Every object has an internal counter (`ob_refcnt`) that records how many names or references currently point to it.

When you do:
```
a = [1, 2, 3]
b = a
```

The list object has a reference count of 2 — both `a` and `b` point to it.

When you do `del b`, the reference count drops to 1 — only `a` still points to it.

When the count reaches 0, CPython knows no name in the program can reach that object, and it can reclaim the memory.

---

## 19. Garbage Collection

Garbage collection means **identifying objects that are no longer reachable** by any part of the program and reclaiming the memory they occupy.

Python has automatic memory management. You do not normally need to write `free()` or manually delete memory the way you would in languages like C or C++. Python handles this for you.

---

## 20. Reference Counting + Garbage Collector

Python uses both mechanisms together:

**Reference Counting:**
- Tracks how many names reference an object.
- Works immediately and continuously in CPython.
- When the count drops to 0, the object is freed right away.
- Handles the vast majority of memory cleanup.

**Garbage Collector (gc module):**
- Handles **cyclic garbage** — situations where reference counting alone cannot free memory.
- A cycle occurs when an object references itself, or when two or more objects reference each other in a loop, even though nothing outside the cycle can reach them.
- Python's cyclic garbage collector detects these isolated cycles and frees them.
- Runs periodically in the background.

---

## 21. del Does Not Necessarily Delete the Object

`del numbers` removes the **name** `numbers` from the namespace. It does not necessarily destroy the object immediately.

If another name still references the same object, the object remains alive and accessible through that other name.

Example:
```
numbers = [1, 2, 3]
b = numbers
del numbers
```

After `del numbers`, the name `numbers` is gone. But the list object still has a reference count of 1 because `b` still points to it. The object is not destroyed. `b` still works normally.

---

## 22. When Does an Object Become Garbage?

An object becomes **eligible for garbage collection** (eligible for memory reclamation) when no name or reference anywhere in the running program can reach it.

Example:
```
numbers = [1, 2, 3]
b = numbers
del numbers
del b
```

After both `del numbers` and `del b`, no name points to the list anymore. The reference count drops to 0. The object is now unreachable and eligible for memory reclamation.

The exact timing of when that memory is actually returned to the OS or reused is an implementation detail. In CPython, because of reference counting, it typically happens immediately when the count hits 0.

---

## 23. Full Mental Model: Variable → Object → Memory → Garbage Collector

```
VARIABLE
   ↓
   binds to
   ↓
OBJECT  (has Identity, Type, Value)
   ↓
   lives in
   ↓
MEMORY  (managed by CPython's allocator)
   ↓
   when no longer reachable (ref count = 0 or cyclic)
   ↓
GARBAGE COLLECTION  (memory reclaimed)
```

---

## Answer to the Final Question:
## "If Python has Garbage Collection, Why Doesn't `del numbers` Necessarily Destroy the Object Immediately?"

Because `del numbers` and "destroying the object" are two completely separate things.

`del numbers` only does one thing — it **removes the name `numbers` from the namespace**. That is all. It is a name operation, not a memory operation.

The object's fate is decided by its **reference count**, not by whether a particular name was deleted.

- If `numbers` was the only name pointing to that object → reference count drops to 0 → CPython frees the memory immediately (this is reference counting doing its job).
- If another name like `b` also points to the same object → reference count only drops by 1 but does not reach 0 → the object is still alive and reachable through `b` → no memory is freed.

Additionally, garbage collection (the cyclic GC) runs **periodically**, not on every `del` call. The cyclic GC is only needed for circular references. For normal objects, reference counting handles deallocation immediately and automatically.

So the reason `del numbers` does not necessarily destroy the object is:
1. `del` removes a name, not an object.
2. The object is only destroyed when its reference count reaches 0.
3. If other references exist, the count does not reach 0.
4. Even if the count does reach 0, that is reference counting at work — not the garbage collector.
5. The cyclic garbage collector is a separate, periodic mechanism for a specific edge case (cycles), not a general-purpose destructor.

---

*End of Notes — 29-09-2026*
