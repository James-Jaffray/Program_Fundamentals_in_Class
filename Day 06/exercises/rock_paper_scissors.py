import random

user_choice = input("Please choose rock, paper, or scissors: ").lower()

if user_choice == "rock":
    user_choice = 0
elif user_choice == "paper":
    user_choice = 1
elif user_choice == "scissors":
    user_choice = 2
else:
    print("Please choose rock, paper or scissors")
    exit()



random_draw = random.randint(0, 2)

if random_draw == 0:
    print("PC threw rock")
elif random_draw == 1:
    print("PC threw paper")
elif random_draw == 2:
    print("PC threw scissors")



if user_choice == 0 and random_draw == 1:
    print("Paper beats Rock: You lose")

elif user_choice == 0 and random_draw == 2:
    print("Rock beats Scissors: You Win!")

elif user_choice == 1 and random_draw == 0:
    print("Paper beats Rock: You Win!")

elif user_choice == 1 and random_draw == 2:
    print("Scissors beat Rock: You lose")

elif user_choice == 2 and random_draw == 0:
    print("Rock beats Scissors: You lose")

elif user_choice == 2 and random_draw == 1:
    print("Scissors beat Paper: You Win!")
else:
    print("Tie Game!")