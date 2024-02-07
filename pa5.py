# pa5.py -- Fall 2023
# Author: Vienne Mueller
# ID: 001395990
# Course/Section: CS 170 – 03
# Assignment: Pa4
# Date Assigned: Thursday, October 5, 2023
# Date/Time Due: Thursday, October 19, 2023 –- 11:55 pm
#
# Description: This program will process a file of data using functions.
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.


# Check if the password length is greater than or equal to 8
def CheckLength(passwd):
    return len(passwd) >= 8

# Check if the password has both uppercase and lowercase letters
def CheckCases(passwd):
    return any(c.isupper() for c in passwd) and any(c.islower() for c in passwd)

# Check if the password has at least one digit
def CheckDigit(passwd):
    return any(c.isdigit() for c in passwd)

def main():
    infile = open("passwords.py", "r")

    passwd = infile.readline().strip()

    print("Password            Result")
    print("------------------------------")

    while passwd != "DONE":
        # Call the functions and send the password as an argument
        check1 = CheckLength(passwd)
        check2 = CheckCases(passwd)
        check3 = CheckDigit(passwd)

        # Check password strength based on the individual checks
        result = "Strong" if check1 and check2 and check3 else "Weak"
        
        # Print the password and result in a formatted manner
        print(f"{passwd.ljust(20)} {result}")

        passwd = infile.readline().strip()

    infile.close()

main()
