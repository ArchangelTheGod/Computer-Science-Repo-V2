#Name: Archangel
#Date: 25/03/24 @08:35 EST
#File Name: 3.04.2 (weightGrouper).py
#Directory: .src/3.00/3.04.2 (weightGrouper).py
#Snapshot Ver. v1.00

#Input
weight = int(input("W=Enter a weight"))

#Processing
if weight > 80:
    print("You qualify for Heavy-weight Wrestling")
elif weight >= 60 and weight <= 80:
    print("You qualify for Medium-weight Wrestling")
elif weight < 60:
    print("You quallify for Light-weight Wrestling") 
