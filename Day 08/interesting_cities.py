cities = [
'Edmonton',
'Paris',
'Munich',
'Berlin',
'Amsterdam',
'Prague'
]

print (f'Cities: {cities}')
cities.remove('Edmonton')
cities.append('Tokyo')
cities.sort()
print(f'Our list of interesting cities in alphabetical order is: {cities}')