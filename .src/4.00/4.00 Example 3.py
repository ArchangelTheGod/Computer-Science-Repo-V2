#Name: Archangel
#Date: 30/04/24 @12:20 EST
#File Name: 4.00 Example 3.py
#Directory: .src/4.00/4.00 Example 3.py
#Snapshot Ver. v1.00

#Constants
wins = 0
loses = 0

#Processing
for i in range(10):
    num = input("Result of game (W) or (L) -> ")
    if num.upper() == "W":
        wins += 1
        print("Total wins: ",wins)
    elif num.upper() == "L":
        loses += 1
        print("Total loses: ",loses)
    elif num != "W".upper() or num != "L".upper():
        print("ok")