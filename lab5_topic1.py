# Author: Vienne Mueller
# BannerID: 001395990 CS170 - 03
# Lab #5_topic1 

# Part I
# Ask the user to enter the lengths of three sides of a triangle
x,y,z=input("Enter 3 numbers: ").split()
x,y,z = int(x),int(y),int(z)
print(x,y,z)

# Check for "valid" lengths ...
# if valid -- compute perimeter -- else print "invalid"
if x + y > z and x + z > y and y + z > x:
    # The sum of any two sides of a triangle must be greater than the third side for it to be valid.
    perimeter = x + y + z
    print(f"The perimeter of the triangle is: {perimeter}")
else:
    print("Invalid lengths")

# Part II
# Ask the user for a one floating point number
print()
number = float(input("Enter one floating point number: "))

# Determine if the input number is positive, negative, or zero
# Respond with your determination
if number > 0:
    print("You entered a positive number!")
elif number < 0:
    print("You entered a negative number!")
else:
    print("You entered a zero!")

