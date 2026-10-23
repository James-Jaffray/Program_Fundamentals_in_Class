while True:
    try:
        bill_total = float(input("Please input bill total: "))
        num_of_people = int(input("Please enter number of people sharing the bill: "))
        individual_price = bill_total / num_of_people
        print(f'A bill of ${bill_total:.2f} with 5% GST, Shared by ${num_of_people} is $${individual_price:.2f} each')
        break
    except ValueError:
        print('Please enter number')
    except ZeroDivisionError:
        print('Cannot divide by 0 people')


# find bill total
# find # of people plitting bill
# calculate each persons share
# handle exceptions
