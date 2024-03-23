#Name: Archangel
#Date: 21/03/24 @12:46 EST
#File Name: 3.03.4 (lesserNumber).py
#Directory: .src/3.00/3.03.4 (lesserNumber).py
#Snapshot Ver. v1.00

#Inputs
num1 = int(input("Enter a number. => "))
num2 = int(input("Enter another number. => "))

#Processing
if num1 < num2:
    print(f"{num1} is less than {num2}")
elif num1 == num2:
    print(f"{num1} is equal to {num2}")
elif num2 < num1:
    print(f"{num2} is less than {num1}")