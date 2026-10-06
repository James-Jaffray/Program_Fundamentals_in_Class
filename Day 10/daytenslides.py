students = ["Alice", "Bob", "Charlie"]

for idx, student in enumerate(students):
    print(f"Student {idx + 1} {student}")


numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        continue # Skip even numbers
    print(f"Odd number: {n}")