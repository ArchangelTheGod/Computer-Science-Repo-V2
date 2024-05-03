#Name: Archangel
#Date: 02/04/24 @13:39 EST
#File Name: 3.05.2 (pumpingTires).py
#Directory: .src/3.00/3.05.2 (pumpingTires).py
#Snapshot Ver. v1.00

#Loop
r = True
while True:
    #Inputs
            # Collect user integer inputs for variable(s) 'tire1', 'tire2', 'tire3', 'tire4'
    tire1 = int(input("What is the pressure of the first tire? -> "))
    tire2 = int(input("What is the pressure of the second tire? -> "))
    tire3 = int(input("what is the pressure of the third tire? -> "))
    tire4 = int(input("What is the pressure of the fourth tire? -> "))

    #Processing
    if tire1 <= 20 and tire2 <= 20: # If tire1 AND tire2 is less than or equal to 20
        frontTiresConfirm = True # Confirms the completion of the first process
        if True:
            if tire3 <= 20 and tire4 <= 20: # If tire3 AND tire4 are less than or equal to 20
                backTiresfalse = True # Confirms the completion of the second process
                if True:
                    print("You tires' pressure is too low. The minimum you can drive with is 20 PSI.")
    elif tire1 == tire2 and tire3 == tire4:
        print("Your tires are good!")