#Name: Archangel
#Date: 21/03/24 @12:33 EST
#File Name: 3.03.1 [2] (correctLogicErrors).py
#Directory: .src/3.00/3.03.1 [2] (correctLogicErrors).py
#Snapshot Ver. v1.00

#Inputs
integ = int(input("Enter an integer. => "))

#Process
if integ > 10 and integ < 99:
    print(f"{integ} is a two-digit number.")
elif integ < 10:
    print(f"{integ} is a single-digit number")
elif integ > 99:
    print(f"{integ} is a three-digit number")