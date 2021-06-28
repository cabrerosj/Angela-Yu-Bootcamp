import random

# Random float. Doesn't include 1.0.
# random.random(0.0, 1.0)

def coinFlip():
    choice = input("Heads or tails? ").lower()
    flip = random.randint(0,1)
    if choice == "heads" and flip == 1:
        print("You got 'heads'! You win!!!")
    if choice == "tails" and flip == 0:
        print("You got 'tails'! You win!!!")
    if choice == "heads" and flip == 0:
        print("You got 'tails'! Try again!")
    if choice == "tails" and flip == 0:
        print("You got 'heads'! Try again!")

coinFlip()