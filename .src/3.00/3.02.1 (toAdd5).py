#Name: Archangel
#Date: 20/03/24 @10:24 EST
#File Name: 3.02.1 (toAdd5).py
#Directory: .src/3.00/3.02.1 (toAdd5).py
#Snapshot Ver. v1.00

#Inputs
number1 = int(input("Enter a number. => "))
number2 = int(input("Enter another number. => "))

#Processing
number1 = number1 + 5

if number2 > 10:
    number2 = number2 + 5
else:
    number2 = number2 + 0 
#Output
print("\n<== Results ==>")
print(f"First Number Result: {number1} \nSecond Number Result: {number2}")