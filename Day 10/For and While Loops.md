---
aliases: [Programming Fundamentals - Day 10, Python Loops Lecture]
tags: [programming-fundamentals, term1, lecture-notes, python, loops, lists]
course: "[[Programming Fundamentals]]"
day: 10
---

# Programming Fundamentals — Day 10: For and While Loops

**Today's focus:** repeating work with `for` and `while`, looping over [[Python Lists]], and controlling a loop with `continue` and `break`. Concept page: [[Python Loops]] (the pseudocode side is [[Loops]]). Day 11 revisited the exercises with input validation using [[Exceptions]].

Lists hold the data; loops do something with **each item**. Like a grocery list: for each item on the list, get the item.

## for Loop Over a List
```python
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for day in days_of_week:
    print(f"{day} is a day of the week")
```
- `for <new variable> in <list>:` The new variable holds the current item on each pass
- The colon ends the line; the **indented** block under it is the loop body
- When the list runs out, the loop stops

## Tuples
A **tuple** is a list that can't be changed (no adding or removing). Use `( )` instead of `[ ]`. One item needs a trailing comma, `("a",)`, or the brackets look like maths.
```python
days_of_weekend = ("Saturday", "Sunday")
if day in days_of_weekend:      # `in` works on tuples and lists
    print(f"{day} is a weekend day")
else:
    print(f"{day} is a weekday")
```
Each extra level of indentation = one more level of nesting (the `if` inside the `for`).

## enumerate: Index and Item Together
```python
for index, day in enumerate(days_of_week):
    print(f"{day} is day number {index + 1} of the week")
```
The index starts at **0** (like list indexes), so add 1 for a human-friendly number.

## continue and break
| Keyword | Does |
|---|---|
| `continue` | Skip the rest of **this pass**, go to the next item |
| `break` | **Stop the whole loop** |

```python
for index, day in enumerate(days_of_week):
    if day == "Wednesday":
        break                      # stop the loop entirely
    if "u" in day:
        continue                   # skip Sunday, Tuesday...
    print(f"{day} is day number {index + 1}")
```
- Strings are lists of characters in Python, so `"u" in day` works
- `%` works in loops too: `if (index + 1) % 2 != 0: continue` skips the odd-numbered days
- Order matters: with the `break` check first, the loop ends the moment it reaches Wednesday (only Monday prints)

## range()
`range(n)` gives `0` to `n - 1`. To include `n`, use `range(n + 1)`.
```python
my_square = int(input("Enter a number to sum the squares: "))
total = 0
for i in range(my_square + 1):
    total = total + i * i
print(f"The sum of squares is {total}")          # 4 → 30
```

## Looping Over a String
```python
word = input("Enter a word: ").lower()
vowels = ["a", "e", "i", "o", "u"]
vowel_count = 0
for letter in word:
    if letter in vowels:
        vowel_count = vowel_count + 1
print(f"There are {vowel_count} vowels in {word}")   # onomatopoeia → 8
```

## while Loop
Repeats **while a condition is True**, so use it when you don't know how many passes you need.
```python
while True:                         # run until we break out
    user_input = input("Enter the age of a student or 'stop' to finish: ").lower()
    if user_input == "stop":        # sentinel value ends the loop
        break
    ages.append(int(user_input))
```
- `while True:` + `break` is the standard "ask until valid / until done" pattern
- A `while` loop must change something that eventually makes the condition false, or `break`, or it never ends ([[Common Python Errors]])

## Exercise Patterns
| Exercise | Pattern |
|---|---|
| Sum of squares 1 to n | `for i in range(n + 1)` and an accumulator |
| Vowel counter | `for letter in word`, `if letter in vowels`, counter |
| Average age until `stop` | `while True`, collect/accumulate, `break` on `stop`, then total ÷ count |
| ISP monthly bill | `match` on package A/B/C; overage = hours − allowance |

**Day 11 refinements** (input validation with [[Exceptions]]):
- Menu choice: `while True` → ask → `if choice in ('A','B','C'): break` else re-prompt
- Number input: wrap `int(input(...))` in `try/except ValueError` inside the loop, so bad input re-prompts instead of crashing
- Average age: catch `ZeroDivisionError` when `stop` is typed before any ages
- ISP bill: package A and B only charge extra **above** the allowance. Without an `if hours > allowance` check, fewer hours than the allowance gives a negative overage and a bill *below* the base price

## To Know
- [ ] `for item in list:` runs the indented block once per item
- [ ] `enumerate()` gives index and item; `range(n)` counts 0 to n−1
- [ ] `continue` skips to the next pass; `break` ends the loop
- [ ] Tuples are lists you can't change
- [ ] `while True:` + `break` for "repeat until valid / until done"
- [ ] Accumulator pattern: start a variable at 0, update it each pass, use it after the loop

## Homework
- Sum of squares, vowel counter, average age of students, ISP prices

## Reflection
*What was the most surprising insight today?*
