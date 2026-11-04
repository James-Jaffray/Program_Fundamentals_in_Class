---
aliases: [Programming Fundamentals - Day 21]
tags: [programming-fundamentals, term1, lecture-notes, python, oop, classes, type-hints, dunder-methods]
course: "[[Programming Fundamentals]]"
day: 21
---

# Programming Fundamentals — Day 21: Classes and Objects

**Today's focus:** defining classes, creating objects, methods, dunder methods (`__str__`, `__repr__`, `__eq__`, `__gt__`, `__lt__`), collections of objects, and type hints. Concept page: [[Object-Oriented Programming]]. Pulls together [[Python Functions]] and [[Python Packages and Imports]]. Full dunder list: [[python_dunder_methods]].

## Why OOP?
Objects bundle **data and the functions that work on it** to model real things.
- **Modularity**: break big problems into pieces
- **Reusability**: reuse a class across programs
- **Encapsulation**: keep data inside the object, expose only what's needed (weaker in Python than other languages)
- **Inheritance / polymorphism**: later; you'll often inherit from classes other people wrote

## Class vs Object
- **Class** = blueprint (the recipe, the car factory)
- **Object / instance** = one thing built from it (the cake, one specific car)

## Type Hints
From now on, annotate parameters and return types.
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def shout(name: str) -> None:       # None = returns nothing
    print(f"HEY {name.upper()}!")
```
- Hints are **documentation, not enforcement**: Python still runs if they're wrong, but editors warn and other developers trust them
- All methods get them, including dunders: `__init__` → `None`, `__str__` → `str`
- Lists: `list[Book]`; "a thing or nothing": `Book | None`

## Defining a Class
```python
class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year
```
- `class` + name in **PascalCase** (functions are `snake_case`)
- `__init__` is the **constructor**, called automatically when you create an object
- `self` is the object being built/used. Always the first parameter
- `self.make` etc. are **attributes** (the object's data)

## Creating and Using Objects
Call the class like a function, passing what `__init__` asks for. No `new` keyword in Python.
```python
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.make)          # dot notation → Toyota
second_car = Car("Honda", "Civic", 2021)
```
Names starting with `_` (like `self._make`) are **private by convention**: don't touch them from outside the class.

## Methods
Functions defined in the class. First parameter is always `self`, but you **don't pass it** when calling; Python does.
```python
class Car:
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def honk(self) -> None:
        print(f"{self.make} {self.model} says beep beep!")

Car("Honda", "Civic").honk()     # Honda Civic says beep beep!
```

## Dunder Methods
"Double underscore" methods that customize how objects behave.

| Method | Triggered by | Purpose |
|---|---|---|
| `__init__` | creating the object | set up attributes |
| `__str__` | `print(obj)`, `str(obj)` | readable text for **users** |
| `__repr__` | `repr(obj)`, the shell | unambiguous text for **developers**, ideally looks like the code that rebuilds it |
| `__eq__` | `a == b` | define what "equal" means |
| `__gt__` / `__lt__` | `a > b`, `a < b` | define ordering |

- Without `__str__`, `print(obj)` shows something like `<library_tools.book.Book object at 0x...>`. If only `__repr__` exists, `print` falls back to it. Best practice: define both.
- Without `__eq__`, `==` asks "same object in memory?", which is `False` for two separately created books even if their titles match
- You choose what equal/greater means: e.g. same **title** for equality, **price** for `>` / `<`
- Bonus: once `__lt__` exists, `sorted(books)` works
- A self-referencing hint goes in quotes (`other: "Book"`), a **forward reference**, because the class isn't finished yet

```python
class Book:
    def __init__(self, title: str, author: str, pages: int, price: float) -> None:
        ...
    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
    def __eq__(self, other: "Book") -> bool:
        return self.title == other.title
    def __gt__(self, other: "Book") -> bool:
        return self.price > other.price
    def __lt__(self, other: "Book") -> bool:
        return self.price < other.price
```

## Collections of Objects
Attributes can hold other objects. A `Garage` (or `Library`) owns a list of `Car`s (or `Book`s).
```python
class Garage:
    def __init__(self) -> None:
        self.cars = []                 # starts empty, created in __init__

    def add_car(self, car: Car) -> None:
        self.cars.append(car)

    def list_cars(self) -> None:
        for car in self.cars:
            print(car)                 # uses Car.__str__
```

## `X | None` Pattern
A search method returns the object **or nothing**.
```python
def find_book(self, title: str) -> Book | None:
    for book in self.books:
        if book.title == title:
            return book
    return None
```
The caller must check before using the result, or the program crashes on a miss:
```python
result = library.find_book("Mistborn")
if result is None:
    print("Book not found")
else:
    print(f"Found: {result}")
```

## Library App Structure
```
library_app.py            # main program, imports the classes
library_tools/
    __init__.py           # makes the folder a package (can be empty)
    book.py               # class Book
    library.py            # class Library (name, books list, add_book, list_books, find_book)
```
```python
from library_tools.book import Book
from library_tools.library import Library
```
A class used in a type hint has to be imported where it's referenced (`library.py` imports `Book`).

## To Know
- [ ] Class = blueprint, object = instance; call the class to create one
- [ ] `__init__(self, ...)` sets attributes; `self` is the current object and isn't passed by the caller
- [ ] Dot notation for attributes and methods; `_name` = private by convention
- [ ] `__str__` (users) vs `__repr__` (developers); `__eq__`, `__gt__`, `__lt__` define comparison
- [ ] Type hints: `param: type`, `-> type`, `-> None`, `list[Book]`, `Book | None`
- [ ] Always `if result is None` before using something that might not exist

## Homework
- Follow-along: build the `Book` / `Library` app

## Reflection
*What was the most surprising insight today?*
