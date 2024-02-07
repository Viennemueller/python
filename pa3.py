# Author: Vienne Mueller
# ID: 001395990
# Course/Section: CS 170 – 03
# Assignment: Pa3
# Date Assigned: Saturday, September 23, 2023
# Date/Time Due: Thursday, October 5, 2023 –- 11:55 pm
# Description: This program will process an input file, keeping counts & sums
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.

# Store regional populations
region_populations = {"NW": 0, "SW": 0, "NE": 0, "SE": 0}
total_population = 0

# Open"states.py"
try:
    with open("states.py", "r") as file:
        print("{:<9} {:<20} {:<10}".format("Region", "State", "Population"))
        print("---------------------------------------------------------")

        # Initialize variables to store data
        region = None
        state = None
        population = None

        for line in file:
            line = line.strip()

            # Check if the line contains data
            if line:
                if region is None:
                    region = line
                elif state is None:
                    state = line
                else:
                    # This is the population line
                    population = int(line)
                    
                    # Print table
                    print("{:<9} {:<20} {:<10}".format(region, state, population))
                    
                    # Update total population and regional subtotals
                    total_population += population
                    region_populations[region] += population
                    
                    # Reset variables for the next set of data
                    region = None
                    state = None
                    population = None

        print("---------------------------------------------------------")
        print(f"Total Population: {total_population}")
        print()
        
        # Print regional subtotals
        for region, subtotal in region_populations.items():
            print(f"{region} Subtotal: {subtotal}")
except FileNotFoundError:
    print("Error: File 'states.py' not found.")
