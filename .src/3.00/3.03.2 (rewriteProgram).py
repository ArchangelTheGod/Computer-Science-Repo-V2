#Name: Archangel
#Date: 21/03/24 @12:38 EST
#File Name: 3.03.2 (rewriteProgram).py
#Directory: .src/3.00/3.03.2 (rewriteProgram).py
#Snapshot Ver. v1.00

#Inputs
wings = int(input("How many points did the wings score? => "))
badGuys = int(input("How many points did the Leafs score? => "))

#Processing
if wings > badGuys:
    print("The Wings won.")
elif wings < badGuys:
    print("Leafs won.")
elif wings == badGuys:
    print("Score is tied.")