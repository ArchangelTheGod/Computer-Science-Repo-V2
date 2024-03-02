#Name: Archangel
#Date: 29/02/24 @12:50 EST
#File Name: 2.04.7 (Mathematical Equations).py
#Directory: .src/2.00/2.04.7 (Mathermatical Equations).py
#Snapshot Ver. v1.00

#Inputs/"Handshake"
name = input("Please Specify Your Name ->")
age =  int(input("Please Specify Your Age ->"))
currentYear = int(input("Please Sepcify The Current Year ->"))

#Calculations
yn25 = 25-age
y25 = currentYear+yn25

yn50 = 50-age
y50 = currentYear+yn50

yn75 = 75-age
y75 =  currentYear+yn75

yn100 = 100-age
y100 = currentYear+yn100

#Greeting
print("Greetings,", name, "!")
print("*"*10)
print("You'll be aged 25 at the year", y25)
print("That'll be in:", yn25)

print("You'll be aged 50 at the year", y50)
print("That'll be in:", yn50)

print("You'll be aged 75 at the year", y75)
print("That'll be in:", yn75)

print("You'll be aged 100 at the year", y100)
print("That'll be in:", yn100)


print("-- Hey There! --")