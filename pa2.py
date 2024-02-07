# Author: Vienne Mueller
# BannerID: 001395990
# Course/Section: CS170 - 03
# Assignment: PA2
# Date Assigned: Tuesday, September 5, 2023
# Date/Time Due: Thursday, September 14, 2023
# Description: This program will determine vehicle fuel mileage and print a formatted table of output
# Certification of Authenticity: I certify that this assignment is entirely my own work.

# Initialize variables to store information about the vehicles with the highest and lowest mileage
highest_mileage_vehicle = ""
lowest_mileage_vehicle = ""
longest_name_vehicle = ""

# Initialize variables to store information about the highest and lowest mileage values
highest_mileage = 0
lowest_mileage = float('inf')

#Ask the user for the three (03) types of cars.
car1 = input("Enter the first car type: ")
car2 = input("Enter the second car type: ")
car3 = input("Enter the third car type: ")

# Ask the user for the number of gallons of fuel for each vehicle.
fuelTankSize1 = float(input(f"Enter the fuel tank size for {car1} (in gallons): "))
fuelTankSize2 = float(input(f"Enter the fuel tank size for {car2} (in gallons): "))
fuelTankSize3 = float(input(f"Enter the fuel tank size for {car3} (in gallons): "))

# Ask the user how many miles each vehicle can drive on one tank of fuel
milesPerTank1 = float(input(f"Enter the number of miles {car1} can drive on one tank: "))
milesPerTank2 = float(input(f"Enter the number of miles {car2} can drive on one tank: "))
milesPerTank3 = float(input(f"Enter the number of miles {car3} can drive on one tank: "))

# Determine vehicle fuel mileage for each car (miles per gallon)
mpg1 = milesPerTank1 / fuelTankSize1
mpg2 = milesPerTank2 / fuelTankSize2
mpg3 = milesPerTank3 / fuelTankSize3

# Check for the vehicle with the highest mileage
if mpg1 > highest_mileage:
    highest_mileage = mpg1
    highest_mileage_vehicle = car1

if mpg2 > highest_mileage:
    highest_mileage = mpg2
    highest_mileage_vehicle = car2

if mpg3 > highest_mileage:
    highest_mileage = mpg3
    highest_mileage_vehicle = car3

# Check for the vehicle with the lowest mileage
if mpg1 < lowest_mileage:
    lowest_mileage = mpg1
    lowest_mileage_vehicle = car1

if mpg2 < lowest_mileage:
    lowest_mileage = mpg2
    lowest_mileage_vehicle = car2

if mpg3 < lowest_mileage:
    lowest_mileage = mpg3
    lowest_mileage_vehicle = car3

# Check for the vehicle with the longest name
if len(car1) > len(longest_name_vehicle):
    longest_name_vehicle = car1

if len(car2) > len(longest_name_vehicle):
    longest_name_vehicle = car2

if len(car3) > len(longest_name_vehicle):
    longest_name_vehicle = car3


# Print the table header.
print("\n{:<20} {:<5} {:<6} {:<5}".format("Car Name", "Tank Size", "Tank Distance", "MPG"))

# Print the information for each car in the table.
print("{:<20} {:<5.2f} {:<6.2f} {:<5.2f}".format(car1, fuelTankSize1, milesPerTank1, mpg1))
print("{:<20} {:<5.2f} {:<6.2f} {:<5.2f}".format(car2, fuelTankSize2, milesPerTank2, mpg2))
print("{:<20} {:<5.2f} {:<6.2f} {:<5.2f}".format(car3, fuelTankSize3, milesPerTank3, mpg3))

# Print vehicle names for the highest and lowest mileage.
print(f"The vehicle with the highest mileage is {highest_mileage_vehicle} with {highest_mileage:.2f} miles per gallon.")
print(f"The vehicle with the lowest mileage is {lowest_mileage_vehicle} with {lowest_mileage:.2f} miles per gallon.")

# Print the vehicle name which has the longest name.
print(f"The vehicle with the longest name is {longest_name_vehicle}.")
