#Name: Archangel
#Date: 18/04/24 @13:52 EST
#File Name: 3.09.2 (trickyNumberz).py
#Directory: .src/3.00/3.09.2 (trickyNumberz).py
#Snapshot Ver. v1.00

#Loop
r = True # Defines "r" variable as a constant
while True: # While constant "r" is "True", repeat codeblock.
    #Input
    integ1 = int(input("\nEnter a number. -> ")) # Input for variable "integ1".
    integ2 = int(input("Enter another number. -> ")) # Input for variable "integ2".
    integ3 = int(input("Enter another number. -> ")) # Input for variable "integ3".

    #Processing
    if integ1 % 2 == 0 and integ1 > integ2 and integ3: # Checks if "integ1" is divisible by 2 and checks if "integ1" is greater than "integ2" and "integ3".
        print(f"{integ1} is the highest even number of the set.")
    elif integ2 % 2 == 0 and integ2 > integ1 and integ3: # Checks if "integ2" is divisible by 2 and checks if "integ2" is greater than "integ1" and "integ3."
        print(f"{integ2} is the highest even number of the set.")
    elif integ3 % 2 == 0 and integ3 > integ2 and integ1:  # Checks if "integ3" is divisible by 2 and checks if "integ3" is greater than "integ1" and "integ2".
        print(f"{integ3} is the highest even number of the set.")
    #Error Checking
    elif integ1 % 2 != 0 or integ1 % 2 != 0 or integ1 % 2 != 0: # Checks if "integ1", "integ2", or "integ3" ISN'T divisible by 2.
        print("Number(s) is/are not even")
    elif integ1 < 2 or integ1 < 2 or integ1 < 2: # Checks if "integ1", "integ2", or "integ3" are less than 2.
        print("Number(s) is/are below 2.")