---
aliases: [Programming Fundamentals - Day 08 Debugging]
tags: [programming-fundamentals, term1, python]
course: "[[Programming Fundamentals]]"
---

# Programming Fundamentals — Day 8: Debugging

**Today's focus:** step through code with the Python debugger (`pdb`).

## [[Debugging in Python|Debugger]] Commands

| Command | Action |
|---|---|
| `n` / `next` | Run the next line of code |
| `s` / `step` | Step into a function call |
| `c` / `continue` | Continue running until the next breakpoint or end |
| `l` / `list` | List the surrounding code lines |
| `p` / `print` | Print the value of a variable |
| `quit` | Exit the debugger |

## Inspecting Variables
While paused at a breakpoint, you can check the value of variables:
```
(Pdb) x
10
(Pdb) y
5
(Pdb) result
NameError: name 'result' is not defined
```
(`result` isn't defined yet at this point in the program, hence the error.)

You can also **change** variable values to test different scenarios:
```
(Pdb) x = 20
(Pdb) n
```

## Stepping Through Code
- `n` (next) — execute the next line
- `s` (step) — step into a function call
- `c` (continue) — run until the next breakpoint or end of the program

## Tips for Effective Debugging
> *(section was left blank in the raw notes — add from the lesson when you have it)*

Related today: [[Python Lists]]
