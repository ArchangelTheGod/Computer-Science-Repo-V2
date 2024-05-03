#Name: Archangel
#Date: 02/05/24 @10:22 EST
#File Name: 4.01.2 (groceryCalculator).py
#Directory: .src/4.00/4.01.2 (groceryCalculator).py
#Snapshot Ver. v1.00

#Inputs
totalItems = int(input("How many items did you purchase? -> "))

#Loop
for i in range(totalItems):
    totalCost = float(input("What is the item cost? -> "))
    
    #Processing
        # Constants
    tax = 0.13
    totalCost *= totalItems
    total = round(totalCost+tax,2)

    print(f"Total: ${total}")