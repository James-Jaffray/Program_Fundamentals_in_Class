---
aliases: [List Methods Cheatsheet, Python List Methods]
tags: [programming-fundamentals, term1, python, cheatsheet]
course: "[[Programming Fundamentals]]"
---

# List Methods Cheatsheet

Quick reference for [[Python Lists]]. Most methods change the list **in place** and return `None` — don't write `colors = colors.sort()`.

Examples use `colors = ["red", "green", "blue"]`.

## Add
| Method | Does | Example → `colors` after |
|---|---|---|
| `.append(x)` | Add `x` to the end | `.append("black")` → `["red","green","blue","black"]` |
| `.insert(i, x)` | Add `x` at index `i`, shifting the rest right | `.insert(1, "white")` → `["red","white","green","blue"]` |
| `.extend(iterable)` | Add every item from another list | `.extend(["pink","gray"])` → `[..., "pink","gray"]` |

`append` adds **one** item (a list appended becomes a nested list); `extend` adds **each** item.

## Remove
| Method | Does | Notes |
|---|---|---|
| `.remove(x)` | Remove first item equal to `x` | `ValueError` if `x` isn't in the list |
| `.pop(i)` | Remove and **return** item at index `i` | `.pop()` takes the last; `IndexError` if out of range |
| `.clear()` | Remove everything | List becomes `[]` |
| `del colors[i]` | Remove by index (statement, not a method) | `del colors[1:3]` removes a slice |

## Find
| Method | Does | Notes |
|---|---|---|
| `.index(x)` | Index of first `x` | `ValueError` if missing |
| `.count(x)` | How many times `x` appears | Returns `0` if none |
| `x in colors` | `True`/`False` membership check | Check this before `.remove()` / `.index()` |

## Order
| Method | Does | Notes |
|---|---|---|
| `.sort()` | Sort in place, ascending | `.sort(reverse=True)` for descending |
| `.reverse()` | Flip order in place | Not a sort — just reverses |
| `sorted(colors)` | Returns a **new** sorted list | Original untouched |

## Copy
| Way | Does |
|---|---|
| `.copy()` or `colors[:]` | New list with the same items |
| `b = colors` | **Not a copy** — both names point at the same list |

## Built-in functions (not methods)
`len(colors)` · `min(colors)` · `max(colors)` · `sum(numbers)` — last valid index is `len(colors) - 1`.

## Gotchas
- In-place methods return `None`: `x = colors.append("a")` makes `x` `None`
- `.remove(x)` only removes the **first** match
- Mixed types can't be sorted (`TypeError`)
- Methods that raise errors can be wrapped in `try`/`except` — see [[Exceptions and try-except]]:
```python
try:
    colors.remove("purple")
except ValueError:
    print("purple isn't in the list")
```

Related: [[Common Python Errors]] (`IndexError`, `ValueError`), [[Programming Fundamentals - Day 13]]
