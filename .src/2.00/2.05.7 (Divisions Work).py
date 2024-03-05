#Name: Archangel
#Date: 04/03/24 @12:10 EST
#File Name: 2.05.7 (Divisions Work).py
#Directory: .src/2.00/2.05.7 (Divisions Work).py
#Snapshot Ver. v1.00

#Input
numerator = int(input("Enter a number to be used as a numerator. => "))
denominator = int(input("Enter another number to be used as a denominator. => "))

#Processing
    #Mixed Fraction Calculation
mixedfrac1 = numerator//denominator
mixedfrac = round(mixedfrac1, 2)
newnumerator = numerator%denominator
    #Improper Fraction Calculation
impfrac = mixedfrac*denominator+numerator

#Output
print(f"Mixed Fraction: ({mixedfrac}){newnumerator}/{denominator}\n")
print(f"Improper Fraction: {impfrac}/{denominator}")