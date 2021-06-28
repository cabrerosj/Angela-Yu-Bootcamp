import random
print("Welcome to Bankers' Roulette!\nType in the names of your meal party and let us choose who pays!")

question = input("Who is in your party? ").title()
party = question.split(", ")

def bankersRoulette():
    rng = random.randint(1, (len(party) - 1))
    print(f"{party[rng]} is paying today!")

bankersRoulette()

# a = ["one", "two", "three", "four", "five"]

# This will choose a random item in the list for you
# print(random.choice(a))