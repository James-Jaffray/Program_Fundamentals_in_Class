---
aliases: [Programming Fundamentals - Day 15]
tags: [programming-fundamentals, term1, lecture-notes, python, functions, modules, exceptions, loops]
course: "[[Programming Fundamentals]]"
day: 15
---

# Programming Fundamentals — Day 15: Functions and Modules Practice

**Today's focus:** moving code into your own module and importing it, plus a loop + exceptions exercise (the pizza bill splitter). Builds on [[Modules and Functions]] (Day 14), [[For and While Loops]] (Day 10) and [[Exceptions]] (Day 13). Concept pages: [[Python Functions]], [[Python Loops]], [[Exceptions and try-except]].

## Moving a Function Into Its Own Module
Exercise: take the sum-of-squares code, put the maths in `squares_calculator.py`, and import it into `sum_of_squares.py`.

```python
# squares_calculator.py
def calculate_sum_of_squares(num):
    total = 0
    for number in range(num):
        total += (number + 1) ** 2      # range starts at 0, so add 1
    return total
```
```python
# sum_of_squares.py
from squares_calculator import calculate_sum_of_squares

try:
    my_square = int(input("Enter a positive whole number to sum the squares: "))
    if my_square < 1:
        print("Error: Enter a positive integer to square. Example: 3")
    else:
        total = calculate_sum_of_squares(my_square)
        print(f"The sum of squares is: {total}")
except ValueError:
    print("Error: Enter a positive integer to square. Example: 3")
```
Input 4 → 1 + 4 + 9 + 16 = **30**.

Two import styles:
| Style | Call it with | Use it when |
|---|---|---|
| `from squares_calculator import calculate_sum_of_squares` | `calculate_sum_of_squares(4)` | You only need a few functions |
| `import squares_calculator` | `squares_calculator.calculate_sum_of_squares(4)` | You use most of the module (prefix every call with the module name) |

- The module file must be in the same folder (or on the path) as the file importing it
- The module does the calculating and `return`s; the main file does the input, validation and printing. That's the same split as [[Modular Thinking]]
- Other exercises from the Day 14 handout used the same pattern: `guess_items_price(guess)` in `price_is_right_games.py` (random prices, returns "You win!" or "Sorry you lose!"), imported into a `while True` game loop where `n` quits

## Pizza Bill Splitter: Loop + Exceptions
Goal: get the bill total and the number of people, calculate each person's share, and keep asking until the input is valid.
```python
while True:
    try:
        bill_total = float(input("Please input bill total: "))
        num_of_people = int(input("Please enter number of people sharing the bill: "))
        individual_price = bill_total / num_of_people
        print(f"Each person pays ${individual_price:.2f}")
        break                                  # only reached when nothing failed
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Cannot divide by 0 people")
```
| Piece | Why |
|---|---|
| `while True` | Keep asking until we `break` |
| `float(...)` for money, `int(...)` for people | Money has cents; people are whole numbers |
| `except ValueError` | Text like `abc` in either prompt |
| `except ZeroDivisionError` | 0 people |
| `break` last inside `try` | A failure skips it, so the loop repeats |
| `:.2f` | Two decimal places |

Watch the f-string: a `$` before `{...}` is just a dollar sign, and `${num_of_people}` would print "$5" for a head count. Only put `$` in front of money.

## To Know
- [ ] Put reusable functions in a module (`.py` file) and import them
- [ ] `from module import function` vs `import module` (and the prefix)
- [ ] Modules return values; the main file handles input/output
- [ ] `while True` + `try` + `break` at the end of the `try` = ask again until valid
- [ ] Catch specific exceptions (`ValueError`, `ZeroDivisionError`), not a bare `except`

## Homework
- Modules and functions exercises (sum of squares, price is right, car price guessing game)

## Reflection
*What was the most surprising insight today?*
