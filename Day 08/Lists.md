# Day 8

## Arrays & Lists

## Homework

## Key Terms


## Modifying List items 

numbers = [10, 20, 30]
numbers[1] = 25
print("Modifed numbers:", numbers)

Replaces the element at index 1

## Slicing Lists
Use start:stop inside brackets to get a sublist
The start index is inclusive, stop is exclusive

letters = ['a', 'b', 'c', 'd', 'e']
print("First three letters:", letters[:3]) - prints the first three letters
print("Last two letters:", letters[-2:]) - last 2 letters

## Length of  List

tasks = ['email', 'meeting', 'code review']
print("Number of tasks:", len(tasks))

## Out-of-Range Index

If you try to access an index that doesn’t exist, Python will raise an IndexError .
fruits = ['apple', 'banana']
print(fruits[5]) # This will raise an IndexError as there is no 5 element

## Summary
Lists are a core data structure in Python.
You can create, access, modify, slice, and measure lists.
Practice with your own examples to get comfortable with list operations!
