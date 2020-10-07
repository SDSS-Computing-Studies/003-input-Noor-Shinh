#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704
import math
x=input("Enter value of side 1")
y=input("Enter value of side 2")
a=int(x)
b=int(y)
result1=math.pow(a,2)+ math.pow(b,2) 
result2=math.sqrt(result1)
result3=str(result2)
response="Side 3 equals to "+ result3
print(response)
