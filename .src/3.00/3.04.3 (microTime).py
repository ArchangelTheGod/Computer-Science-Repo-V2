#Name: Archangel
#Date: 25/03/24 @08:35 EST
#File Name: 3.04.3 (microTime).py
#Directory: .src/3.00/3.04.3 (microTime).py
#Snapshot Ver. v1.00

#Loop
r = True
while True:        
    #Input
    items = int(input("How many items are you heating? => "))
    heatingVal = int(input("What is the default heating time for 1 item? => "))

    #Processing
    if items == 1:
        print(f"\nHeating time should be {heatingVal} minute(s) for {items} item(s).")
    elif items == 2:
        heatingValSecs = 30
        print(f"\nHeating time should be {heatingVal}.{heatingValSecs} for {items} item(s).")
    elif items == 3:
        heatingVal = heatingVal*2
        print("\n[WARNING] HEATING 3 ITEMS AT ONCE IS NOT RECOMMENDED. PROCEED WITH CAUTION")
        print(f"Heating time should be {heatingVal} minute(s) for {items} item(s).")
    elif items > 3:
        print("\nYOU'RE INSANE.")