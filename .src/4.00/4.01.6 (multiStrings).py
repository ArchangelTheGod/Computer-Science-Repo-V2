#Name: Archangel
#Date: 09/05/24 @12:24 EST
#File Name: 4.01.6 (multiStrings).py
#Directory: .src/4.00/4.01.6 (multiStrings).py
#Snapshot Ver. v1.00

#Processing
def HIBRO():
    print("HELLO"*3)

def fiftyX():
    print("x"*50)

def rectangle():
    #Inputs
    m = int(input("Enter a number. -> "))
    n = int(input("Enter a numebr. -> "))

    #Processing
    for i in range(n):
        print(""*n+"*"*m)

rectangle()