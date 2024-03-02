#Name: Archangel
#Date: 29/02/24 @12:12 EST
#File Name: 2.04.2 (Mathematical Equations Example II).py
#Directory: .src/2.00/2.04.2 (Mathermatical Equations Example II).py
#Snapshot Ver. v1.00

#Inputs
n1 = float(input('Enter the first digit. => '))
n2 = float(input('Enter the second digit. => '))
n3 = float(input('Enter the third digit. => '))

#Calc
sum = (n1 + n2 + n3) #Adds the variable floats and converts into a singular float
avg = sum / 3 #Calculates the average of the sum variable.

#Output
print("\n<== Results ==>")
print(f"Average of {n1}, {n2}, {n3} is:", avg)
print("The sum of the variables however, is:", sum)