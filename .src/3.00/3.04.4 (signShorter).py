#Name: Archangel
#Date: 21/03/24 @12:50 EST
#File Name: 3.04.4 (signShorter).py
#Directory: .src/3.00/3.04.4 (signShorter).py
#Snapshot Ver. v1.00

#Inputs
num = int(input("Enter a negative or positive number. => "))

#Processing
if num <= -1:
    print(f"{num} is a negative number.")
elif num >= 0:
    print(f"{num} is a positive")