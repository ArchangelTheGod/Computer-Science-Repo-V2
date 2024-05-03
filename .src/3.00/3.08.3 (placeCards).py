#Name: Archangel
#Date: 10/04/24 @13:20 EST
#File Name: 3.08.3 (placeCards).py
#Directory: .src/3.00/3.08.3 (placeCards).py
#Snapshot Ver. v1.00

#Inputs
name = input("What is your name? -> ")
isDoctor = input("Are you a doctor?")
isMale = input("Are you currently identifying as a male? -> ")
isFemale = input("Are you currently identifying as a female? -> ")

#Procesing & Structuring
print("\n<--(Card)-->")
if isDoctor == "yes".lower():
    doctorTitle = input("What is your Doctor Title? -> ")
    print(f"Doctor {name} {doctorTitle}")
    if isFemale == "yes".lower():
        genderTitle = "Ms. "
    elif isMale == "yes".lower():
        genderTitle = "Mr. "