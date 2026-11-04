---
aliases: [Programming Fundamentals - Day 19]
tags: [programming-fundamentals, term1, lecture-notes, python, file-io, pathlib, exceptions]
course: "[[Programming Fundamentals]]"
day: 19
---

# Programming Fundamentals — Day 19: Reading and Writing Files

**Today's focus:** opening, reading and writing text files, handling a missing file, and building file paths that work from anywhere with `pathlib`. Uses [[Exceptions and try-except]] and [[Python Functions]]. Next: [[Working with CSV Files]].

## Opening Files with `with`
```python
with open("notes.txt", "r") as f:
    lines = f.readlines()
```
- `with` closes the file for you when the block ends, even if an error happens
- Always pass `encoding='utf-8'` for text files you care about

| Mode | Does |
|---|---|
| `'r'` | read (default); file must exist |
| `'w'` | write; **creates or overwrites** the whole file |
| `'a'` | append; adds to the end, creates if missing |

## Reading
| Method | Returns |
|---|---|
| `f.read()` | the whole file as one string |
| `f.readline()` | one line at a time |
| `f.readlines()` | list of all lines |

Each line keeps its trailing `\n`, so clean up with `.strip()`:
```python
return [line.strip() for line in lines if line.strip()]   # drops blank lines too
```

## Writing
```python
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write(f"{entry}\n")      # write() doesn't add a newline for you
```
`'w'` wipes the file first, so use `'a'` when you want to keep what's there.

## Missing Files
Opening a file that doesn't exist raises `FileNotFoundError` and the program crashes. Catch it:
```python
def read_journal(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            entries = file.readlines()
        return [e.strip() for e in entries if e.strip()]
    except FileNotFoundError:
        return ["Error: The file does not exist. Please check the file path."]
```

## Journal App Pattern
Small functions plus a `main()` menu loop:
- `read_journal(path)`: returns the entries (with the `try/except` above)
- `write_journal(path, entry)`: appends one entry
- `main()`: loop asking read / write / quit, `.strip().lower()` the answer, `break` on `q`
- `if __name__ == "__main__": main()` so it can also be imported (see [[Modules and Functions]])

## Paths and `pathlib`
A relative path like `'journal.txt'` is resolved from the **current working directory (CWD)**, i.e. where you ran the command, **not** where the script lives. Run the script from another folder and it can't find the file.

Fix: build the path from the script's own location.
```python
from pathlib import Path
file_path = Path(__file__).parent / "journal.txt"
```
- `__file__` is the path of the running script
- `.parent` is the folder it's in
- `/` joins path pieces (works on Windows and macOS/Linux)

Handy `Path` methods: `.exists()`, `.is_file()`, `.is_dir()`, `.name`, `.suffix`, and `Path.cwd()` for the CWD. `open()` accepts a `Path` as is. Use `file_path.name` when you only want the filename in a print.

## Best Practices
- Use `with` so files always close
- Handle `FileNotFoundError` instead of letting the program crash
- Use clear paths and check they exist when the program depends on them
- Use `pathlib` for paths

## To Know
- [ ] Modes: `r` read, `w` overwrite, `a` append
- [ ] `read()` vs `readline()` vs `readlines()`; `.strip()` removes the `\n`
- [ ] `write()` needs an explicit `\n`
- [ ] `try/except FileNotFoundError` around the open
- [ ] `Path(__file__).parent / "file.txt"` is relative to the script, not the CWD

## Homework
- Exercise 1: `file_reader.py` (`read_file` returns lines) and `file_summary.py` (imports it, asks for a filename, prints numbered non-empty lines and the total)
- Exercise 2: `file_writer.py` (`write_to_file` with `'w'`, `append_to_file` with `'a'`, each printing a success message) and `file_editor.py` (asks filename, write or append, how many lines)

## Reflection
*What was the most surprising insight today?*
