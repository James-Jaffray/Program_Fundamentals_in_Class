---
aliases: [Programming Fundamentals - Day 03]
tags: [programming-fundamentals, term1, python]
course: "[[Programming Fundamentals]]"
---

# Programming Fundamentals — Day 3: Beginning Programming

**Today's focus:** write small programs that take user input, convert types, do math, and print formatted output.

## [[User Input and f-strings]]
- `input("prompt")` always returns a **string** — convert it before doing math (see [[Data Types]])
- `float(...)` for decimals, `int(...)` for whole numbers
- f-strings mix variables into text: `print(f"{celsius}°C is {fahrenheit}°F")`
- Format specs control rounding: `{value:.3f}` = 3 decimal places, `{value:.2f}` = 2
- `\n` inside a string starts a new line

```python
celsius = float(input("Provide temp in celsius: "))
fahrenheit = (celsius * (9/5)) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")
```

## The Exercise Pattern
Every exercise follows **input → calculate → print** (the same idea as the [[IPO Model]]). Today's set:
- Celsius → Fahrenheit
- Silly sentence from a name, adjective, verb and place
- Rectangle width/height → area and perimeter (3 decimal places)
- Price × quantity plus GST
- Miles → kilometres (`1 mile = 1.609344 km`, 2 decimal places)
- Trip cost from distance, fuel consumption (l/100km) and price per litre

## To Know
- Use `# %%` cell markers in VS Code to run a section at a time

## Homework
- Finish `beginning_programming_exercises` (the six above)

## Reflection
*What was the most surprising insight today?*
