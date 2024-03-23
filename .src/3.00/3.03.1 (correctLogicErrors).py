#Name: Archangel
#Date: 21/03/24 @12:30 EST
#File Name: 3.03.1 (correctLogicErrors).py
#Directory: .src/3.00/3.03.1 (correctLogicErrors).py
#Snapshot Ver. v1.00

#Inputs
num = int(input("Enter a number. => "))

#Processing
if num <= 10 and num >= 5:
    print(f"{num} is above 5 and below 10.")
else:
    print(f"{num} is not between 5 or 10.")