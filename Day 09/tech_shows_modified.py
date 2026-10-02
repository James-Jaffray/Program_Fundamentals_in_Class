tv_shows = [
    'Silicon Valley',
    'Halt and Catch Fire',
    'Blackberry',
    'The Billion Dollar Code',
    'Mr. Robot',
    'The IT Crowd',
    'WeCrashed',
    'The Social Network',
    'Severance',
    'Pirates of Silicon Valley',
]

print('The first item on the list')
print(tv_shows[0])
print('The last item on the list.')
print(tv_shows[-1:])

tv_shows[6] = "The Dropout"
print('Change "WeCrashed" to "The Dropout"')
print(tv_shows[6])


tv_shows[8] = "Black Mirror"
print('Change "The Social Network" to "Black Mirror"')
print(tv_shows[8])

print(tv_shows[4:9])
print('The top five shows are:')
print(f'Ranked 1 is: {tv_shows[0]}')
print(f'Ranked 1 is: {tv_shows[1]}')
print(f'Ranked 1 is: {tv_shows[2]}')
print(f'Ranked 1 is: {tv_shows[3]}')
print(f'Ranked 1 is: {tv_shows[4]}')



