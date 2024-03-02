#Name: Archangel
#Date: 01/03/24 @13:45 EST
#File Name: 2.05.5 (Divisions Work).py
#Directory: .src/2.00/2.05.5 (Divisions Work).py
#Snapshot Ver. v1.00

#Input
numberproc = int(input("Enter a digit to convert into 4. =>"))

#Calc
thousands = numberproc // 1000
hundreds = numberproc %1000 // 100
tens = numberproc %100 // 10
ones = numberproc %10 // 1
#Output
print("\n<== Results ==>")
print(f"New number: {thousands}{hundreds}{tens}{ones}")