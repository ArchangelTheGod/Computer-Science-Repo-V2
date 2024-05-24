#Name: Archangel
#Date: 16/05/24 @13:51 EST
#File Name: 4.04.6 (20Flips).py
#Directory: .src/4.00/4.04.6 (20Flips).py
#Snapshot Ver. v1.00

#Imports
import random

#Contants/loop
coinFlips = 0
heads = 0
tails = 0
prevFlip = 0
seqChange = -1
streak = 1
longStreak = 0
while coinFlips < 20:
    coin = random.randrange(1,3)
    if coin == 1:
        coinFace = "heads"
        heads += 1
    elif coin == 2:
        coinFace = "tails"
        tails += 1
    coinFlips += 1
    if coin == prevFlip:
        streak += 1
    else:
        streak = 1
        seqChange += 1
    if streak >longStreak:
        longStreak = streak
    prevFlip = coin
    
    # if heads > tails:
    #     coinCount = 1
    # elif heads != tails :
    #     coinCount =+ 1
    print(f"Coin toss results: You got {coinFace} || Flips: {coinFlips}/20")

print(f"Total times landed on heads: {heads}")
print(f"Total times landed on tails: {tails}")
print(f"Consecutive coin count (Highest) {longStreak} || (How many times) {seqChange}")