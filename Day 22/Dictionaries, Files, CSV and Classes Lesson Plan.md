---
aliases: [Programming Fundamentals - Day 22 Lesson Plan]
tags: [programming-fundamentals, term1, lesson-plan, python, dictionaries, file-io, csv, oop]
course: "[[Programming Fundamentals]]"
day: 22
---

# Lesson Plan: Dictionaries, Files, CSV and Classes

Quick version: [[Dictionaries, Files, CSV and Classes Summary]]. Source notes: [[Looping Through Dictionaries]] · [[Reading and Writing Files]] · [[Working with CSV Files]] · [[Classes and Objects]].

**Audience:** someone who knows variables, loops, functions, lists, and `try/except`.
**Length:** about 3.5 hours (the blocks stand alone, so split across sessions if needed).

## Learning Objectives
By the end, the learner can:
1. Loop a dictionary by keys, values, or pairs and tally data with a second dictionary
2. Read, write, and append text files safely with `with`, `pathlib`, and `try/except`
3. Read, filter, sort, write, and update CSV files with `DictReader` / `DictWriter`
4. Define a class with `__init__`, methods, and dunder methods, and use type hints
5. Combine all four in one small program

## Timeline
| Block | Topic | Time |
|---|---|---|
| 0 | Hook: the data lifecycle | 10 min |
| 1 | Looping dictionaries | 40 min |
| 2 | Text files | 40 min |
| 3 | CSV files | 45 min |
| 4 | Classes and objects | 50 min |
| 5 | Capstone: library app | 30 min |
| 6 | Wrap-up quiz | 10 min |

---

## Block 0 — Hook (10 min)
Ask: *"Your program tracks 500 books. Where does the data live while it runs? What happens when you close it?"*

Draw the pipeline and refer back to it all lesson:
```
dictionary  →  file / CSV  →  class + objects
(structure)    (persistence)   (modelling)
```
- Dictionaries: label data so you can find it
- Files: keep data after the program ends
- Classes: bundle data with the code that works on it

---

## Block 1 — Looping Dictionaries (40 min)

### Explain (10 min)
A dictionary loop is a list loop where you choose *what comes back*.

| Method | Gives you | Use when |
|---|---|---|
| `keys()` | each key | you need only names |
| `values()` | each value | you need only data |
| `items()` | each `(key, value)` pair | you need both |

```python
scores = {"Ava": 82, "Ben": 67, "Chen": 91}

for name in scores.keys():
    print(name)                      # Ava, Ben, Chen

total = 0
for score in scores.values():
    total += score                   # running total pattern
print(total / len(scores))           # 80.0

for name, score in scores.items():   # tuple unpacking: each pair split into two names
    print(f"{name} scored {score}")
```
**Point out:** `items()` hands back tuples, and `name, score` is multiple assignment that unpacks them.

### Example: tallying (10 min)
Goal: count how many times each word appears.
```python
text = "the cat saw the dog and the cat ran"
counts = {}

for word in text.split():
    if word not in counts:       # without this check: KeyError
        counts[word] = 0
    counts[word] += 1

print(counts)   # {'the': 3, 'cat': 2, 'saw': 1, 'dog': 1, 'and': 1, 'ran': 1}
```
Show the same thing in one line with `get()`:
```python
counts[word] = counts.get(word, 0) + 1
```
**Class discussion:** what if we skipped the `not in` check? Run it live and read the `KeyError`.

The lecture version used pre-built keys (`voting_results = {"apple": 0, ...}`) so `voting_results[vote] += 1` worked. That fails the moment a new fruit shows up, which is why the check or `get()` matters.

### Sorted output
```python
for word, n in sorted(counts.items()):                     # by key (alphabetical)
    print(f"{word}: {n}")

for word, n in sorted(counts.items(), key=lambda pair: pair[1], reverse=True):   # by count
    print(f"{word}: {n}")
```
(`lambda` is covered properly in Block 3. For now, "a tiny inline function that says what to sort on".)

### Nested structures
```python
cities = {
    "Edmonton": {"country": "Canada", "population": 1_100_000},
    "Tokyo":    {"country": "Japan",  "population": 14_000_000},
}

for city, info in cities.items():
    print(city)
    for key, value in info.items():
        print(f"  {key}: {value}")
```
Also show: a **list of dictionaries** (`people = [{"name": "Ava"}, ...]`) and a **dictionary with list values** (`{"Ava": [3, 7, 21]}`).

