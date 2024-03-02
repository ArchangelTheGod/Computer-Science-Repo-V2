#Name: Archangel
#Date: 29/02/24 @12:22 EST
#File Name: 2.04.5 (Mathematical Equations).py
#Directory: .src/2.00/2.04.5 (Mathermatical Equations).py
#Snapshot Ver. v1.06

#Input and Variable Checker
run1 = True
run2 = True
while run1:
    try:
        number1 = int(input("Enter a number between 2 and 9. => "))
        if number1 < 1 or number1 > 9:
            print("Error! Number cannot be below 1 or above 9!")
        else:
            run1 = False
    except:
        print("Error! Number cannot be below 1 or above 9!")

while run2:
    try:
        number2 = int(input("Enter a number between 2 and 9. => "))
        if number2 < 1 or number2 > 9:
            print("Error! Number cannot be below 1 or above 9!")
        else:
            run2 = False
    except:
        print("Error! Number cannot be below 1 or above 9!")

ans1 = number1+number2
ans2 = number1-number2
ans3 = number1*number2
ans4 = number1/number2
ans5 = number1**number2

#Output
print(f"\nEquation 1: {number1}+{number2}={ans1}")
print(f"Equation 2: {number1}-{number2}={ans2}")
print(f"Equation 3: {number1}*{number2}={ans3}")
print(f"Equation 4: {number1}/{number2}={ans4}")
print(f"Equation 5: {number1}^{number2}={ans5}")