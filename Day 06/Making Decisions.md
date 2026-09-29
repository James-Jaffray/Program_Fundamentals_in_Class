---
aliases: [Programming Fundamentals - Day 06]
tags: [programming-fundamentals, term1, python]
course: "[[Programming Fundamentals]]"
---

# Programming Fundamentals — Day 6: Making Decisions

**Today's focus:** use `if` statements with comparison and logical operators to make programs respond to input.

## [[Conditionals]]
- `if` runs a block only when its condition is `True`; `else` handles everything else; `elif` adds extra conditions
- Comparisons (`==`, `!=`, `>`, `<`, `>=`, `<=`) produce a boolean
- **Python uses indentation** (not curly braces) to mark what belongs inside the `if`
- Use `==` to compare, not `=` (assignment)

```python
concert_name = input("What is the name of the concert tonight? ")

if concert_name == "taylor swift":
    print("you're in the right place")
else:
    print("this is not the concert you are looking for")
```

## Random Numbers
- `import random`, then `random.randint(0, 1)` gives a random integer in that range
- Used for the coin-flip and high-or-low games

## In-Class Exercises
Concert ticket check, `heads_or_tails.py`, `high_or_low.py`, `leap_year.py` (divisible by 4 but not 100, or divisible by 400), `month_name.py`, `package_selector.py`, `zodiac.py`, `rock_paper_scissors.py`, and `pokemon_catch_broken.py` (find and fix the bug).

## To Know
- Compare the user's input to the exact type — `input()` returns a string, so convert first when comparing numbers

## Homework
- Making Decisions exercises — Chapter 05 exercises 5.3–5.7

## Reflection
*What was the most surprising insight today?*
