print("Welcome to Odds or Evens.")

def oddEven(number):
    number = int(number)
    if number % 2 == 0:
        print("This number is Even.")
        return oddEven(input("Type in a number you'd like to check: "))
    else:
        print("This number is Odd.")
        return oddEven(input("Type in a number you'd like to check: "))

oddEven(input("Type in a number you'd like to check: "))