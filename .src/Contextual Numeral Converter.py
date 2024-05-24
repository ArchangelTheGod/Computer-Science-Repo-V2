# Decimal to Binary Conversion
def d2b():
    r = True
    while True:
        dec_num = int(input("Enter an integer:  "))
        bin_num = bin(dec_num).replace("0b","")
        print(bin_num)

# Binary to Decimal Conversion
def b2d():
    r = True
    while True:
        bin_num = input("Enter a binary number:  ")
        dec_num = int(bin_num, 2)
        print(dec_num)

# # Decimal to Hexadecimal Conversion
def d2hx():
    r = True
    while True:
        dec_num = int(input("Please enter an integer:  "))
        hex_num = hex(dec_num)
        print(hex_num)

# # Hexadecimal to Decimal Conversion
def hx2d():
    r = True
    while True:
        hex_num = input("Enter a hex number:  ")
        dec_num = int(hex_num, 16)
        print(dec_num)

#Processing
# d2b()
# b2d()
# d2hx()
# hx2d()