# lab3.py
# Author:             Vienne Mueller
# BannerID/Section:   001395990-03
# Do you Respond to the doodle link: Yes

# Print a couple of blank lines before the program begins
print()
print()

# Ask the user for the radius of the pizza (in inches)
radius = float(input("Enter the radius of the pizza (in inches): "))
# Compute the area of the pizza (in square inches) using math.pi
import math  # Import the math module
pizza_area = math.pi * (radius ** 2)

# Ask the user for the price of the pizza
price = float(input("Enter the price of the pizza: "))
# Compute the price of the pizza per square inch
price_per_square_inch = price / pizza_area

# Print out the price of the pizza per square inch NOT rounded
print(f"Price per square inch: {price_per_square_inch}")
# Then print out the price, rounded to 2 decimal places
print(f"Price (rounded to 2 decimal places): {price_per_square_inch:.2f}")

# If the price per square inch of the pizza is higher than $0.02, then print Costly Pizza.
# If the price per square inch of the pizza is less than $0.01, then print Pizza price is Cheap.
# Otherwise, print pizza price is standard.
if price_per_square_inch > 0.02:
    print("Costly Pizza")
elif price_per_square_inch < 0.01:
    print("Pizza price is Cheap")
else:
    print("Pizza price is standard")

# Print a couple of blank lines before the next section of code begins
print()
print()

# Ask the user to enter a 3-letter word
# You are allowed only ONE input statement
threeWord = input("Enter a 3-letter threeWord: ")
# Check if it's an acceptable length and contains ONLY letters A through Z or spaces
# Print the ASCII code (a number) for each letter of the word just input
# You can use the ord() function to convert a character to an integer (ASCII value)
# like count1 = ord(word[0]) to find the ASCII value of the 1st input letter in the variable word
if len(threeWord) == 3:
    ascii_values = [ord(letter) for letter in threeWord]
    print("ASCII values for the letters in the word:")
    for i in range(3):
        print(f"Letter {threeWord[i]}: {ascii_values[i]}")
else:
    print("Please enter a 3-letter word.")

# Print a couple of blank lines when the program is done
print()
print()
