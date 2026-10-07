pk_a_price = 9.95
pk_b_price = 13.95
pk_c_price = 19.95
num_of_hours = 0


while True:
    package_selected = input('Enter the Package: ').upper()
    if package_selected in ('A', 'B', 'C'):
        break
    else:
        print(f'Please choose valid package')

while True:
    try:
        num_of_hours = int(input('Enter the number of hours used: '))
    except ValueError:
        print(f'Please enter a valid number of hours')
        
    if num_of_hours <= 0:
        print("You didn't enter any hours")
    else:
        break



match package_selected:
    case 'A':
        if num_of_hours > 10:
            overdraft = num_of_hours - 10
            total = pk_a_price + (overdraft*2)
            print(f'The total price is ${total}')
        else:
            total = pk_a_price
            print(f'The total price is ${total}')

    case 'B':
        if num_of_hours > 20:
            overdraft = num_of_hours - 20
            total = pk_b_price + (overdraft*1)
            print(f'The total price is ${total}')
        else:
            total = pk_b_price
            print(f'The total price is ${total}')
    case 'C':
        total = pk_c_price
        print(f'The total price is ${total}')