BASE_PRICE = 12.00
TIP = 1.18
total_price = 0


toppings = {
    'cheese' : True,
    'pepperoni' : True,
    'mushrooms' : False,
    'pineapple' : False,
    'anchovies' : True,
    'olives' :  False,
    'sausage' : True
}
toppings_prices = {
    'cheese' : 0.5,
    'pepperoni' : 2.0,
    'mushrooms' : 1.0,
    'pineapple' : 0.5,
    'anchovies' : 1.5,
    'olives' :  1.25,
    'sausage' : 2.25
}

print("The toppings of your pizza are:")

for ingredient in toppings:
    if toppings[ingredient] == True:
        print(ingredient)
        ingredient_price = toppings_prices.get(ingredient)
        total_price = total_price + ingredient_price
    else:
        print(f'No {ingredient}')

total_price = (total_price + BASE_PRICE) * TIP
print(f"Your total is: ${total_price:.2f}")