### Check for understanding
1. Which method would you use to find the highest score? *(values)*
2. What happens with `for k, v in d:` (no `.items()`)? *(it loops keys only, so unpacking each key into two names raises `ValueError`)*
3. Why can't you write `counts[word] += 1` on an empty dict? *(key doesn't exist yet)*

### Practice (15 min)
**Exercise 1.1:** Given `pets = {"Rex": "dog", "Mia": "cat", "Bo": "dog", "Kit": "cat", "Zed": "fish"}`, print how many of each animal there are, alphabetically.

**Exercise 1.2:** Using `cities` above, print the total population.

<details><summary>Answers</summary>

```python
# 1.1
tally = {}
for animal in pets.values():
    tally[animal] = tally.get(animal, 0) + 1
for animal, n in sorted(tally.items()):
    print(f"{animal}: {n}")          # cat: 2, dog: 2, fish: 1

# 1.2
total = 0
for info in cities.values():
    total += info["population"]
print(total)                          # 15100000
```
</details>

---

## Block 2 — Text Files (40 min)

### Explain (10 min)
Variables vanish when the program ends. Files persist.

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
```
- `with` closes the file automatically, even after an error
- `encoding="utf-8"` avoids surprises when the file moves between computers

| Mode | Does | Danger |
|---|---|---|
| `"r"` | read (default) | file must exist |
| `"w"` | write | **erases existing contents** |
| `"a"` | append to end | none, creates if missing |

| Read method | Returns |
|---|---|
| `read()` | one big string |
| `readline()` | next single line |
| `readlines()` | list of lines |

**Demo the trailing newline:** `print(lines)` shows `['hello\n', 'world\n']`. Clean up with `.strip()`:
```python
clean = [line.strip() for line in lines if line.strip()]   # also drops blank lines
```

### Writing
```python
def write_entry(path, entry: str) -> None:
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{entry}\n")      # write() adds no newline
```
**Live experiment:** switch `"a"` to `"w"`, run twice, watch the old entry vanish. Remove `\n`, watch entries glue together.

### Missing files
```python
def read_entries(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []        # or print a friendly message
```
Run it with a bad filename first without the `try` so learners see the traceback.

### The CWD trap
`open("journal.txt")` looks in the **current working directory**, which is wherever the terminal is, *not* where the script is saved.

Demo: run the script from its folder (works), then from the parent folder (breaks). Fix:
```python
from pathlib import Path

file_path = Path(__file__).parent / "journal.txt"
```
- `__file__` → this script's path · `.parent` → its folder · `/` → joins path pieces on any OS
- Useful extras: `.exists()`, `.is_file()`, `.name`, `.suffix`, `Path.cwd()`

### Journal app skeleton
```python
from pathlib import Path

def read_journal(path): ...      # try/except version above
def write_journal(path, entry): ...

def main() -> None:
    path = Path(__file__).parent / "journal.txt"
    while True:
        action = input("(r)ead, (w)rite, (q)uit: ").strip().lower()
        if action == "r":
            for entry in read_journal(path):
                print(entry)
        elif action == "w":
            write_journal(path, input("Entry: "))
        elif action == "q":
            break

if __name__ == "__main__":
    main()
```

### Check for understanding
1. You opened a log with `"w"` and lost it. What should you have used? *(`"a"`)*
2. Script works in VS Code but fails from the terminal. Likely cause? *(relative path / CWD)*

### Practice (15 min)
**Exercise 2.1:** Write `count_lines(path)` that returns the number of non-empty lines, or `-1` if the file doesn't exist.

**Exercise 2.2:** Write `numbered(path)` that prints `1. first line`, `2. second line`, … skipping blanks.

<details><summary>Answers</summary>

```python
def count_lines(path) -> int:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return len([line for line in f if line.strip()])
    except FileNotFoundError:
        return -1

def numbered(path) -> None:
    lines = [l.strip() for l in open(path, encoding="utf-8") if l.strip()]
    for i, line in enumerate(lines, start=1):
        print(f"{i}. {line}")
```
</details>

---

## Block 3 — CSV Files (45 min)

### Explain (5 min)
CSV = plain text, one row per line, values separated by commas. Every spreadsheet and database can import and export it.

Create `artists.csv` for the demos:
```
name,members,year_formed,monthly_listeners
Quiet Harbor,4,2009,12500000
Neon Parade,3,2015,9300000
The Tall Pines,5,1998,4100000
Static Bloom,3,2018,15200000
```

### Reading with `DictReader`
```python
import csv

def read_artists(path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))     # header row becomes the keys

