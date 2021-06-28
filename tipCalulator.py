print("Welcome to the Tip Calculator!")

bill = input("What is your total bill? ")
tip = input("What percent tip would you like to add? ")
totalWithTip = "{:.2f}".format((int(tip) / 100 + 1) * float(bill))
split = input("How many people is this being split between? ")
# This allows 2 decimal places even with a 0 at the end
individual = "{:.2f}".format(float(totalWithTip) / int(split))

def perPerson():
    print(f"Your bill is ${bill}, you want to add {tip}% tip, and split between {split} people. Your total with tip is ${totalWithTip}. Each of you should pay ${individual}.")

perPerson()