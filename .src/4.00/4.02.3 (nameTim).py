#Name: Archangel
#Date: 09/05/24 @13:50 EST
#File Name: 4.02.3 (nameTim).py
#Directory: .src/4.00/4.02.3 (nameTim).py
#Snapshot Ver. v1.00

#Constants
name = ""

#Input/Processing/loop
while name != "tim".lower():
    name = input("What is your name? -> ")
    if name == "tim".lower():
        print("Tim!")
        break
    elif name != 'tim'.lower():
            print("You're not tim!")