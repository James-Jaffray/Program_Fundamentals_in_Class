year = int(input("Please enter a year: "))

animal = ["monkey", "rooster", "dog", "pig", "rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep"]

animal_num = year % 12

print(animal[animal_num])