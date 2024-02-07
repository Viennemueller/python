# Author:       Vienne Mueller
# ID/Section:   001395990-03

# Print 2 blank lines
print()
print()

# Part I of this lab is simply using input statements and
# arithmetic expressions 
# Ask the user to input hours and hourly rate, then compute gross pay
# First, complete the following input statements 
hours = float(input("Enter hours worked: "))  # Get user input for hours worked
rate = float(input("Enter hourly rate: "))    # Get user input for hourly rate

# Write an equation to compute gross pay using the variables above hours and rate
grossPay = hours * rate

# Print 1 blank line
print()

# Print out hours, rate, and gross pay that you just computed 
print("Hours =", hours)
print("Rate =", rate)
print("Gross Pay =", grossPay)

# ------------------------------------------------------------------
# Part II of this lab will use the math library, which means it must
# be imported

import math
# Print sin/cos/tan for the "common" angles of 30, 45 & 90 degrees
# Remember, sometimes one of these trig functions is undefined 
print()
print("Angle         Sine       Cosine     Tangent")
print("-------------------------------------------") 

# Convert degrees to radians: # use pi/180 * degree. 
# For pi use math.pi 
degree1 = 30
radian1 = math.radians(degree1)  # Convert degree to radian for degree1
degree2 = 45
radian2 = math.radians(degree2)   # Convert degree to radian for degree2
degree3 = 90
radian3 = math.radians(degree3)   # Convert degree to radian for degree3

# There are NO errors in the following PRETTY print statements

pretty = "{0:6}  {1:10.3f}  {2:10.3f}  {3:10.3f}"
print(pretty.format(degree1, math.sin(radian1), math.cos(radian1), math.tan(radian1)))
print(pretty.format(degree2, math.sin(radian2), math.cos(radian2), math.tan(radian2)))
print(pretty.format(degree3, math.sin(radian3), math.cos(radian3), math.tan(radian3)))
