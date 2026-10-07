---
aliases: [Programming Fundamentals - Day 13]
tags: [programming-fundamentals, term1, python]
course: "[[Programming Fundamentals]]"
---

# Programming Fundamentals — Day 13: Exceptions

**Today's focus:** handle errors gracefully with `try`/`except` instead of letting the program crash, and signal your own errors with `raise`.

## [[Exceptions and try-except|Exceptions]]
- Exceptions are errors that happen **while the program runs** ([[Common Python Errors]]: `NameError`, `TypeError`, `ValueError`, `ZeroDivisionError`, `IndexError`…)
- Unhandled → the program stops and prints a traceback
- Handled → you catch it and respond instead of crashing

### Without handling
```python
age = input("Enter your age: ")
years = 100 - int(age)
print(f"You will be 100 in {years} years.")
```
Entering `twenty` crashes with `ValueError: invalid literal for int() with base 10: 'twenty'` — `int()` can't convert a non-numeric string.

### try / except
```python
age = input("Enter your age: ")
try:
    years = 100 - int(age)
    print(f"You will be 100 in {years} years.")
except ValueError as e:
    print(f"Invalid input! Please enter a number. ({e})")
```
- Code that might fail goes in `try`
- If it raises that error, jump to `except` — no crash
- `as e` captures the error object so you can print its message

### Multiple exceptions
Stack several `except` clauses on one `try`; the matching one runs.
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
```
| Input | Result |
|---|---|
| `0` | `You can't divide by zero!` |
| `twenty` | `That's not a valid number!` |

### else and finally
```python
try:
    print("Trying something risky...")
except Exception:
    print("An error occurred.")
else:
    print("No errors occurred!")
finally:
    print("This always runs, error or not.")
```
- `else` — runs only if **no** exception happened
- `finally` — **always** runs
- Instructor's advice: avoid `else`/`finally` unless you have a specific reason; they can make code harder to read

### Raising exceptions
Signal an error from your own code with `raise`:
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")
```
Output: `Error: Cannot divide by zero!` — a bit more advanced, but useful for custom error handling in larger programs.

## Best Practices
- Keep the code inside `try` as small as possible
- Handle only the exceptions you expect
- Tell the user what went wrong
- Use specific exception types instead of a general `Exception`

## To Know
- `try` + `except` = catch and respond; `else` = success path; `finally` = always runs; `raise` = throw your own
- Order of `except` clauses doesn't matter for unrelated errors, but pick the **specific** type (`ValueError`) over `Exception`
- Traceback → read the last line first ([[Common Python Errors]])

## Homework
- 

## Reflection
*What was the most surprising insight today?*

Cheatsheet: [[List Methods Cheatsheet]]

Related today: [[Debugging in Python]], [[User Input and f-strings]]
