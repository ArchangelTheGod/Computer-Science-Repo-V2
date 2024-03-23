#Name: Archangel
#Date: 19/03/24 @09:22 EST
#File Name: 3.01.6 (readyToDrive).py
#Directory: .src/3.00/3.01.6 (readyToDrive).py
#Snapshot Ver. v1.00

#Input
age = int(input("Please state an age to check that you're qualified to drive. => "))

#Constants
legalAge = 16
#Processing
if age < legalAge and age > 10:
    print(f"You are not yet old enough to drive. The minimum age is {legalAge}. You are: {age}.")
elif age > legalAge or age == legalAge:
    print(f"You are old enough to drive! You've passed the minimum age; {legalAge} - You are {age}.")
elif age < legalAge and age < 10:
    print(f"You are FAR too young to drive! The minimum age is {legalAge}. You are: {age}.")