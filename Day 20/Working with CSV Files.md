---
aliases: [Programming Fundamentals - Day 20]
tags: [programming-fundamentals, term1, lecture-notes, python, file-io, csv, lambda]
course: "[[Programming Fundamentals]]"
day: 20
---

# Programming Fundamentals — Day 20: Working with CSV Files

**Today's focus:** reading, filtering, sorting, writing and updating CSV files with the `csv` module. Builds on [[Reading and Writing Files]] and [[Dictionary Basics]].

## What Is a CSV?
Comma-Separated Values: plain text, one row per line, tabular data. Easy to read and write, and supported by spreadsheets and databases, so it's the standard way to move data between programs.

## Reading: `DictReader`
```python
import csv

def read_artists(file_path):
    artists = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)      # header row becomes the keys
        for row in reader:
            artists.append(row)            # each row is a dictionary
    return artists
```
**Everything comes back as a string**, including numbers. Convert with `int()` / `float()` before doing math or numeric sorting.

`pprint` (`from pprint import pprint`) prints big lists of dictionaries in a readable layout.

## Filtering
A list comprehension with a condition:
```python
popular = [a for a in artists if int(a["monthly_listeners"]) >= 10_000_000]
```
Underscores in number literals (`10_000_000`) are just for readability.

## Sorting
`sorted()` takes a **key function** that says what to sort on.
- Gotcha: sorting numbers as strings goes character by character, so `'9300000'` lands *after* `'12500000'`. Convert numeric columns to `int` in the key.
- Keep the numeric column names in a constant: `NUMERIC_COLUMNS = ['members', 'year_formed', 'monthly_listeners']`

```python
def sort_artists_by(artists, column, reverse=True, top_n=5):
    if column in NUMERIC_COLUMNS:
        key = lambda artist: int(artist[column])
    else:
        key = lambda artist: artist[column]
    return sorted(artists, key=key, reverse=reverse)[:top_n]
```
**`lambda`**: a tiny anonymous function written inline, `lambda x: x["name"]`. Good for short throwaway key functions instead of a full `def`.

## Making It Interactive
List the columns with `enumerate`, let the user pick a number, subtract 1 to get the index, sort by that column:
```python
columns = list(artists[0].keys())
for index, column in enumerate(columns):
    print(f"{index + 1}. {column}")
choice = int(input("Column number: ")) - 1
```

## Writing: `DictWriter`
```python
def write_top_artists(file_path, artists):
    fieldnames = list(artists[0].keys())
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()                 # the column names row
        for artist in artists:
            writer.writerow(artist)
```
- Open with `newline=''` when writing CSVs (otherwise you can get blank lines on Windows)
- `writeheader()` writes the header, `writerow()` writes one dictionary

## Updating a CSV: Read → Modify → Write
You can't edit a row in place. Read everything, change the dictionaries, write it all back.
```python
def add_listeners_per_member(file_path):
    artists = read_artists(file_path)
    for artist in artists:
        artist["listeners_per_member"] = round(
            int(artist["monthly_listeners"]) / int(artist["members"])
        )
    write_top_artists(file_path, artists)     # new column added to the file
```
A new key on every row becomes a new column. Writing back with `'w'` replaces the original file.

## Program Structure
Small single-purpose functions (`read_`, `filter_by_`, `sort_..._by`, `write_`) and a `main()` that wires them together. Data file found with `Path(__file__).parent / 'data' / 'music_artists.csv'`.

## To Know
- [ ] `csv.DictReader` → rows as dictionaries; values are all strings
- [ ] `csv.DictWriter` + `writeheader()` + `writerow()`; open with `newline=''`
- [ ] Filter with a list comprehension, sort with `sorted(key=...)`
- [ ] Convert numeric columns before comparing or sorting
- [ ] `lambda args: expression` for short key functions
- [ ] Update = read, modify, write back

## Homework
- Challenge: `oldest_artists(artists, top_n=3)` (reuse `sort_artists_by` with `reverse=False` on `year_formed`), `filter_by_members(artists, exact_count)`, then export the 3-member bands to `data/three_member_bands.csv`

## Reflection
*What was the most surprising insight today?*
