---
aliases: [Programming Fundamentals - Day 18]
tags: [programming-fundamentals, term1, lecture-notes, python, dictionaries, loops]
course: "[[Programming Fundamentals]]"
day: 18
---

# Programming Fundamentals — Day 18: Looping Through Dictionaries

**Today's focus:** looping over a dictionary's keys, values and key-value pairs, tallying with a second dictionary, and combining dictionaries with lists. Builds on [[Dictionary Basics]] and [[Python Loops]].

## Three Ways to Loop
Same idea as looping a list, but you pick *what* you get back:

| Method | Gives you | Use when |
|---|---|---|
| `d.keys()` | each key | you only need the names |
| `d.values()` | each value | you only need the data |
| `d.items()` | each `(key, value)` pair | you need both |

```python
for voter in fav_fruit_voters.keys():       # keys (also the default if you just loop `d`)
    print(f"- {voter}")

for vote in fav_fruit_voters.values():      # values
    ...

for fruit, votes in voting_results.items(): # both, unpacked into two variables
    print(f"- The fruit: {fruit} has {votes} votes")
```
`for fruit, votes in ...` is **multiple assignment**: each pair gets split into two names.

## The Voting Example
Two dictionaries: `fav_fruit_voters` (name → fruit) and `voting_results` (fruit → count, all starting at 0). Goal: tally the votes.

**First attempt** with an `if/elif` per fruit works but doesn't scale:
```python
for vote in fav_fruit_voters.values():
    if vote == "banana":
        voting_results["banana"] += 1
    elif vote == "apple":
        voting_results["apple"] += 1
    ...
```

**Refactor**: the vote *is* the key, so use it directly.
```python
for vote in fav_fruit_voters.values():
    voting_results[vote] += 1
```
One line, handles any fruit already in `voting_results`.

## Totals and Sorted Output
```python
total_votes = 0
for count in voting_results.values():
    total_votes += count
print(f"Total votes cast: {total_votes}")

for fruit, votes in sorted(voting_results.items()):   # alphabetical by key
    print(f"- The fruit: {fruit} has {votes} votes")
```
`sorted()` on `items()` orders by key by default.

## Taking Input Into the Dictionary
```python
name = input("What's your name? ").lower()
user_fav_fruit = input("What is your favorite fruit? ").lower()
fav_fruit_voters[name] = user_fav_fruit      # adds a new voter
```
**Challenge:** a new fruit isn't in `voting_results` yet, so `voting_results[vote] += 1` would raise a `KeyError`. Check `if vote not in voting_results` and add it (starting at 0) before counting. See [[Dictionary Basics]] for `in` and `get()`.

## Dictionaries and Lists Together
Practice structures from the Crash Course exercises (6-7 to 6-11):
- **List of dictionaries**: one dictionary per person or pet, loop the list and print each one's contents
- **Dictionary with list values**: a person with several favorite numbers or places
- **Dictionary of dictionaries**: cities as keys, each holding `country`, `population`, `fact`

Loop pattern for a dictionary of dictionaries:
```python
for city, info in cities.items():
    print(city)
    for key, value in info.items():
        print(f"  {key}: {value}")
```

## To Know
- [ ] `keys()`, `values()`, `items()` and what each returns
- [ ] `for key, value in d.items():` unpacks each pair
- [ ] Use the value as a key to tally: `counts[x] += 1` (key must exist first)
- [ ] `sorted(d.items())` for ordered output
- [ ] Dictionaries can hold lists, and lists can hold dictionaries

## Homework
- Crash Course dictionary exercises 6-1, 6-2, then 6-7 to 6-11

## Reflection
*What was the most surprising insight today?*
