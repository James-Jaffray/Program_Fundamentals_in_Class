num_1 = (input("Please insert a number between 1 - 100: "))

if type(num_1) == str:
    print("please insert a valid number between 1 - 100")
else:

    if num_1 < 50 and num_1 >= 0:
        print(f"{num_1} is Less than 50")
    elif num_1 > 49 and num_1 <= 100:
        print(f"{num_1} is greater than 50")
    else:
        print("please insert a valid number between 1 - 100")
