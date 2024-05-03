#Name: Archangel
#Date: 12/04/24 @09:47 EST
#File Name: 3.06 (cookieOrder).py
#Directory: .src/3.00/3.06 (cookieOrder).py
#Snapshot Ver. v1.00

#Loop
r = True
while True:
    #Inputs
    print("You choices are: Chocolate Chip, Raisin, & Shortbread.")
    cookieBox = input("What type of cookie do you want to order? -> ")
    cookieNum = int(input("How many boxes of cookies do you want to order? -> "))

    #Constants
    cost = 6.95
    tax = 0.13
    discount = 10
    #Processing
    if cookieBox == "Chocolate Chip".lower or cookieBox == "Raisin".lower() or cookieBox == "Shortbread".lower():
        if cookieNum < 5 or cookieNum < 10:
            total = round(tax*cost, 4)
            print(f"You total is ${total}. Enjoy!")