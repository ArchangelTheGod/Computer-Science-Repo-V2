#Name: Archangel
#Date: 15/05/24 @13:41 EST
#File Name: 4.04.1 (rollTheDice).oy
#Directory: .src/4.00/4.04.1 (rollTheDice).py
#Snapshot Ver. v1.00

def example1():
    #Imports
    import random

    rolls = 1
    while rolls != 3:
        #Processing
        roll = random.randint(2, 6)
        roll += roll
        rolls+=1
    print(f"Rolls: 2, Total Rolled: {roll}")

def example2():
    #Imports
    import random

    roll = random.randint(2,12)
    print(roll)


#Both work similarily, but one result requires you to roll twice, and add the
#sum of the rolls. The other one requires 1 roll and outputs the roll result.