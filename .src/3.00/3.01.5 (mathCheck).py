#Name: Archangel
#Date: 19/03/24 @08:50 EST
#File Name: 3.01.5 (mathCheck).py
#Directory: .src/3.00/3.01.5 (mathCheck).py
#Snapshot Ver. v1.00

#Input
q1 = int(input("What is 9999 + 1? => "))
q2 = int(input("What is 9786754 x 4657? => "))
q3 = int(input("What is the square-root of 9876564? => "))

#Constants
ans1 = "10,000"
ans2 = "45,576,913,378"
ans3 = "3,143"

#Processing
    #text structuring
print("\n<== Results ==>")
    #Answer Checking
if q1 != 10000:
    print(f"[Q1] Wrong, the correct answer was {ans1}.")
    print(f"Your answer was: {q1}\n")
elif q1 == 10000:
    print(f"[Q1] Correct! The answer IS {ans1}!")
    print(f"Your answer was: {q1}\n")

if q2 != 45576913378:
    print(f"[Q2] Wrong, the correct answer was {ans2}.")
    print(f"Your answer was: {q2}\n")
elif q2 == 45576913378:
    print(f"[Q2] Correct! The answer IS {ans2}!")
    print(f"Your answer was: {q2}\n")

if q3 != 3143:
    print(f"[Q3] Wrong, the correct answer was {ans3}.")
    print(f"Your answer was: {q3}\n")
elif q3 == 3143:
    print(f"[Q3] Correct! The answer IS {ans3}!")
    print(f"Your answer was: {q3}\n")