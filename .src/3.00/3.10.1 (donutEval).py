#Name: Archangel
#Date: 19/04/24 @09:42 EST
#File Name: 3.10.1 (donutEval).py
#Directory: .src/3.00/3.10.1 (donutEval).py
#Snapshot Ver. v1.00

#Import
import random as rand

#Loop
r = True # constant r is a true loop
while True: # While constant r is true...,
    #Input
    #   Menu Processing
    print("\n\t<------(Menu)------>")
    print("Doughnuts\t\t$2.00/ea")
    print("Danishes\t\t$1.50/ea")
    print("Cinnamon Rolls\t\t$3.00/ea")
    print("Abbreviations: d, dn, cr")
    #   Input Collection
    userSelect = input("\nWhat kind of pastries would you like? -> ")
    quantSelect = int(input("How many would you like? -> "))
    if quantSelect is isinstance(quantSelect,int): # Checks if "quantSelect" is an integer. If true, program throws an error and breaks loop.
        print("[Error!] Quantity must be an integer.")
        break # Breaks constant r Loop

    #Constants
        #   Item Prices
    doughnutPrice = 2.00 # Price of a singular Doughnut
    danishPrice = 1.50 # Price of a singular Danish
    cinnamonRollsPrice = 3.00 # Price of a singular Cinnamon Roll
        #   Toppings Prices
    sprinklez = 0.15
    icing = 0.05
    butterCream = 0.10
        #   Tax & Discount
    tax = .13 # Tax of 13%
    discount = 20 # Discount of 20% if 12 or more items are purchased with toppings



    # Random
    orderNumber = rand.randrange(9999) + 1 # Assigns a random number from 1 to 10,000 for an order number

    #Processing
    if userSelect == "Doughnuts".lower() or userSelect == "d".lower(): # Doughnuts Processing
            # Price Processing
        dsubtotal = round(doughnutPrice*quantSelect,2)
            #Toppings Processing
        print("\n\t\t\tSelect Applicable.") # Topping Menu
        print("Toppings Menu: Sprinkles (0.15c per Doughnut)")
        askToppings = input("Would you like toppings? -> ")
        if askToppings == "y".lower() or askToppings == "Yes".lower(): # Checks if string input is equal to "y" or "Yes"
            if quantSelect >= 12: # Checks if the quantity of product is above or greater than 12, if true, calculate new sub total with 20% discount
                sprinklez = round(sprinklez*quantSelect, 2)
                dsubtotal = round(dsubtotal*discount/100,2)
                dtotal = round(tax+dsubtotal+sprinklez, 2)
                tax = round(tax*dsubtotal, 2)
            elif quantSelect < 12 or quantSelect >= 1: # Checks if the quantity of the product is less than 12 or greater than and equal to 1, if true, calculate tax and new subtotal.
                sprinklez = round(sprinklez*quantSelect, 2)

                dtotal = round(tax+dsubtotal+sprinklez, 2)
                tax = round(tax*dsubtotal, 2)
        elif askToppings == "n".lower() or askToppings == "No".lower(): # Checks if the string input is equal to "n" or "No", if true, calculate tax and total.
            print("No toppings then.")
            dtotal = round(tax+dsubtotal, 2)
            tax = round(tax*dsubtotal, 2)

        # Receipt Processing
        print("\n\tOrder Summary")
        print(f"ORDER NUMBER: {orderNumber}")
        print(f"Item:\t\t\t{userSelect}(s)")
        print(f"Quantity:\t\t{quantSelect}")
        print(f"Subtotal:\t\t${dsubtotal}")
        print(f"Tax:\t\t\t${tax}")
        print("------------------------------------")
        print(f"Total:\t\t\t${dtotal}")

    elif userSelect == "Danish".lower() or userSelect == "dn".lower(): # Danish Processing
        # Price Processing
        dnsubtotal = danishPrice*quantSelect
        # Toppings Processing
        print("\n\t\t\tSelect Applicable.") # Topping Menu
        print("Toppings Menu: Icing (0.05c per Danish)")
        askToppings = input("Would you like toppings? -> ")
        if askToppings == "y".lower() or askToppings == "Yes".lower(): # Checks if string input is equal to "y" or "Yes"
            if quantSelect >= 12: # Checks if the quantity of product is above or greater than 12, if true, calculate new sub total with 20% discount
                icing = round(icing*quantSelect, 2)
                dnsubtotal = round(discount*dnsubtotal/100,2)
                dntotal = round(tax+dnsubtotal+icing, 2)
                tax = round(tax*dnsubtotal, 2)
            elif quantSelect >= 1 or quantSelect < 12: # Checks if the quantity of the product is less than 12 or greater than and equal to 1, if true, calculate tax and new subtotal.
                dntotal = round(tax+dnsubtotal+icing, 2)
                tax = round(tax*dnsubtotal, 2)
        elif askToppings == "n".lower() or askToppings == "No".lower(): # Checks if the string input is equal to "n" or "No", if true, calculate tax and total.
            print("No toppings then.")
            dntotal = round(tax+dnsubtotal, 2)
            tax = round(tax*dnsubtotal, 2)
        # Receipt Processing
        print("\n\tOrder Summary")
        print(f"ORDER NUMBER: {orderNumber}")
        print(f"Item:\t\t\t{userSelect}(s)")
        print(f"Quantity:\t\t{quantSelect}")
        print(f"Subtotal:\t\t${dnsubtotal}")
        print(f"Tax:\t\t\t${tax}")
        print("------------------------------------")
        print(f"Total:\t\t\t${dntotal}")

    elif userSelect == "Cinnamon Roll".lower() or userSelect == "cr".lower(): # Cinnamon Rolls Processing Processing
        # Price Processing
        crsubtotal = cinnamonRollsPrice*quantSelect
        #Toppings Processing
        print("\n\t\t\tSelect Applicable.") # Topping Menu
        print("Toppings Menu: Buttercream Icing (0.10c per Cinnamon Roll.)")
        askToppings = input("Would you like toppings? -> ")
        if askToppings == "y".lower() or askToppings == "Yes".lower(): # Checks if string input is equal to "y" or "Yes"
            if quantSelect >= 12: # Checks if the quantity of product is above or greater than 12, if true, calculate new sub total with 20% discount
                butterCream = round(butterCream*quantSelect, 2)
                crsubtotal = round(discount*crsubtotal/100,2)
                crtotal = round(tax+crsubtotal+butterCream, 2)
                tax = round(tax*crsubtotal, 2)
            elif quantSelect >= 1 or quantSelect < 12: # Checks if the quantity of the product is less than 12 or greater than and equal to 1, if true, calculate tax and new subtotal.
                butterCream = round(butterCream*quantSelect, 2)
                crtotal = round(tax+crsubtotal+butterCream, 2)
                tax = round(tax*crsubtotal, 2)
        elif askToppings == "n".lower() or askToppings == "No".lower(): # Checks if the string input is equal to "n" or "No", if true, calculate tax and total.
            print("No toppings then.")
            crtotal = round(tax+crsubtotal, 2)
            tax = round(tax*crsubtotal, 2)
        # Receipt Processing
        print("\n\tOrder Summary")
        print(f"ORDER NUMBER: {orderNumber}")
        print(f"Item:\t\t\t{userSelect}(s)")
        print(f"Quantity:\t\t{quantSelect}")
        print(f"Subtotal:\t\t${crsubtotal}")
        print(f"Tax:\t\t\t${tax}")
        print("------------------------------------")
        print(f"Total:\t\t\t${crtotal}")

    #   Error Catching- Checks if string input is NOT equal to any of these OTHER strings simultaneously. If all flags are true, order will not be proecessed and program will self-terminate.
    elif userSelect != "Cinnamon Roll".lower() and userSelect != "cr".lower() and userSelect != "Danish".lower() and userSelect !="dn".lower() and userSelect != "Doughnuts".lower() and userSelect != "d".lower():
        print("\n[Error!] Invalid order!")
        print(f"[Error!] Error found at -> ({userSelect})")
        break # Breaks Loop if all flags are true

#       TESTING
#Treatment 1: Doughnuts, 12 items, no toppings
#Expected Output(s): No discount, $24 (Without federal tax), $3.12 Tax
#Output: Total: $24.13, Tax: $3.12
#
#Treatment 2: Doughnuts, 12 items, yes toppings
#Expected Output(s): 20% Discount, Total: $6.73, Tax: $0.62
#Output: Total: $6.73, Tax: $0.62
#
#Treatment 3: Doughnuts, < 12 items (5), no toppings
#Expected Output(s): No Discount, Total: $10.13, Tax: $0.13
#Output: Total: $10.13, Tax: $0.13
#
#Treatment 4: Doughnuts, < 12 items (5), yes toppings
#Expected Output(s): No discount, Total: $10.88
#
#       FOREWORD: SINCE ALL ITEMS SHARE THE SAME SOURCECODE BASE, THE TESTING TREATMENT RESULTS APPLY TO ALL ITEMS IN THE LISTED SCENARIOS.
