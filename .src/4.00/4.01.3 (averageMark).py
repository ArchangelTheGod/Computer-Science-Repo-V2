#Name: Archangel
#Date: 07/05/24 @12:13 EST
#File Name: 4.01.3 (averageMark).py
#Directory: .src/4.00/4.01.3 (averageMark).py
#Snapshot Ver. v1.00

#Constants
total = 0
#Inputs/Loop
toMark = int(input("How many marks are being entered? (5 max) -> "))

for i in range(toMark):
    grade = float(input("Enter a mark -> "))

    if grade <= 0 or grade > 100:
        print("Your mark(s) aren't between 0 and 100")
        break
    elif grade >= 0 or grade <= 100:
        total += grade

#Processing
avg = round(total/toMark,2)
print(f"\n{avg}%")