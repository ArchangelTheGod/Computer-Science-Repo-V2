#Name: Archangel
#Date: 09/04/24 @12:55 EST
#File Name: 3.07.1 (nestedIfs1).py
#Directory: .src/3.00/3.07.1 (nestedIfs1).py
#Snapshot Ver. v1.00

#1
    #A: 1 is more efficient

#2
def les1():
        #Loop
    r = True
    while True:
            #Inputs
        temperature  = int(input("Enter a number. -> "))

            #Constants
        max_temp = 100

            #Processing
        if (temperature >= max_temp):
            print("The Porridge is TOO HOT.")
        elif (temperature <= max_temp) and (temperature > 0) and (temperature < 10):
                print("The Porridge is at OPTIMAL TEMPERATURE.")
        elif (temperature != max_temp) and (temperature <= 0):
                print("The Porridge is too cold")

#3
    #A: Will print "Reject".
    #B: Will not print anything. 

#4:
    #This code is checking if the letter is any of the vowels; A,E,I,O,U (and sometimes Y). If it's not any of these letters, it's a consonant.