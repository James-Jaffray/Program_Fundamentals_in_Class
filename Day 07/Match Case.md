---
aliases: [Programming Fundamentals - Day 07]
tags: [programming-fundamentals, term1, python]
course: "[[Programming Fundamentals]]"
---

# Programming Fundamentals — Day 7: Match Case

**Today's focus:** replace long `if`/`elif` chains with `match`/`case`, and keep practicing decisions.

## [[Match Case]]
- New in Python 3.10 — a more concise, readable alternative when many `if`/`elif` checks compare the **same value**
- Each `case` ends with `:` and its indented block runs when matched
- `case _:` is the default (runs if nothing else matches)
- Combine values in one case with `|` (e.g. `"A+" | "A" | "A-"`)
- Normalize input first — `.upper()` avoids case-sensitivity problems

```python
letter_grade = input("Enter your letter grade (A, B, C, D): ").upper()

match letter_grade:
    case "A":
        gpa = 4.0
    case "B":
        gpa = 3.3
    case _:
        print("could not determine numeric grade")
        gpa = 0.0

print(f"Your GPA is {gpa}")
```

## To Know
- Reuse the [[Conditionals]] exercises from Day 6 (coin flip, leap year, zodiac, rock-paper-scissors) and try rewriting suitable ones with `match`

## Homework
- Grade-to-GPA program (`grade_match_case.py`)

## Reflection
*What was the most surprising insight today?*
