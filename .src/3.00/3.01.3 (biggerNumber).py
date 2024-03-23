#Name: Archangel
#Date: 19/03/24 @08:35 EST
#File Name: 3.01.3 (biggerNumber).py
#Directory: .src/3.00/3.01.3 (biggerNumber).py
#Snapshot Ver. v1.00


#Input
number1 = int(input("Enter a number. => "))
number2 = int(input("Enter another number. => "))

#Processing
if number1 < number2:
    output = f"{number2} is greater than {number1}"
elif number1 > number2:
    output = f"{number1} is greater than {number2}"

#Output
print("\n<== Results ==>")
print(output)