# Author: Vienne Mueller
# ID: 001395990
# Course/Section: CS 170 – 03
# Lab 6

# Open the input file "fuel.py" for reading
infile = open("fuel.py")

# Define fuel prices for each type
fuel_prices = {'S': 2.62, 'P': 2.36, 'R': 2.12, 'D': 2.35}
print()
# Print table headers
print(f"{'Fuel Type':<15}{'Gallons':<15}{'Bill':<15}")
print("----------------------------------------")

# Read and process the data lines
for i in range(15):
    fuel_type = infile.readline().strip()
    fuel_amount = float(infile.readline())

    # Map abbreviations to full names
    fuel_names = {'S': 'Super Unleaded', 'P': 'Unleaded Plus', 'R': 'Regular Unleaded', 'D': 'Diesel'}

    total_bill = fuel_prices[fuel_type] * fuel_amount

    # Format the output to align columns and use money format
    print(f"{fuel_names[fuel_type]:<20}{fuel_amount:0.2f}{' ' * 5}{total_bill:0.2f}")

# Close the input file
infile.close()