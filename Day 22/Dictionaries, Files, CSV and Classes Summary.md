---
aliases: [Programming Fundamentals - Day 22]
tags: [programming-fundamentals, term1, summary, python, dictionaries, file-io, csv, oop]
course: "[[Programming Fundamentals]]"
day: 22
---

# Programming Fundamentals — Days 18–22: Summary

**Big picture:** the last stretch takes data from *loose values* to *real programs*. Dictionaries organize it, files and CSVs make it last, and classes package data with the code that works on it. Teaching version: [[Dictionaries, Files, CSV and Classes Lesson Plan]].

```
dictionary  →  file / CSV  →  class + objects
(structure)    (persistence)   (modelling)
```

## Dictionaries ([[Looping Through Dictionaries]])
| Method | Gives you |
|---|---|
| `d.keys()` | each key (also the default when you loop `d`) |
| `d.values()` | each value |
| `d.items()` | each `(key, value)` pair, unpack with `for k, v in d.items():` |

- **Tally pattern:** `counts[x] += 1` (the key must already exist, or use `if x not in counts` / `get()` first)
- **Sorted output:** `sorted(d.items())` orders by key
- **Nesting:** list of dicts, dict with list values, dict of dicts (loop `.items()` twice)

## Text Files ([[Reading and Writing Files]])
- Always `with open(path, "r", encoding="utf-8") as f:` so the file closes itself
- Modes: `r` read, `w` **overwrite**, `a` append
- `read()` whole string · `readline()` one line · `readlines()` list; lines keep `\n`, so `.strip()`
- `write()` doesn't add `\n` for you
- Missing file → `FileNotFoundError`; wrap in `try/except` ([[Exceptions and try-except]])
- Relative paths resolve from the **CWD**, not the script. Use `Path(__file__).parent / "file.txt"`

## CSV ([[Working with CSV Files]])
- `csv.DictReader` → each row is a dict (header row = keys). **Every value is a string**
- `csv.DictWriter` → `writeheader()` then `writerow(dict)`; open with `newline=""`
- Filter with a list comprehension, sort with `sorted(data, key=lambda row: ...)`
- Convert numbers (`int()`, `float()`) before comparing or sorting, or `'9'` sorts after `'12'`
- Updating a file = **read → modify → write back** (no in-place edit)

## Classes and Objects ([[Classes and Objects]])
- **Class** = blueprint, **object** = one instance. Class names are `PascalCase`
- `__init__(self, ...)` runs on creation and sets attributes; `self` is passed automatically
- Methods are functions inside the class; call with dot notation `obj.method()`
- `_name` = private by convention
- Dunder methods: `__str__` (users), `__repr__` (developers), `__eq__`, `__lt__`, `__gt__` (once `__lt__` exists, `sorted()` works)
- Type hints (`name: str`, `-> None`, `list[Book]`, `Book | None`) document intent, they aren't enforced
- A class can hold a list of other objects (`Library` → `Book`s); search methods return `Book | None`, so check `is None` first
- Packages: `library_tools/__init__.py` + `book.py` + `library.py`, imported with `from library_tools.book import Book`

## Common Mistakes
| Mistake | Fix |
|---|---|
| `KeyError` when tallying a new key | check `in` first or use `.get(key, 0)` |
| Lost the file's old contents | you used `'w'`, use `'a'` to append |
| Entries run together on one line | add `\n` to `write()` |
| `FileNotFoundError` only from some folders | build the path from `__file__`, not the CWD |
| CSV numbers sort wrong or `TypeError` on math | they're strings, convert first |
| `print(obj)` shows `<... object at 0x...>` | define `__str__` |
| `AttributeError: 'NoneType'...` | `find_*` returned `None`, check `is None` before using |

## Related
[[Dictionary Basics]] · [[Python Functions]] · [[Python Packages and Imports]] · [[Object-Oriented Programming]] · [[Python Master Reference]]
