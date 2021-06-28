from math import ceil

def paint_calc(height, width, cover):
    cans = ceil(height * width / cover)
    print(f"You will need {cans} cans of paint to cover a wall that's {height} x {width} feet.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height = test_h, width =test_w, cover = coverage)