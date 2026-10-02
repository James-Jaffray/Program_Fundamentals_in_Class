numbers = [42, 7, 19, 100, 3]
numbers.sort()
print("Sorted numbers:", numbers)
numbers.sort(reverse=True)
print("Sorted (descending)", numbers)


print(len(numbers))

print(f'After sorting, 100 is in index: {numbers.index(100)}')
