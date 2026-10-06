pk_a_price = 9.95
pk_b_price = 13.95
pk_c_price = 19.95
num_of_hours = 0


while True:
    package_selected = input('Enter the Package: ').upper()
    if package_selected in('A', 'B', 'C'):
        break
    else:
        print(f'Please choose valid package')

while True:
    num_of_hours = input('Enter the number of hours used: ')
    if int(num_of_hours) > 0:
        break
    else:
        print(f'Please enter a valid number of hours')


match package_selected:
    case 'A':
        overdraft = num_of_hours - 10
        total = pk_a_price + (overdraft*2)
        print(f'The total price is ${total}')
    case 'B':
        overdraft = num_of_hours - 20
        total = pk_b_price + (overdraft*1)
        print(f'The total price is ${total}')
    case 'C':
        total = pk_c_price
        print(f'The total price is ${total}')