artists = read_artists("artists.csv")
print(artists[0])   # {'name': 'Quiet Harbor', 'members': '4', 'year_formed': '2009', 'monthly_listeners': '12500000'}
```
**Highlight:** the numbers are in quotes. Everything from a CSV is a string.

### The string-sorting trap (10 min)
```python
sorted(["9300000", "12500000"])      # ['12500000', '9300000']  ← wrong, compares character by character
sorted([9300000, 12500000])          # [9300000, 12500000]      ← right
```
So convert before comparing, filtering, or sorting.

### Filter and sort
```python
big = [a for a in artists if int(a["monthly_listeners"]) >= 10_000_000]

by_listeners = sorted(artists, key=lambda a: int(a["monthly_listeners"]), reverse=True)
```
`lambda a: int(a["monthly_listeners"])` is a function with no name: *"given an artist, return the number to sort by."* Compare it to the `def` version so learners see they're equivalent:
```python
def listeners(a):
    return int(a["monthly_listeners"])

sorted(artists, key=listeners, reverse=True)
```
Keep a constant for numeric columns so one function can sort by any column:
```python
NUMERIC_COLUMNS = ["members", "year_formed", "monthly_listeners"]

def sort_by(artists, column, reverse=True, top_n=3):
    if column in NUMERIC_COLUMNS:
        key = lambda a: int(a[column])
    else:
        key = lambda a: a[column]
    return sorted(artists, key=key, reverse=reverse)[:top_n]
```

### Writing with `DictWriter`
```python
def write_artists(path, artists) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(artists[0].keys()))
        writer.writeheader()
        for artist in artists:
            writer.writerow(artist)
```
- `newline=""` prevents blank lines between rows on Windows
- `writeheader()` writes the column names; `writerow()` writes one dict

### Updating: read → modify → write
You can't edit one row inside the file. Load everything, change the dicts, write all of it back.
```python
def add_listeners_per_member(path) -> None:
    artists = read_artists(path)
    for artist in artists:
        artist["listeners_per_member"] = round(
            int(artist["monthly_listeners"]) / int(artist["members"])
        )
    write_artists(path, artists)       # a new key on every row = a new column
```
Warn: this overwrites the original. Write to a copy first while testing.

### Check for understanding
1. Why does `artist["members"] + 1` crash? *(string + int)*
2. What does `reverse=True` do with a lambda key? *(highest first)*
3. Why `newline=""`? *(avoid blank lines on Windows)*

### Practice (20 min)
**Exercise 3.1:** `filter_by_members(artists, exact_count)` returning matching artists.

**Exercise 3.2:** Export the 3-member bands to `three_member_bands.csv`.

**Exercise 3.3:** `oldest_artists(artists, top_n=3)` using `sort_by` with `reverse=False`.

<details><summary>Answers</summary>

```python
def filter_by_members(artists, exact_count):
    return [a for a in artists if int(a["members"]) == exact_count]

write_artists("three_member_bands.csv", filter_by_members(artists, 3))
# Neon Parade, Static Bloom

def oldest_artists(artists, top_n=3):
    return sort_by(artists, "year_formed", reverse=False, top_n=top_n)
# The Tall Pines (1998), Quiet Harbor (2009), Neon Parade (2015)
```
</details>

---

## Block 4 — Classes and Objects (50 min)

### Why (5 min)
Dictionaries hold data; functions live somewhere else. A class bundles both so the data and its behaviour travel together. Benefits: modularity, reuse, encapsulation.

**Analogy:** class = cookie cutter, object = the cookie. One cutter, many cookies, each with its own icing.

### Type hints first (5 min)
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def shout(name: str) -> None:       # None = returns nothing
    print(name.upper())
```
Hints are documentation. Python won't stop you from passing the wrong type, but editors and teammates will catch it.

