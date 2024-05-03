#Name: Archangel
#Date: 10/04/24 @13:18 EST
#File Name: 3.08.2 (biggestInteger).py
#Directory: .src/3.00/3.08.2 (biggestInteger).py
#Snapshot Ver. v1.00

#Loop
r = True
while True:
    #Inputs
    integer1 = int(input("Enter a number. -> "))
    integer2 = int(input("Enter another number. -> "))
    integer3 = int(input("Enter another number. -> "))

    #Processing
    if integer1 > integer2 and integer1 > integer3:
        print(f"Integer 1 ({integer1}) is greater than Integer 2 and 3.")
    elif integer2 > integer1 and integer2 > integer3:
        print(f"Integer 2 ({integer2}) is greater than Interger 1 and 3.")
    elif integer3 > integer1 and integer3 > integer2:
        print(f"Integer 3 ({integer3}) is greater than Integer 1 and 2")