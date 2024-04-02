#Name: Archangel
#Date: 25/03/24 @08:28 EST
#File Name: 3.04.1 (ageGrouper).py
#Directory: .src/3.00/3.04.1 (ageGrouper).py
#Snapshot Ver. v1.00

#Loop
r = True
while True:
    #Input
    age = int(input("What is your age? -> "))

    #Processing
    if age < 12:
        print("You're a child")
    elif age >= 12 and age <= 19:
        print("You're a teen")
    elif age >=20 and age <= 65:
        print("You're an adult")
    elif age >= 65:
        print("You're a senior")