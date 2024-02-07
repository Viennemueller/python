# Author:             Vienne Mueller
# BannerID/Section:   001395990-03
# Lab #4

# Task #1: Odd and Even Numbers

# Initialize variables
input_item = input("Enter a positive integer (or 0/negative to quit): ")

# Repeat loop based on input item NOT being zero or negative
while input_item.isdigit() and int(input_item) > 0:
    # Process data - determine if input data is odd or even
    input_number = int(input_item)
    if input_number % 2 == 0:
        print(f"{input_number} is even.")
    else:
        print(f"{input_number} is odd.")
    
    # Get next input item
    input_item = input("Enter another positive integer (or 0/negative to quit): ")

# Print a blank line before moving on to task #2
print()

# Task #2: Print pounds/kilograms table

print("Part 2: Pounds to Kilograms Conversion Table")
print("Pounds     Kilograms")
print("---------------------------------------------")

count = 5

while count <= 100:
    kilograms = count * 0.45359237
    print(f"{count:5} {kilograms:9.2f}")
    count += 5  # Increment by 5 for the next iteration
