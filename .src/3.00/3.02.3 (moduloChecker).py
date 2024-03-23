#Name: Archangel
#Date: 20/03/24 @10:40 EST
#File Name: 3.02.3 (moduloChecker).py
#Directory: .src/3.00/3.02.3 (moduloChecker).py
#Snapshot Ver. v1.00

#Inputs
number1 = int(input("Enter a number. => "))
number2 = int(input("Enter another number. => "))

#Calc/Processing
mod = number1%number2

#Prompt
r = True
while True:
    print(f"\nCalculate the modulo of {number1} and {number2}.")
    confirm1 = str(input("Ready? [TYPE 'Ok' to continue.] => "))
    if confirm1 == "Ok".lower():
        stateReady = True
        break
    else:
        print("Process Terminated.")
        break

if stateReady == True:
    answer = int(input("\nOkay, now input your answer. => "))
    if answer != mod:
        print(f"\nWrong. The answer was {mod}. You answered {answer}.")
        print("Modulo works by using integer division to divide your first variable, 'a' by the second variable 'b'.")
        print(f"Like this: {number1} % {number2} = {mod}")
    else:
        print(f"\nNice job! you answered {number1} mod {number2} = {mod}!")