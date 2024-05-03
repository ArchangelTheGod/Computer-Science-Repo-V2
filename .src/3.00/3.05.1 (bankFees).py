#Name: Archangel
#Date: 02/04/24 @13:29 EST
#File Name: 3.05.1 (bankFees).py
#Directory: .src/3.00/3.05.1 (bankFees).py
#Snapshot Ver. v1.00

#Inputs
        # Collect User integer inputs for variable(s) 'checkingbal' and 'savingsbal'
checkingbal = int(input("What is the balance of your checking account? -> "))
savingsbal = int(input("What is the balance of your savings account? -> "))
totalchecks = int(input("How many checks are you cashing? -> "))

#Constants
        # Service Charge fee of 15 cents
srvchrg = 0.15

#Processing
if checkingbal >= 1000 or savingsbal >= 1500:
    print("No serivce charge fee!")
elif checkingbal < 1000 or savingsbal < 1500:
    totalchecks = totalchecks*srvchrg
    print(f"Total service charge: ${totalchecks}")