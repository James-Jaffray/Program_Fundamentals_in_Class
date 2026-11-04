---
aliases: [Programming Fundamentals - Day 17]
tags: [programming-fundamentals, term1, lecture-notes, python, dictionaries]
course: "[[Programming Fundamentals]]"
day: 17
---

# Programming Fundamentals — Day 17: Dictionary Basics

**Today's focus:** storing data as key-value pairs: creating a dictionary, reading and changing values, safe lookups with `get()` and `in`, and nesting. Follows [[Python Lists]]; next up is [[Looping Through Dictionaries]].

## What Is a Dictionary?
Data stored as **key-value pairs**. Look up the key, get the value, like a real dictionary (word → definition).
- Keys are **unique** (usually strings); values can be **any type**, including lists and other dictionaries
- Great for structured data: a contact, a product, a burger
- Other languages call it a "map" or "associative array"
- Access by **key**, not by index like a list

## Creating One
Curly braces, `key: value`, commas between pairs.
```python
student = {
    "name": "Alex",
    "age": 21,
    "major": "Physics",
    "grades": [88, 92, 79]    # a list as a value
}
```

## Accessing, Changing, Adding
Square brackets with the key.
```python
print(student["name"])                    # Alex
student["age"] = 22                       # update an existing key
student["email"] = "alex@example.com"     # new key → added
```
Assigning to a key that doesn't exist **adds** it. So a typo in the key on assignment silently creates a second key instead of changing the one you meant.

## Safe Lookups
Reading a missing key with `[]` raises a `KeyError` (see [[Exceptions and try-except]]). Two ways around it:

**`get()`** returns a default instead of crashing:
```python
middle = student.get("middle_name", "N/A")   # "N/A" because the key is missing
```

**`in`** checks for a key first:
```python
if "email" in student:
    print("Email is:", student["email"])
else:
    print("No email on file.")
```
`in` checks **keys**, not values.

## Looping (Quick Version)
A plain `for` loop walks the keys; use each key to get its value. Full coverage next class.
```python
for key in student:
    print(f"{key}: {student[key]}")
```

## Nested Dictionaries
A value can be another dictionary. Chain the brackets to dig in.
```python
inventory = {
    "apple":  {"price": 0.5, "stock": 30},
    "banana": {"price": 0.3, "stock": 50}
}
print(inventory["apple"]["price"])   # 0.5
```

## In-Class Examples
- **Birthday lookup**: dictionary of name → birthday, `input()` the name (`.lower()` so case doesn't matter), `in` check, print the date or a "don't have it" message
- **Burger**: dictionary with a number, strings, a boolean and a list of toppings; reassign values (`burger['patties'] = 2`) and print them with an f-string
- **Pizza prices**: two dictionaries with the same keys (`toppings` is True/False, `toppings_prices` is the cost). Loop the toppings, add the price of each `True` one with `.get()`, add the base price, then the tip multiplier, and print with `:.2f`

## To Know
- [ ] `{key: value, ...}`; keys unique, values anything
- [ ] `d[key]` reads, `d[key] = value` updates **or adds**
- [ ] `d[missing]` → `KeyError`; `d.get(key, default)` and `key in d` avoid it
- [ ] Nested: `d["outer"]["inner"]`
- [ ] Use a dictionary when you look things up by name; use a list when order/position matters

## Homework
- Dictionary exercises: `birthdays.py` and `pizza_prices.py`

## Reflection
*What was the most surprising insight today?*
