import random


print("You encountered a wild Charizard!")
print("")
print("Which ball would you like to throw (enter the number):")
print("1: Poke Ball")
print("2: Great Ball")
print("3: Ultra Ball")
print("4: Master Ball")

selected_ball = int(input())

match selected_ball:
    case 1:
        print("Throwing Pokeball...")
        if random.randint(1, 19) + 1 > 10:
            print("Congratulations! You caught Charizard.")
        else:
            print("Charizard escaped!")
    case 2:
            print("Throwing Pokeball...")
            if random.randint(1, 19) + 2 > 10:
                print("Congratulations! You caught Charizard.")
            else:
                print("Charizard escaped!")
    case 3:
            print("Throwing Pokeball...")
            if random.randint(1, 19) + 3 > 10:
                print("Congratulations! You caught Charizard.")
            else:
                print("Charizard escaped!")
    case 4:
            print("Throwing Pokeball...")
            if random.randint(1, 19) + 4 > 10:
                print("Congratulations! You caught Charizard.")
            else:
                print("Charizard escaped!")
    case _:
          print("Invalid Selection")
          exit()