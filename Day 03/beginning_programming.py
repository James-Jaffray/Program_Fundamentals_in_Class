# Ask the user for a temperature in Celsius and convert it to Fahrenheit.
# %%

celsius = input("Provide temp in celsius: ")
celsius = float(celsius)
fahrenheit = (celsius*(9/5)) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F")



# Ask the user for a name, an adjective, a verb (past tense) and a place.
# Print a silly sentence using them.
# %%

name = input("Please input a name: ")
adjective = input("Please input an adjective: ")
verb = input("Please input a (past tense) verb: ")
place = input("Please input a Place: ")

print(f"{name} was spending their day {adjective} until he remembered \nhe forgot his phone back at {place}. \nso they quickly {verb} back to {place} to get it")


# Ask the user for the width and height of a rectangle. There could be
# decimals. Calculate and display the width, height, area, and perimeter.
# Calculations print the results rounded to 3 decimal places.
# %%

width = float(input("Please insert a width: "))
height = float(input("Please insert a height: "))


area = width * height
perimeter = (width*2) + (height*2)

print(f"Width: {width:.3f}\nHeight: {height:.3f} \nArea: {area:.3f}\nPerimeter: {perimeter:.3f}")


# Ask for the price of an item and the quantity purchased. Display the
# amount of the total including GST
# %%

price = float(input("Please insert the price in dollars: "))
qty = int(input("Please insert the quantity: "))
gst = 1.05

pre_gst = price*qty
post_gst = pre_gst*gst

print(f"The final cost will be: {post_gst:.2f}")




# Ask the user for a number of miles and print out how many kilometres
# it is. Display to 2 decimal places.
# The conversion rate is 1 mile = 1.609344 kilometers
# %%

miles = input("Please insert number of miles to be converted: ")
miles = float(miles)

kilometers = (miles * 1.609344)
print(f"{miles} miles is equal to {kilometers:.2f} kilometers")

# Ask the user for the distance they want to travel, the fuel consumption
# of their vehicle in l/100km and the price per litre. Display the cost for
# the trip!
# %%

distance_wanted = int(input("What distance are you looking to travel in km: "))
fuel_consumption = float(input("vehicles fuel consumption per 100km: "))
price_per_litre = float(input("current price per L: "))

litres_need = (distance_wanted / 100) * fuel_consumption
overall_cost = litres_need * price_per_litre

print(f"Traveling {distance_wanted}km's would cost: ${overall_cost:.2f}")
# %%


