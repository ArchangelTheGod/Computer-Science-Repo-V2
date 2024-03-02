#Name: Archangel
#Date: 01/03/24 @13:37 EST
#File Name: 2.05.3 (Divisions Work).py
#Directory: .src/2.00/2.05.3 (Divisions Work).py
#Snapshot Ver. v1.00

#Input
nume = int(input("Insert the numerator of your fraction. => "))
denom = int(input("Enter the denomenator of your fraction. => "))

#Calc
wholefrac = nume//denom
newnume = nume%denom

#Output
print("\n<== Results ==>")
print(f"Mixed fraction converted to: ({wholefrac}){newnume}/{denom}")