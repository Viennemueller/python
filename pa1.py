# Author: Vienne Mueller
# BannerID: 001395990
# Course/Section: CS170 - 03
# Assignment: PA1
# Date Assigned: Wednesday, August 23, 2023
# Date/Time Due: Thursday, August 31, 2023 
# Description: This program will determine vehicle fuel mileage and cost of a automobile trip.
# Certification of Authenticity: I certify that this assignment is entirely my own work.
#Sources: https://www.w3schools.com/python/ref_func_float.asp

# input statements
carType = input("Enter your car type: ")
fuelTankSize = input("Enter the fuel tank size: ")
milesPerTank = input("Enter the number of miles you can drive on one tank: ")
cost = input("Enter the cost for fuel: ")

# vehicle fuel mileage (miles per tank / tank size)
mpg = float(milesPerTank) / float(fuelTankSize)

# total cost of a trip (milesPerTank / mpg * cost)
totalCost = (float(milesPerTank) / mpg) * float(cost)

# print outputs
print("While driving a", carType, "with a tank that can hold", fuelTankSize, "gallons, you can drive",milesPerTank, "miles. The cost of fuel is", cost, "per gallon.")
#put in dollar format
print("For the trip, the total cost will be $", format(totalCost, ".2f"))
print("Your vehicle's fuel mileage is:", mpg, "miles per gallon.")
