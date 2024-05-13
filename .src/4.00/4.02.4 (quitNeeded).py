#Name: Archangel
#Date: 09/05/24 @13:00 EST
#File Name: 4.02.4 (quitNeeded).py
#Directory: .src/4.00/4.02.4 (quitNeeded).py
#Snapshot Ver. v1.00

#Constants
string = ""

#Input/Processing/loop
while string != "quit".lower():
    string = input("Ok. ")
    if string == "quit".lower():
        print("Goodbye")
        break
    elif string != 'quit'.lower():
            print(f"{string}")