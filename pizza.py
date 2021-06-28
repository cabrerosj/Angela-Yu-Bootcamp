print("Manager: Sawp you faka! Congratz on dis job right hea at DA PIZZA HALE!\nTry ask deez fakas what kine pizza dey like.")

def pizzaOda():
    size = input("You: Sawp, fakaz. What size pizza you like? Get 'Manini', 'Regula', and 'Bambucha'. ")
    total = 0
    if size.lower() == "manini":
        total += 15
    elif size.lower() == "regula":
        total += 20
    elif size.lower() == "bambucha":
        total += 25
    else:
        print("BRAH DAS NOT ONE PIZZA YOU FAKA!")
        pizzaOda()

    pepperoni = input("You like one Italian sausage on top? 'Shoots' or 'No Need'? ")

    if pepperoni.lower() == "shoots":
        if size.lower() == "manini":
            total += 2
        elif size.lower() == "regula" or "bambucha":
            total += 3
        print("I knew you like sausage.")
    elif pepperoni.lower() == "no need":
        print("Raja.")
    else:
        print("DAS NOT ONE FUCKIN ANSA!")
        pizzaOda()

    extraCheese = input("If you like moa cheese, lmk. 'Shoots' or 'No Need'? ")
    
    if extraCheese.lower() == "shoots":
        total += 1
        print("Hope you get Lactaid!")
    elif extraCheese.lower() == "no need":
        print("Raja.")
    else:
        print("DAS NOT ONE FUCKIN ANSA!")
        pizzaOda()

    finalTotal = "{:.2f}".format(total)

    print(f"Brah, you fuckin hungry, ah? You wen oda one {size} pizza with stuff on top. Your total steh ${finalTotal}. HURRY UP! GIMME MY MONEY!\n*Customa wen pay*\nYou: K wait ova dea fass kine. Going be about one hour. I call when the ting steh finish.")
    

pizzaOda()