#Name: Archangel
#Date: 25/03/24 @09:35 EST
#File Name: 3.04.5 (payCalc).py
#Directory: .src/3.00/3.04.5 (payCalc).py
#Snapshot Ver. v1.00

#Inputs
ot = int(input("How many hours did you work Over Time? -> "))

#Constants
firstPay = 12.00*40
totalOt = 15.00*ot
totalOt = totalOt + firstPay

#Processing
if ot == 0:
    print(f"You made ${firstPay}")
elif ot != 0:
    print(f"You made ${totalOt} with {ot} hours of Over Time.")