#Name: Archangel
#Date: 29/04/24 @11:08 EST
#File Name: 4.00 Example 2.py
#Directory: .src/4.00/4.00 Example 2.py
#Snapshot Ver. v1.00

#Inputs
num = int(input("Enter a number. -> "))

#Constants
num2 = 3
num3 = 2

#Processing
    #Loop
for num in range(num,0,-1):
    print(f"{num} ^{num2} = {num**num2}")
    print(f"{num} ^{num3} = {num**num3}")
    print("\n")