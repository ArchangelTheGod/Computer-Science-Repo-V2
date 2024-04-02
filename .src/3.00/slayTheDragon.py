
#Name: Archangel
#Date: 27/03/24 @10:18 EST
#File Name: slayTheDragon.py
#Directory: .src/3.00/slayTheDragon.py
#Snapshot Ver. v1.00

#Loop
r = True
while True:
    #Inputs
    shieldInfo = int(input("What is the energy percentage of the Energy Shield? -> "))
    saberInfo = int(input("What is the current energy percenatge of the Lightsaber? -> "))

    #Processing
    if saberInfo >= 90 and shieldInfo == 100:
        print("You killed the dragon!")
    elif saberInfo < 90 and shieldInfo != 100:
        print("You cannot slay the dragon, you're far too weak LOL")