#Name: Archangel
#Date: 20/03/24 @10:30 EST
#File Name: 3.02.2 (outToLunch).py
#Directory: .src/3.00/3.02.2 (outToLunch).py
#Snapshot Ver. v1.00

#Inputs
cost = float(input("Enter the price of your meal. => "))

#Constants
tax = .8
total = round(0.8*cost, 4)

#Processing
if cost > 4.00:
    print(f"Total cost calculated with tax: {total}")
else:
    print(f"Total cost (Without tax): {cost}")