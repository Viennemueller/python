# Author: Vienne Mueller
# BannerID: 001395990 CS170 - 03 
# Lab #5_topic2

# Ask the user to enter the x coordinate (it can be a float)
x = float(input("Enter the x coordinate: "))

# Ask the user to enter the y coordinate (it can be a float)
y = float(input("Enter the y coordinate: "))

# Check if the coordinate is at the origin
if x == 0 and y == 0:
    print("This point is on the origin")
# Check if the coordinate is on the x-axis
elif y == 0:
    print("This point is on the x-axis.")
# Check if the coordinate is on the y-axis
elif x == 0:
    print("This point is on the y-axis.")
# Check which quadrant the coordinate falls into
elif x > 0 and y > 0:
    print("This point is in Quadrant I.")
elif x < 0 and y > 0:
    print("This point is in Quadrant II.")
elif x < 0 and y < 0:
    print("TThis point is in Quadrant III.")
elif x > 0 and y < 0:
    print("This point is in Quadrant IV.")
else:
    print("Unplottable")

