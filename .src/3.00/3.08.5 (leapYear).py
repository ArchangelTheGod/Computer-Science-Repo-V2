#Name: Archangel
#Date: 10/04/24 @13:54 EST
#File Name: 3.08.5 (leapYear).py
#Directory: .src/3.00/3.08.5 (leapYear).py
#Snapshot Ver. v1.00

#Loop
r = True
while True:
    #Inputs
    year = int(input("Input a year. -> "))

    #Processing
    if year % 4 == 0 and year % 400 == 0:
        print(f"{year} is a leap year.")
        if year % 100 != 0:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")