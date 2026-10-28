
# burger dictionary
burger = {
    'patties': 1,
    'patty_type': 'beef',
    'chese': True,
    'toppings': ['lettuce', 'tomato', 'onion', 'pickles', 'ketchup', 'mustard'],
    'bun': 'sesame seed'
}


burger['patties'] = 2
burger['patty_type'] = 'vegetarian'
burger['cheese'] = False
burger['bun'] = 'whole wheat'



print("Here's what's in your burger:")
print(f"{burger['patties']} {burger['patty_type']} patties is on your burger.")
