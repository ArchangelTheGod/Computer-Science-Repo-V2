#Name: Archangel
#Date: 18/03/24 @12:48 EST
#File Name: 3.01.1.py
#Directory: .src/3.00/3.01.1.py
#Snapshot Ver. v1.00

#inputs
digit1 = int(input("Enter a number to process. => "))
digit2 = int(input("Enter another digit. => "))
digit3 = int(input("Enter one more digit. => "))

#Processing
    #digit1 Variable Processing
def d1process():
    if digit1 > 50:
        print(f"Output; {digit1} is greater than 50.")
    if digit1 != 12:
        print(f"Output; {digit1} is anything OTHER than 12")
    if digit1 > 10:
        print(f"Output; {digit1} is HIGHER than 10")
    elif digit1 < 10:
        print(f"Output; {digit1} is LESSER than 10.")
    elif digit1 == 10:
        print(f"Output; {digit1} is EQUAL to 10")
    print("\n")

    #digit2 Variable Processing
def d2process():
    if digit2 > 50:
        print(f"Output; {digit2} is greater than 50.")
    if digit2 != 12:
        print(f"Output; {digit2} is anything OTHER than 12")
    if digit2 > 10:
        print(f"Output; {digit2} is HIGHER than 10")
    elif digit2 < 10:
        print(f"Output; {digit2} is LESSER than 10.")
    elif digit2 == 10:
        print(f"Output; {digit2} is EQUAL to 10")
    print("\n")

    #digit3 Variable Processing
def d3process():
    if digit3 > 50:
        print(f"Output; {digit3} is greater than 50.")
    if digit3 != 12:
        print(f"Output; {digit3} is anything OTHER than 12")
    if digit3 > 10:
        print(f"Output; {digit3} is HIGHER than 10")
    elif digit3 < 10:
        print(f"Output; {digit3} is LESSER than 10.")
    elif digit3 == 10:
        print(f"Output; {digit3} is EQUAL to 10")
    print("\n")

#Outputs
print("\n<== Results ==>")
d1process()
d2process()
d3process()