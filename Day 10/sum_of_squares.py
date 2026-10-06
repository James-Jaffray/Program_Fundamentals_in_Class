my_square = int(input('Enter a number to sum the squares: '))
sum = 0

for i in range(my_square+1):
    # print(f'{i} X {i} = {i*i}')
    individualsum = (i*i)
    sum = (sum + individualsum)
    

print(f'The sum of squares is {sum}')