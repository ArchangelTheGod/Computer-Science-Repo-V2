#Name: Archangel
#Date: 25/03/24 @08:55 EST
#File Name: 3.04.4 (quadSolver).py
#Directory: .src/3.00/3.04.4 (quadSolver).py
#Snapshot Ver. v1.00

#Imports
import cmath

aCoeff = int(input("Enter the first coefficient. => "))
bCoeff = int(input("Enter the second coefficient. => ")) 
cCoeff = int(input("Enter the third coefficient. => "))

#Calc
dis = (bCoeff**2) - (4 * aCoeff*cCoeff)

#Roots
ans1 = (-bCoeff-cmath.sqrt(dis))/(2 * aCoeff)
ans2 = (-cCoeff + cmath.sqrt(dis))/(2 * aCoeff)

#Results
print('The roots are')
print(ans1)
print(ans2)


# NOTICE; CODE IS NOT MY OWN- KUDOOS TO https://www.geeksforgeeks.org/python-program-to-solve-quadratic-equation/