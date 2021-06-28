year = int(input("Which year do you want to check? "))

def isLeap():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("LEAP YEAR!")
            else:
                print("NOT LEAP YEAR!")
        else:
            print("LEAP YEAR")
    else:
        print("NOT LEAP YEAR!")
isLeap()