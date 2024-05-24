#Name: Archangel
#Date: 16/05/24 @12:51 EST
#File Name: 4.04.4 (randomLetters).py
#Directory: .src/4.00/4.04.4 (randomLetters).py
#Snapshot Ver. v1.00

#Imports
import random

r = True
while True:
    #Processing
    nameChoice1 = random.choice("AZEL")
    nameChoice2 = random.choice("AZEL")

    if nameChoice1 == nameChoice2:
        print(f"{nameChoice1} & {nameChoice2} were generated and are the same.")
        break
    else:
        print(f"{nameChoice1} & {nameChoice2} were generated. They are NOT the same.")
