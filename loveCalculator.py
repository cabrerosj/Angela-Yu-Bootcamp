print("Welcome to the Love Calculator, where your and your crush's name determines your compatability!")

firstName = input("Whats your name? ").lower()
crushName = input("Whats your crush's name? ").lower()

# Counts characters in a string
T = firstName.count("t") + crushName.count("t")
R = firstName.count("r") + crushName.count("r")
U = firstName.count("u") + crushName.count("u")
E = firstName.count("e") + crushName.count("e")

L = firstName.count("l") + crushName.count("l")
O = firstName.count("o") + crushName.count("o")
V = firstName.count("v") + crushName.count("v")

true = str(T + R + U + E)
love = str(L + O + V + E)

trueLove = true + love

def loveCalc():
    if int(trueLove) < 10  and int(trueLove) > 90:
        print(f"Your score is {trueLove}, you go together like coke and mentos.")
    elif 40 <= int(trueLove) <= 50:
        print(f"Your score is {trueLove}, you are alright together.")
    else:
        print(f"Your score is {trueLove}")

loveCalc()