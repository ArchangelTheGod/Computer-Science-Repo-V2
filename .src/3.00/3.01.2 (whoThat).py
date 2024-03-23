#Name: Archangel
#Date: 19/03/24 @08:27 EST
#File Name: 3.01.2 (whoThat).py
#Directory: .src/3.00/3.01.2 (whoThat).py
#Snapshot Ver. v1.00

#Loop
r = True
while True:
    #Input
    name = input("What is your name? => ")

    #Processing
    if name == "Azel".lower():
        output = "Hello, Azel!"
    elif name != "Azel".lower():
        output = f"Hello, {name}!"

    #Output
    print("\n<== Results ==>")
    print(output)