#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2
import math 
x=input("Enter value of a")
y=input("Enter value of b")
z=input("Enter value of c")
a=float(x)
b=float(y)
c=float(z)
result=(c-b)/a
answer=str(result)
response="x is equal to "+ answer
print(answer)
