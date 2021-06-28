import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = input("Rock, Paper, or Scissors? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
npcChoice = random.randint(0, 2)

def fingerBattle():
    if choices == str(0):
        print(f"You chose:\n{rock}")
        if npcChoice == 0:
            print(f"The Computer chose:\n{rock}\nYou tied!")
        elif npcChoice == 1:
            print(f"The Computer chose:\n{paper}\nYou lose!")
        elif npcChoice == 2:
            print(f"The Computer chose:\n{scissors}\nYou win!")
    elif choices == str(1):
        print(f"You chose:\n{paper}")
        if npcChoice == 0:
            print(f"The Computer chose:\n{rock}\nYou win!")
        elif npcChoice == 1:
            print(f"The Computer chose:\n{paper}\nYou tied!")
        elif npcChoice == 2:
            print(f"The Computer chose:\n{scissors}\nYou lose!")
    elif choices == str(2):
        print(f"You chose:\n{scissors}")
        if npcChoice == 0:
            print(f"The Computer chose:\n{rock}\nYou lose!")
        elif npcChoice == 1:
            print(f"The Computer chose:\n{paper}\nYou win!")
        elif npcChoice == 2:
            print(f"The Computer chose:\n{scissors}\nYou tied!")
    else:
        print("EERRRRR!!! Wrong entry. BOY BYE!")

fingerBattle()