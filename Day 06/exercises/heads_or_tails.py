import random

userguess = input("Please guess heads or tails: ").lower()

if userguess == "heads":
    userguess = 1
elif userguess == "tails":
    userguess = 0
else:
    print("Please input heads or tails:")
    exit()

coinflip = random.randint(0, 1)


if userguess == coinflip:
    print("Correct!")

elif userguess != coinflip:
    print("Incorrect Please try again")




