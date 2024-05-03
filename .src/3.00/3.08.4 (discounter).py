#Name: Archangel
#Date: 10/04/24 @13:43 EST
#File Name: 3.08.4 (discounter).py
#Directory: .src/3.00/3.08.4 (discounter).py
#Snapshot Ver. v1.00

#Inputs
tvType = input("What type of TV are you buying; LCD or Plasma? -> ")
price = int(input("what is the price of the TV? -> "))

#Processing
if tvType == "lcd".lower():
    price = 5%price
    print(f"Your TV will be 5% off; {price}")
elif tvType == "plasma".lower():
    tvSize = int(input("What size is the TV? (30\" or 42\"?)"))
    if tvSize == 30:
        price = 8%price
        print(f"Your 30\" TV will be 8% off; {price}")
    elif tvSize == 42:
        price = 10%price
        print(f"Your 42\" TV will be 10% off; {price}")