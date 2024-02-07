# Author: Vienne Mueller
# ID: 001395990
# Course/Section: CS 170 – 03
# Lab 6 While

# Open the input file "fuel.py" for reading
infile = open("fuel.py", "r")

# Define fuel prices for each type
fuel_prices = {'S': 2.62, 'P': 2.36, 'R': 2.12, 'D': 2.35}

# Initialize total bills for each fuel type
total_bills = {'S': 0.00, 'P': 0.00, 'R': 0.00, 'D': 0.00}

# Print table headers
print(f"{'Fuel Type':<15}{'Gallons':<20}{'Bill':<15}")
print("----------------------------------------")

# Read and process the data lines
while True:
    fuel_type = infile.readline().strip()
    if not fuel_type:  # Check if we've reached the end of the file
        break
    fuel_amount = float(infile.readline())

    # Map abbreviations to full names
    fuel_names = {'S': 'Super Unleaded', 'P': 'Unleaded Plus', 'R': 'Regular Unleaded', 'D': 'Diesel'}

    total_bill = fuel_prices[fuel_type] * fuel_amount
    total_bills[fuel_type] += total_bill

    # Format the output to align columns and use money format
    print(f"{fuel_names[fuel_type]:<20}{fuel_amount:<15}{total_bill:0.2f}")

# Close the input file
infile.close()