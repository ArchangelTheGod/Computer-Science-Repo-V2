#Name: Archangel
#Date: 16/04/24 @12:19 EST
#File Name: 3.09.1 (alienz).py
#Directory: .src/3.00/3.09.1 (alienz).py
#Snapshot Ver. v1.00

#Loop
r = True 
while True: # While Loop
    #Inputs
    print("\nPlease provide information about the type of alien that has illegally entered our atmosphere. Ready?") # Initial Print Statement With Instructions
    isAlien = input("Did you spot an alien? -> ") # Checks if your REALLY saw an Alien

    #Processing
    if isAlien == "Yes".lower() or isAlien == "y".lower():
        howManyAntennae = int(input("How many antennae did you see on it's head? -> ")) # How many antennae did you see on the alien?
        howManyEyes = int(input("How many eyes did the alien have? -> ")) # How many eyes did you see on the alien?
        if howManyAntennae == 0 and howManyEyes == 0: # If all conditions are = 0, program ends.
            print("You didn't spot an alien then.")
        else:
            if howManyAntennae >= 1 and howManyAntennae <= 3: # Dalek species checker
                if howManyEyes > 0 and howManyEyes <= 4:
                    print("The species of alien you spotted was Dalek.")
            elif howManyAntennae == 1 or howManyAntennae == 2 and howManyEyes > 0 or howManyEyes <=3: # Cybermen species checker
                    print("The species of alien you spotted was Cybermen")
            if howManyAntennae >= 1 and howManyAntennae <= 7 and howManyEyes == 1 or howManyEyes == 2: # Sontaran species checker
                print("The species of alien you spotted was Sontaran")
            elif howManyAntennae > 7 or howManyEyes > 4:
                print("The alien you've identified does not currently exist in our database.")

    elif isAlien != "Yes".lower() or isAlien != "y".lower(): # If condition is not equal to "Yes", program ends.
                print("You didn't spot an alien then.")
            