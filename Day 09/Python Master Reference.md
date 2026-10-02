---
aliases: [Programming Fundamentals - Master Reference]
tags: [programming-fundamentals, term1, python, cheat-sheet]
course: "[[Programming Fundamentals]]"
---

# Python Master Reference (Days 1–8)

One-page-ish lookup for everything so far, written for beginners. Each section links to the deeper concept note. Day-by-day notes are in [[Programming Fundamentals]].

**Contents:** [[#1. The Basics]] · [[#2. Data Types]] · [[#3. Input, Output & f-strings]] · [[#4. Operators]] · [[#5. Strings]] · [[#6. Making Decisions]] · [[#7. Match Case]] · [[#8. Lists]] · [[#9. Errors & Debugging]] · [[#10. Git]] · [[#11. Coming Up: Loops]]

---

## 1. The Basics

### Run a program
Save as `something.py`, then in a terminal: `python something.py`. In VS Code you can also use `# %%` on its own line to make a "cell" and run one section at a time.

### Comments
```python
# This is a comment — Python ignores it
price = 10  # comments can go after code too
```
Use them to explain *why*, not to repeat the code. Clean up scratch comments before you submit (see Day 1 code review).

### Variables — [[Variables]]
A variable is a **name that holds a value**. `=` means "store the right side in the name on the left" (it is *not* the math "equals").
```python
name = "Alice"
age = 21
age = age + 1      # reassign: age is now 22
```
- Python is **dynamically typed** — you don't declare a type, it just follows the value
- Names are case-sensitive (`Age` ≠ `age`), can't start with a number, can't contain spaces
- **Snake case** is the Python convention: `days_until_due`, not `daysUntilDue`
- Style rules live in **PEP 8** (the Python style guide)

### Reading code top-to-bottom
Python runs line by line, in order. A variable must be created *before* you use it (otherwise `NameError`).

---

## 2. Data Types — [[Data Types]]

| Type | What it is | Examples | Convert with |
|---|---|---|---|
| `str` | Text (always in quotes) | `"Alice"`, `'hi'`, `"42"` | `str(x)` |
| `int` | Whole number | `14`, `0`, `-5` | `int(x)` |
| `float` | Number with a decimal | `3.14`, `-2.5`, `0.0` | `float(x)` |
| `bool` | `True` or `False` (capital first letter) | `True`, `False` | `bool(x)` |
| `list` | Ordered collection of items | `[1, 2, 3]` | `list(x)` |

- Check a type with `type(x)` → `<class 'int'>`
- `"42"` (text) and `42` (number) are different things! `"42" + "1"` is `"421"`; `42 + 1` is `43`
- Converting can fail: `int("hello")` → `ValueError`; `int("3.5")` also fails (use `int(float("3.5"))`)
- `int(3.9)` gives `3` — it **chops off** the decimal, doesn't round. Use `round(3.9)` to round

---

## 3. Input, Output & f-strings — [[User Input and f-strings]]

### print
```python
print("Hello")
print("Total:", 25)        # commas add a space between items
print("Line 1\nLine 2")    # \n = new line
```

### input — always gives you a string
```python
name = input("What is your name? ")
age = int(input("How old are you? "))   # convert right away if you need a number
```

### f-strings — put variables inside text
Put an `f` before the quote and variables inside `{ }`:
```python
total = 12.5
print(f"{name} owes ${total:.2f}")   # Alice owes $12.50
```

| Format | Meaning | Example |
|---|---|---|
| `{x:.2f}` | 2 decimal places | `3.14159` → `3.14` |
| `{x:.3f}` | 3 decimal places | `3.14159` → `3.142` |
| `{x:,}` | thousands commas | `1234567` → `1,234,567` |

### The usual program shape — [[IPO Model]]
**Input → Process (calculate) → Output (print).** Almost every exercise so far follows it.

---

## 4. Operators

### Math — [[Data Types]]

| Op | Does | `a=10, b=3` gives |
|---|---|---|
| `+` | add | `13` |
| `-` | subtract | `7` |
| `*` | multiply | `30` |
| `/` | divide (**always** a float) | `3.3333…` |
| `//` | floor division (drop the remainder) | `3` |
| `%` | modulus (the remainder) | `1` |
| `**` | exponent | `1000` |

- **Order of operations** is normal math: `( )` first, then `**`, then `* / // %`, then `+ -`
- `%` is handy for "is it even?" (`n % 2 == 0`) and "is it divisible by?" (leap years)
- Shortcuts: `x += 1` means `x = x + 1` (also `-=`, `*=`, `/=`)
- **Overloaded operators:** the same symbol can do different things. `+` adds numbers but *joins* strings (`"a" + "b"` → `"ab"`); `*` repeats strings (`"ha" * 3` → `"hahaha"`)

### Comparison — result is always `True` or `False`

| Op | Meaning |
|---|---|
| `==` | equal to |
| `!=` | not equal to |
| `>` / `<` | greater / less than |
| `>=` / `<=` | greater-or-equal / less-or-equal |

⚠ `=` **stores** a value; `==` **compares**. Mixing them up is the #1 beginner bug.

### Logical (boolean) operators — [[Boolean Logic]]

| Op | True when… | Example |
|---|---|---|
| `and` | **both** sides are True | `age >= 18 and has_id` |
| `or` | **at least one** side is True | `day == "sat" or day == "sun"` |
| `not` | flips True ↔ False | `not has_ticket` |

Truth table:

| A | B | `A and B` | `A or B` |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

- `not x == "y"` is the same as `x != "y"`
- Each side of `and`/`or` must be a full comparison: `x == 1 or x == 2` ✅ — `x == 1 or 2` ❌ (always "true", a classic trap)
- `in` checks membership: `"a" in "banana"` → `True`; `3 in [1, 2, 3]` → `True`

---

## 5. Strings — [[Python Strings]]
A string is a sequence of characters, so a lot of list ideas work on it.
```python
word = "Python"
len(word)        # 6
word[0]          # 'P'   (index starts at 0)
word[-1]         # 'n'   (last character)
word[:3]         # 'Pyt' (slice: start inclusive, stop exclusive)
```

| Method | Does | Result for `"  Hello "` / `"Hello"` |
|---|---|---|
| `.upper()` | all caps | `"HELLO"` |
| `.lower()` | all lowercase | `"hello"` |
| `.strip()` | trim spaces at both ends | `"Hello"` |
| `.replace("l", "L")` | swap text | `"HeLLo"` |

- Strings can't be changed in place; methods **return a new string**: `name = name.strip()`
- Tip: normalize input before comparing — `answer = input("y/n? ").strip().lower()`
- Quotes: `"it's"` or `'say "hi"'` — mix them to include the other kind; `\n` new line, `\t` tab

---

## 6. Making Decisions — [[Conditionals]]

### Shape
```python
if condition:
    # runs when condition is True
elif other_condition:
    # runs when the first was False and this is True
else:
    # runs when nothing above was True
```
- `elif` and `else` are optional; you can have many `elif`s but only one `else` (always last)
- **Only the first block whose condition is True runs** — the rest are skipped. A duplicate condition lower down is dead code
- **Indentation = which code belongs to the `if`** (use 4 spaces). The colon `:` after the condition is required
- Wrong indentation → `IndentationError`

### Worked example (the concert check)
```python
concert_name = input("What is the name of the concert tonight? ")
has_ticket = input("Do you have a ticket? (y/n) ")

if has_ticket == "y":
    ticket_type = input("VIP or Standard? ")

if not has_ticket == "y":
    print("Sorry you need a ticket to get in")
elif concert_name == "taylor swift" and ticket_type == "VIP":
    print("have fun superstar!")
elif concert_name == "taylor swift" and ticket_type == "Standard":
    print("enjoy the show")
elif concert_name == "billie eilish":
    print("this concert is next door")
else:
    print("this is not the concert you are looking for")
```
Order matters: the "no ticket" check goes first so nothing else runs for those people.

### Patterns worth remembering
```python
# even / odd
if n % 2 == 0: ...

# in a range (chained comparison works in Python)
if 0 <= grade <= 100: ...

# leap year: divisible by 4, except centuries, unless divisible by 400
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): ...
```

### Nested ifs
An `if` inside another `if` (indent again). Use when the second question only makes sense after the first is answered (like asking ticket type only *after* "do you have a ticket?").

### Random numbers
```python
import random
flip = random.randint(0, 1)   # 0 or 1 (both ends included)
```
`import` goes at the top of the file. `randint(a, b)` includes both `a` and `b`.

### Compare like with like
`input()` is a string. `age = input(...)` then `age > 18` → `TypeError`. Convert first: `age = int(input(...))`.

---

## 7. Match Case — [[Match Case]]
Python 3.10+. Tidier than a long `if/elif` chain when every branch checks **the same value**.
```python
day = input("Enter a day: ").lower()

match day:
    case "monday":
        print("Start of the work week!")
    case "saturday" | "sunday":     # | means "or" inside a case
        print("It's the weekend!")
    case _:                          # _ = wildcard / default
        print("Just another day.")
```
- Always include `case _:` for unmatched values
- Normalize first (`.lower()` / `.upper()`) so `"Monday"` and `"monday"` match
- For ranges (`grade >= 90`) use `if/elif` — `match` is for specific values

---

## 8. Lists — [[Python Lists]]
An **array** in other languages. A list holds many items in one variable (usually all the same type).
```python
colors = ["red", "blue", "green", "yellow"]
```

| Task | Code | Result / note |
|---|---|---|
| Access | `colors[0]` | `"red"` — index starts at **0** |
| Last item | `colors[-1]` | `"yellow"` — negatives count from the end |
| Change | `colors[1] = "pink"` | replaces that item |
| Length | `len(colors)` | `4` |
| Slice | `colors[1:3]` | `["blue", "green"]` — start **inclusive**, stop **exclusive** |
| First 3 | `colors[:3]` | first three items |
| Last 2 | `colors[-2:]` | last two items |
| Add to end | `colors.append("black")` | |
| Insert at spot | `colors.insert(1, "white")` | |
| Remove by value | `colors.remove("red")` | |
| Remove by position | `colors.pop(0)` | returns the removed item; `.pop()` takes the last |
| Is it in there? | `"red" in colors` | `True` / `False` |
| Sort | `colors.sort()` | sorts in place |

### Index map (why "5th item" is index 4)
```
item:    'a'  'b'  'c'  'd'  'e'
index:    0    1    2    3    4
negative: -5   -4   -3   -2   -1
```

### Slicing gotchas
- `[:4]` gives the **first four** items (indexes 0–3). `[:5]` gives five!
- `[-3:]` gives the **last three**
- Slices never raise an error if they run past the end; plain indexing does

### IndexError
`fruits = ["apple", "banana"]` then `fruits[5]` → `IndexError: list index out of range`. The last valid index is always `len(list) - 1`.

---

## 9. Errors & Debugging — [[Debugging in Python]], [[Common Python Errors]]

### How to read an error
Read the **last line first** (error type + message), then look at the line number just above it. Python usually points at, or just after, the real problem.

### The usual suspects

| Error | Usually means | Fix |
|---|---|---|
| `SyntaxError` | Typo in the code's grammar — missing `:`, quote, bracket | Check the line shown and the one before it |
| `IndentationError` | Spaces are wrong (unexpected or missing indent) | Use 4 spaces consistently |
| `NameError` | Using a variable that doesn't exist (typo, or not created yet) | Check spelling and order |
| `TypeError` | Mixing types: `"5" + 3`, `"7" > 3` | Convert with `int()` / `float()` / `str()` |
| `ValueError` | Right type, impossible value: `int("hello")` | Validate or fix the input |
| `IndexError` | List index doesn't exist | Stay within `0` … `len(list) - 1` |
| `ZeroDivisionError` | Divided by 0 | Check the divisor first |

Logic bugs (no error, wrong answer): add temporary `print()` lines to see values, or use the debugger.

### The debugger (pdb)
Put `breakpoint()` where you want to pause, then run the file.

| Command | Action |
|---|---|
| `n` / `next` | Run the next line |
| `s` / `step` | Step into a function call |
| `c` / `continue` | Run until the next breakpoint or the end |
| `l` / `list` | Show surrounding code |
| `p x` / `print x` | Show the value of `x` (or just type `x`) |
| `x = 20` | Change a value to test a scenario |
| `quit` | Exit the debugger |

A `NameError` inside the debugger usually just means that line hasn't run yet.

---

## 10. Git — [[Git Basics]]
**Version control** records changes to files over time so you can go back, see who changed what and when, and work with others.

### First-time setup (once per computer)
```
git --version
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --global --list
```

### The everyday loop
```
git status                    # what changed?
git add .                     # stage everything (or: git add <file>)
git commit -m "Describe it"   # save a snapshot with a message
git log --graph               # view history
git diff                      # see what changed since the last commit
```
Think of it as: **edit → add (stage) → commit (save) → push (upload)**.

### Connect to GitHub
```
git init                                    # turn this folder into a repo
git remote add origin <remote-url>          # link to the GitHub repo
git remote -v                               # check the link
git push --set-upstream origin master       # first push (branch may be called main)
git push                                    # later pushes
```
- `git branch` lists/creates branches; `git remote` manages remote links
- `git clone <url>` copies an existing repo; `git pull` downloads new changes
- Write commit messages that say *what* changed ("Add leap year check"), not "stuff"

---

## 11. Coming Up: Loops
Not covered in Python yet (the Day 8 slides are titled "Arrays and Loops" but only get through lists). A quick preview, since lists and loops go together — see [[Loops]] for the concept.
```python
# for loop: do something for each item
for color in colors:
    print(color)

# for loop with a counter
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

# while loop: repeat while a condition is True
count = 0
while count < 3:
    print(count)
    count += 1
```
Same rules as `if`: colon at the end, indented block underneath.

---

## Quick Chooser

| I want to… | Use |
|---|---|
| Store a value | variable: `x = 5` |
| Get typed text | `input()` (then convert if it's a number) |
| Show something | `print()` / f-string |
| Do one thing or another | `if / else` |
| Pick from several ranges/conditions | `if / elif / else` |
| Pick from several exact values | `match / case` |
| Hold many items | list |
| Count items / get the size | `len()` |
| Do something many times | loop (coming up) |
| Find the bug | read the error → `print()` → debugger |
| Save my work history | `git add` → `commit` → `push` |

## Check Yourself
1. What does `input()` always return, and how do you turn it into a number?
2. What's the difference between `=` and `==`?
3. What is `17 // 5`? `17 % 5`? `17 / 5`?
4. In an `if / elif / elif / else` chain where two conditions are True, how many blocks run?
5. For `items = ["a","b","c","d"]`, what are `items[1]`, `items[-1]`, `items[:2]` and `items[1:3]`?
6. Which error do you get from `items[10]`? From `int("hi")`? From using an undefined variable?
7. Write a condition for "age is 13 to 19 inclusive".

<details>
<summary>Answers</summary>

1. A string; `int(...)` or `float(...)`. 2. `=` stores, `==` compares. 3. `3`, `2`, `3.4`. 4. One — the first True one. 5. `"b"`, `"d"`, `["a","b"]`, `["b","c"]`. 6. `IndexError`, `ValueError`, `NameError`. 7. `13 <= age <= 19` (or `age >= 13 and age <= 19`).
</details>
