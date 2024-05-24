#Name: Archangel
#Date: 16/05/24 @13:39 EST
#File Name: 4.04.5 (areVowels).py
#Directory: .src/4.00/4.04.5 (areVowels).py
#Snapshot Ver. v1.00

#Imports
import random

r = True
while True:
    #Processing
    nameChoice1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVXYZ")
    nameChoice2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVXYZ")
    nameChoice3 = random.choice("ABCDEFGHIJKLMNOPQRSTUVXYZ")
    vowels = random.choice("AEIOUY")

    if nameChoice1 == vowels and nameChoice2 == vowels and nameChoice3 == vowels:
        print(f"{nameChoice1} & {nameChoice2} & {nameChoice3} were generated and are vowels.")
        break
    else:
        print(f"{nameChoice1} & {nameChoice2} & {nameChoice3} were generated. They are NOT the same.")