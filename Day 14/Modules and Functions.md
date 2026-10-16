---
aliases: [Programming Fundamentals - Day 14]
tags: [programming-fundamentals, term1, lecture-notes, python, functions, modules]
course: "[[Programming Fundamentals]]"
day: 14
---

# Programming Fundamentals — Day 14: Modules and Functions

**Today's focus:** writing reusable functions — defining, parameters, return values, the main guard, default and keyword arguments, importing from other files. Concept page: [[Python Functions]]. Same idea as [[Introduction to Modular Thinking]], now in Python.

## What Is a Function?
A reusable block of code that performs one specific task. Functions organise code into logical sections so it's easier to read, maintain and debug.
- Analogy: a tool in a toolbox — each has a purpose, use it whenever you need it
- Every programming language has them; fundamental concept

## Defining and Calling
Use `def`, a name (any valid Python name), and parentheses. Call it by name with `()`.
```python
# function definition
def greet_user():
    print("Hello, welcome to the program!")

# function call
greet_user()
```
Analogy: a recipe — define the steps once, make the dish whenever you want.

## Parameters and Arguments
**Parameters** are the inputs listed in the definition; **arguments** are the values you pass when calling.
```python
def add_numbers(a, b):      # a and b are parameters
    return a + b

result = add_numbers(3, 7)  # 3 and 7 are arguments
print("Sum:", result)
```
Analogy: ingredients — change them to make different versions of the dish.

## Returning Values
`return` sends a value back to the caller. Variables made inside a function only exist in that function's scope, so return them to use outside.
```python
def get_favorite_color():
    color = input("What's your favorite color? ")
    return color

user_color = get_favorite_color()
print("You like", user_color)
```
Analogy: a machine that takes input and gives you output. See [[User Input and f-strings]].

## Organizing Code with Functions
Functions separate concerns and make code easier to test and reuse.
```python
def get_temperature():
    return float(input("Enter the temperature: "))

def is_hot(temp):
    return temp > 30

temp = get_temperature()
if is_hot(temp):
    print("It's a hot day!")
else:
    print("It's not too hot.")
```
Conditionals: [[Conditionals]].

## The Main Guard
Code under `if __name__ == "__main__":` runs only when the file is **executed directly** (`python example.py`), not when it's imported.
```python
def main():
    print("This code runs when the script is executed directly.")

if __name__ == "__main__":
    main()
```
Use this pattern so your code works both as a script and as an importable module.

## Default Parameter Values
Give a parameter a default to make it optional.
```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9  (3 squared — default used)
print(power(2, 3))   # 8  (2 cubed — default overridden)
```

## Keyword Arguments
Pass arguments by name for clarity; order doesn't matter between keyword arguments.
```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(animal="dog", name="Buddy")
describe_pet(name="Whiskers", animal="cat")
```
**Positional arguments must come before keyword arguments** when you mix them.

## Importing Functions from Other Files
Put functions in separate files (modules) and import them.
```python
# math_utils.py
def square(n):
    return n * n
```
```python
# another file
from math_utils import square

print(square(6))   # 36
```
Project structure and more on imports come later.

## To Know
- `def name(params):` defines, `name(args)` calls
- Parameters = in the definition; arguments = values passed in the call
- `return` hands a value back; local variables don't exist outside the function
- `if __name__ == "__main__":` runs code only when the file is run directly
- Defaults make a parameter optional (`exponent=2`); keyword arguments are passed by name, after any positional ones
- `from file import function` reuses functions across files

## Reflection
*What was the most surprising insight today?*
