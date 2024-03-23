#Name: Archangel
#Date: 19/03/24 @08:40 EST
#File Name: 3.01.4 (smallerNumber).py
#Directory: .src/3.00/3.01.4 (smallerNumber).py
#Snapshot Ver. v1.00

#Input
number1 = int(input("Enter a number. => "))
number2 = int(input("Enter another number. => "))

#Processing
if number1 < number2:
    output = f"{number1} is less than {number2}"
elif number2 < number1:
    output = f"{number2} is less than {number1}"

#Output
print("\n<== Results ==>")
print(output)