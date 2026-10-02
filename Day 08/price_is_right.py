import random

price1 = random.randint(1,10)
price2 = random.randint(1,10)
price3 = random.randint(1,10)

guess = input('Guess the price of the item: ')

pricelist = [price1,price2,price3]

if guess in pricelist:
    print('You win!')
else:
    print('You Lose!')

print('The prices were:')
print(pricelist)