### Build a class step by step (20 min)

**Step 1: attributes**
```python
class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

my_car = Car("Toyota", "Corolla", 2020)
second = Car("Honda", "Civic", 2021)
print(my_car.make)       # Toyota
print(second.year)       # 2021
```
Teach these four points, in order:
1. `class Car:` is PascalCase
2. `__init__` runs automatically when you call `Car(...)`
3. `self` = *the object being built*. It's always first and you never pass it
4. `self.make = make` stores the argument on that specific object

**Step 2: methods**
```python
    def honk(self) -> None:
        print(f"{self.make} {self.model} says beep beep!")

Car("Honda", "Civic", 2021).honk()
```

**Step 3: `__str__` vs `__repr__`**
```python
    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model}"       # for users

    def __repr__(self) -> str:
        return f"Car(make={self.make!r}, model={self.model!r}, year={self.year})"   # for developers
```
```python
print(my_car)        # 2020 Toyota Corolla
print(repr(my_car))  # Car(make='Toyota', model='Corolla', year=2020)
```
Demo what `print(my_car)` shows *without* `__str__`: `<__main__.Car object at 0x...>`. Rule of thumb: define both.

**Step 4: comparison**
```python
    def __eq__(self, other: "Car") -> bool:
        return self.make == other.make and self.model == other.model

    def __lt__(self, other: "Car") -> bool:
        return self.year < other.year
```
- Without `__eq__`, `==` asks "same object in memory?", so two identical-looking cars are `False`
- You decide what "equal" and "less than" mean
- Once `__lt__` exists, `sorted(cars)` just works
- `"Car"` in quotes is a **forward reference** (the class isn't finished being defined yet)

### Objects that hold objects (10 min)
```python
class Garage:
    def __init__(self) -> None:
        self.cars: list[Car] = []

    def add_car(self, car: Car) -> None:
        self.cars.append(car)

    def find_car(self, model: str) -> Car | None:
        for car in self.cars:
            if car.model == model:
                return car
        return None
```
`Car | None` means *"a Car, or nothing"*. The caller **must** check:
```python
garage = Garage()
garage.add_car(Car("Honda", "Civic", 2021))

result = garage.find_car("Civic")
if result is None:
    print("Not found")
else:
    print(f"Found: {result}")
```
Show the crash: `garage.find_car("Pinto").make` → `AttributeError: 'NoneType' object has no attribute 'make'`.

### Check for understanding
1. Class or object: `Car`, `my_car`, `Garage()`? *(class, object, object)*
2. Why does calling `my_car.honk()` work when `honk` takes `self`? *(Python passes it)*
3. Which method does `print()` use? *(`__str__`, falling back to `__repr__`)*
4. What does `Book | None` force the caller to do? *(check `is None`)*

### Practice (10 min)
**Exercise 4.1:** Write a `Pet` class with `name`, `species`, `age`; `__str__` returning `"Rex the dog (3)"`; `__lt__` comparing age.

**Exercise 4.2:** Add a `Shelter` class with `pets`, `add_pet`, `oldest_pet() -> Pet | None`.

<details><summary>Answers</summary>

```python
class Pet:
    def __init__(self, name: str, species: str, age: int) -> None:
        self.name = name
        self.species = species
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} the {self.species} ({self.age})"

    def __lt__(self, other: "Pet") -> bool:
        return self.age < other.age

class Shelter:
    def __init__(self) -> None:
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def oldest_pet(self) -> Pet | None:
        if not self.pets:
            return None
        return max(self.pets)       # works because __lt__ is defined
```
</details>

---

## Block 5 — Capstone: Library App (30 min)
Everything in one program: **CSV → objects → dictionary tally → sorted CSV out**.

**Folder layout**
```
library_app.py
books.csv
library_tools/
    __init__.py      # empty, marks the folder as a package
    book.py
    library.py
```

**`books.csv`**
```
title,author,pages,price
Mistborn,Brandon Sanderson,541,12.99
Elantris,Brandon Sanderson,496,11.50
The Hobbit,J.R.R. Tolkien,310,9.99
The Fellowship of the Ring,J.R.R. Tolkien,423,14.25
Dune,Frank Herbert,612,13.75
```

**`library_tools/book.py`**
```python
class Book:
    def __init__(self, title: str, author: str, pages: int, price: float) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages}, price={self.price})"

    def __eq__(self, other: "Book") -> bool:
        return self.title == other.title

    def __lt__(self, other: "Book") -> bool:
        return self.price < other.price

    def __gt__(self, other: "Book") -> bool:
        return self.price > other.price
```

**`library_tools/library.py`**
```python
import csv
from pathlib import Path
from library_tools.book import Book      # imported because it's used in type hints


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def find_book(self, title: str) -> Book | None:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def load_from_csv(self, file_path: Path) -> None:
        with open(file_path, "r", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                self.add_book(Book(row["title"], row["author"],
                                   int(row["pages"]), float(row["price"])))

    def books_per_author(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for book in self.books:
            counts[book.author] = counts.get(book.author, 0) + 1
        return counts

    def save_to_csv(self, file_path: Path) -> None:
        fieldnames = ["title", "author", "pages", "price"]
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for book in sorted(self.books):          # uses Book.__lt__ (by price)
                writer.writerow({"title": book.title, "author": book.author,
                                 "pages": book.pages, "price": book.price})
```

**`library_app.py`**
```python
from pathlib import Path
from library_tools.library import Library


def main() -> None:
    library = Library("City Library")
    library.load_from_csv(Path(__file__).parent / "books.csv")

    for author, count in sorted(library.books_per_author().items()):
        print(f"{author}: {count} book(s)")

    result = library.find_book("dune")
    if result is None:
        print("Book not found")
    else:
        print(f"Found: {result}")

    library.save_to_csv(Path(__file__).parent / "books_by_price.csv")


if __name__ == "__main__":
    main()
```

**Expected output**
```
Brandon Sanderson: 2 book(s)
Frank Herbert: 1 book(s)
J.R.R. Tolkien: 2 book(s)
Found: Dune by Frank Herbert
```
`books_by_price.csv` is then written cheapest first (The Hobbit → The Fellowship of the Ring).

**Debrief: where did each idea show up?**
| Idea | Where |
|---|---|
| Dictionary tally | `books_per_author` |
| `items()` + `sorted()` | printing authors in `library_app.py` |
| `DictReader` + string → number conversion | `load_from_csv` |
| `DictWriter`, `newline=""` | `save_to_csv` |
| `pathlib` | `Path(__file__).parent / ...` |
| Class, `__init__`, `self` | `Book`, `Library` |
| `__str__`, `__repr__`, `__eq__`, `__lt__` | `Book` (`sorted(self.books)`) |
| `X \| None` + `is None` | `find_book` and its caller |

**Stretch goals**
- Handle `FileNotFoundError` in `load_from_csv`
- Add `remove_book(title)` returning `True`/`False`
- Add `total_value()` summing prices with `.values()`-style accumulation

---

## Block 6 — Wrap-up Quiz (10 min)
1. Which gives you key *and* value: `keys()`, `values()`, or `items()`? **`items()`**
2. You read a CSV and `row["price"] > 10` raises `TypeError`. Why? **Value is a string; use `float()`.**
3. Which mode keeps existing contents and adds to the end? **`"a"`**
4. Why use `Path(__file__).parent`? **So the path works from any working directory.**
5. What's the difference between `__str__` and `__repr__`? **User-friendly vs developer/unambiguous.**
6. What does `self` refer to? **The specific object the method is being called on.**
7. Method returns `Book | None`. What must the caller do before using it? **Check `is None`.**
8. To change one value in a CSV, what are the three steps? **Read all, modify, write all back.**

## Teaching Notes
- **Live-code the failures** (KeyError, FileNotFoundError, `'w'` wiping a file, CSV strings). Learners remember errors they watched happen.
- **Pacing:** Block 4 is the densest. If time is short, drop `__gt__`, `__repr__`, and Exercise 4.2, and keep `__init__`, methods, `__str__`, and `X | None`.
- **Common confusions:** `self` (say "the object itself" often), `items()` vs `values()`, why a CSV update rewrites the whole file.
- **Homework:** Crash Course 6-1, 6-2, 6-7 to 6-11; the Day 20 challenge (`oldest_artists`, `filter_by_members`, export); finish the Library stretch goals.
