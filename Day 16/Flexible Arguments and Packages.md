---
aliases: [Programming Fundamentals - Day 16]
tags: [programming-fundamentals, term1, lecture-notes, python, functions, packages, modules]
course: "[[Programming Fundamentals]]"
day: 16
---

# Programming Fundamentals — Day 16: Flexible Arguments and Packages

**Today's focus:** functions that accept any number of arguments (`*args`, `**kwargs`), unpacking lists and dicts into a call, and organizing code into packages you can run with `python -m`. Continues [[Functions and Modules Practice]] and [[Modules and Functions]]. Concept pages: [[Python Functions]], [[Python Packages and Imports]].

## Why Flexible Arguments?
A function can take no arguments, 2, 4, or any number. That makes it more reusable when you don't know in advance how much input you'll get.

### Positional vs keyword (recap)
```python
def describe_pet(animal, name):
    print(f"{name} is a {animal}.")

describe_pet("dog", "Buddy")             # positional: order matters
describe_pet(animal="cat", name="Milo")  # keyword: order doesn't matter
```

## *args: Any Number of Positional Arguments
```python
def print_numbers(*args):
    for n in args:
        print(n)

print_numbers(1, 2, 3)
print_numbers(10, 20)
print_numbers(5, 15, 25, 35)
```
`args` arrives as a **tuple**, so you loop over it ([[For and While Loops]]). The name `args` is convention; the `*` is what matters.

## **kwargs: Any Number of Keyword Arguments
```python
def print_settings(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_settings(theme="dark", font="Arial", size=12)
# theme: dark
# font: Arial
# size: 12
```
`kwargs` arrives as a **dictionary** of name → value.

## Both Together
```python
def order_summary(*items, **options):
    print("Items ordered:")
    for item in items:
        print("-", item)
    print("Options:")
    for key, value in options.items():
        print(f"{key}: {value}")

order_summary("burger", "fries", drink="cola", size="large")
```
Order in the definition: normal parameters, then `*args`, then `**kwargs`.

| Syntax | Collects | Becomes |
|---|---|---|
| `*args` | extra positional arguments | tuple |
| `**kwargs` | extra keyword arguments | dict |

## Argument Unpacking
Same symbols, opposite direction: in a **call**, `*` and `**` spread a collection into separate arguments.
```python
def show_info(name, age):
    print(f"{name} is {age} years old.")

person = ("Alice", 30)
show_info(*person)            # same as show_info("Alice", 30)

settings = {"name": "Bob", "age": 25}
show_info(**settings)         # same as show_info(name="Bob", age=25)
```
- `*` unpacks a list/tuple into positional arguments
- `**` unpacks a dict into keyword arguments; the **keys must match the parameter names**
- In a `def`, the star **collects**. In a call, the star **spreads**

## Packages: A Folder as One Unit
Once a project outgrows one file, group related code in a folder. A folder becomes a **package** when it contains an `__init__.py` (it can be empty).

```
pizza_shop/
├── __init__.py       # marks pizza_shop as a package
├── __main__.py       # entry point for python -m
└── utils/
    ├── __init__.py   # marks utils as a sub-package
    └── pizza.py      # contains make_pizza()
```
- Every nested folder needs its own `__init__.py`
- Imports mirror the folders: `from pizza_shop.utils.pizza import make_pizza` is package → sub-package → file → function

### __main__.py
The entry point Python looks for when you run the package.
```python
# pizza_shop/__main__.py
from pizza_shop.utils.pizza import make_pizza

if __name__ == "__main__":
    make_pizza("cheese", size=12, crust="thin")
```
`make_pizza` is a good place for `*args` and `**kwargs` (toppings and options).

### Running it
From the folder that **contains** `pizza_shop/`:
```
python -m pizza_shop
```
- Python treats it as a package and runs its `__main__.py`
- Running `python pizza_shop/__main__.py` directly often breaks the dotted imports, so use `-m`

## To Know
- [ ] `*args` collects extra positional arguments into a tuple; `**kwargs` collects keyword arguments into a dict
- [ ] Definition order: normal params, `*args`, `**kwargs`
- [ ] In a call, `*` and `**` unpack a tuple/list or dict
- [ ] Package = folder with `__init__.py`; each sub-folder needs one too
- [ ] `__main__.py` is what `python -m package_name` runs
- [ ] Dotted imports follow the folder structure

## Homework
- Follow-along examples from class (`demo.py`, the `pizza_shop` package)

## Reflection
*What was the most surprising insight today?*
