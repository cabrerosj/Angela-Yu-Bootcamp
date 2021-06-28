print("Wanna see if you're fat? Welcome to Fat Shaming App 2.0!")

kg = float(input("What is your weight in kilograms? "))
m = float(input("What is your height in meters? "))
BMI = round(kg / m ** 2)

def BMImetrics():
    if BMI < 18.5:
        print(f"Your BMI is {BMI}.\nBruh, do you even eat, bro?")
    elif BMI < 25:
        print(f"Your BMI is {BMI}.\nYou a normie. We don't like normies.")
    elif BMI < 30:
        print(f"Your BMI is {BMI}.\nI like em big. I like em chunky.")
    elif BMI < 35:
        print(f"Your BMI is {BMI}.\nBIG BOOTY HOE!")
    else:
        print(f"Your BMI is {BMI}.\nOh you fat fat. You wanna try keto?")

BMImetrics()