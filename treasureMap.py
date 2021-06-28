row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

def xMarksTheSpot():
    position = input("Where do you want to put the treasure? ")
    # position = list(position)                                     #turns each character in the string into a list item
    row = int(position[0])
    column = int(position[1]) 

    if column == 1:
        row1[row - 1] = "x"
        print(f"{row1}\n{row2}\n{row3}")
    elif column == 2:
        row2[row - 1] = "x"
        print(f"{row1}\n{row2}\n{row3}")
    elif column == 3:
        row2[row - 1] = "x"
        print(f"{row1}\n{row2}\n{row3}")

xMarksTheSpot()