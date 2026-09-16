year = int(input("Please enter a year: "))

if (year % 4) == 0 and (year % 100) != 0 and (year % 400) != 0:
    print(f"{year} is a leap? True")

else:
    print(f"{year} is a leap year? False")

    

