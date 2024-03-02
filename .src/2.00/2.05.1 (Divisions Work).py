#Name: Archangel
#Date: 01/03/24 @13:10 EST
#File Name: 2.05.1 (Divisions Work).py
#Directory: .src/2.00/2.05.1 (Divisions Work).py
#Snapshot Ver. v1.00

#Loop
run = True
while run:
    #Input
    int1 = int(input("Enter a digit here. => "))
    int2 = int(input("Enter another digit here. => "))

    #0 Blocker
    if int1 or int2 == 0:
        run = False
        print("\n  Error! Number cannot be a 0")
        print("Program terminated.")
    else:
        #Calculate
        output = int1//int2

        #Output
        print("\n<== Results ==>")
        print(f"Answer is: {output}")

        #Confirm exit
        exitprompt = input("Exit program? type Y or N to confirm => ")
        if exitprompt == "y".lower():
            run = False
        elif exitprompt == "n".lower():
            run = True