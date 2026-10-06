interesting_cities = [
'Edmonton',
'Paris',
'Munich',
'Berlin',
'Amsterdam',
'Prague'
]

print (f'Cities: {interesting_cities}')
interesting_cities.remove('Edmonton')
interesting_cities.append('Tokyo')
interesting_cities.sort()
print(f'Our list of interesting cities in alphabetical order is: \n{interesting_cities}')

invalid_cities = ['Munich', 'Berlin']

for city in interesting_cities:
    if city not in invalid_cities:
        print(F"{city} is an interesting city that we can visit")
    