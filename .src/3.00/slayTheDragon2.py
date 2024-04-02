
#Name: Archangel
#Date: 27/03/24 @10:25 EST
#File Name: slayTheDragon2.py
#Directory: .src/3.00/slayTheDragon2.py
#Snapshot Ver. v1.00

#Inputs
shieldInfo = int(input("What is the energy charge of the shield? -> "))
saberInfo = int(input("What is the energy charge of the Lightsaber? -> "))

#Processing
if shieldInfo != 100 and saberInfo != 90:
    print("You can't attack the dragon, you're far too weak LOL")
elif shieldInfo > 99 and shieldInfo < 101 and saberInfo > 89 and saberInfo < 91:
    print("You can kill the dragon!")