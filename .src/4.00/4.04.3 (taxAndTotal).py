#Name: Archangel
#Date: 16/05/24 @12:35 EST
#File Name: 4.04.3 (taxAndTotal).py
#Directory: .src/4.00/4.04.3 (taxAndTotal).py
#Snapshot Ver. v1.00

#Imports
import random

#Inputs
price = float(input("Enter a price value. -> "))

#Processing
tax = random.randrange(10,20)
tax = tax/100
total = round(tax+price,2)

print(f"Your total: ${total}")