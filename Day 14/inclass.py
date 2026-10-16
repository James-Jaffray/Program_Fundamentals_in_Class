def get_temperature():
    return float(input("Enter the temperature: "))

def is_hot(temp):
    return temp > 30

temp = get_temperature()

if is_hot(temp):
    print("It's a hot day!")
else:
    print("It's not too hot.")



user_entered_temp = get_temperature()

if is_hot(user_entered_temp):
    print("It's a hot day!") 
else:
    print("It's not too hot.")