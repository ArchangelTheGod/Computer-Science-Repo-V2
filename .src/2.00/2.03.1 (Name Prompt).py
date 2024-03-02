#Name: Archangel
#Date: 27/02/24 @09:25 EST
#File Name: 2.03.1 (Name Prompt).py
#Directory: .src/2.00/2.03.1 (Name Prompt).py
#Snapshot Ver. v1.00

# Input Prompts
nameInput = input("What is your name? => ")
ageInput = input("How old are you? (Must be an integer) => ")
addressInput = input("What is your address? => ")

# Write To
f = open("telemetry.txt", "a")
f.write("<== New Entry ==>\n")
f.write("-Name: ")
f.write(nameInput)
f.write("\n")
f.write("-Age: ")
f.write(ageInput)
f.write("\n")
f.write("-Address: ")
f.write(addressInput)
f.write("\n")
f.write("\n")
f.close()


# Structuring/Output
print("\n <== Telemetry Report ==>")
print("Your name is: ",nameInput)
print("You are aged: ",ageInput)
print("You live at: ",addressInput)