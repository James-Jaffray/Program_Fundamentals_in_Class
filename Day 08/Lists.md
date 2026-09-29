---
aliases: [Programming Fundamentals - Day 08 Lists]
tags: [programming-fundamentals, term1, python]
course: "[[Programming Fundamentals]]"
---

# Programming Fundamentals — Day 8: Arrays & Lists

**Today's focus:** work with lists — modify, slice, measure, and avoid `IndexError`.

## [[Python Lists|Lists]]
Lists are a core data structure in Python (see also [[Data Types]]). You can create, access, modify, slice, and measure them.

### Modifying List Items
```python
numbers = [10, 20, 30]
numbers[1] = 25
print("Modified numbers:", numbers)
```
Replaces the element at index 1.

### Slicing Lists
Use `start:stop` inside brackets to get a sublist. The start index is **inclusive**, the stop is **exclusive**.
```python
letters = ['a', 'b', 'c', 'd', 'e']
print("First three letters:", letters[:3])  # first three letters
print("Last two letters:", letters[-2:])    # last two letters
```

### Length of a List
```python
tasks = ['email', 'meeting', 'code review']
print("Number of tasks:", len(tasks))
```

### Out-of-Range Index
Accessing an index that doesn't exist raises an `IndexError`.
```python
fruits = ['apple', 'banana']
print(fruits[5])  # IndexError — there is no element 5
```

## Takeaway
Practice with your own examples to get comfortable with list operations.

Related today: [[Debugging in Python]]

## To Know
- Indexes start at 0; slice stop is exclusive


## Homework
- `hobbies.py` exercise: build a list of 9 hobbies, then print its length, the 5th item, the first four items as a sub list, and the last three items

## Reflection
*What was the most surprising insight today?*
