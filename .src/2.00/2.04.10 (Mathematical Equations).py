#Name: Archangel
#Date: 29/02/24 @12:55 EST
#File Name: 2.04.10 (Mathematical Equations).py
#Directory: .src/2.00/2.04.10 (Mathermatical Equations).py
#Snapshot Ver. v1.00

#Input
hours = int(input("Input a value for hours. => "))
minutes = int(input("Input a value for minutes. => "))
seconds = int(input("Input a value for seconds. => "))

#Calc/Conversion
convertedmins = minutes/60
convertedsecs = seconds/60
rounded1 = round(convertedmins, 1)
rounded2 = round(convertedsecs, 1)
total = hours+rounded1+rounded2

#Output
print("Total", total)