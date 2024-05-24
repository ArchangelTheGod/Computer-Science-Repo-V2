#Name: Archangel
#Date: 22/05/24 @12:54 EST
#File Name: 4.05.1 (guessingGame).py
#Directory: .src/4.00/4.05.1 (guessingGame).py
#Snapshot Ver. v1.00

#Constants
streak = 0
numGen = 0
userNum = 0
confirm = False

#Imports
import random as r

#Loop
while confirm == False:
    #Input
    userNum = int(input("Guess a number. -> "))

    #Random
    numGen = r.randrange(0,4)
    if userNum > 4:
        print("No, bro. No.")
        break

    if userNum == numGen:
        print(f"Correct! The number is {numGen}!")
        print(f"It took you {streak} tries to guess the number!")
        confirm = True
    elif userNum != numGen:
        streak += 1
        print("Wrong, try again.")
        confirm = False