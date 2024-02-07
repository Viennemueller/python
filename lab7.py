# Author: Vienne Mueller
# BannerID/Section: 001395990-03
# lab7.py

# LAB Average
def labAvg(infile):
    g1 = float(infile.readline())
    g2 = float(infile.readline())
    g3 = float(infile.readline())
    g4 = float(infile.readline())
    g5 = float(infile.readline())
    g6 = float(infile.readline())
    g7 = float(infile.readline())

    print("Lab Grades:", g1, g2, g3, g4, g5, g6, g7)

    sum_lab = g1 + g2 + g3 + g4 + g5 + g6 + g7
    avg_lab = sum_lab / 7  # computes average
    avg_lab = avg_lab / 10  # computes % (because labs are worth 10 points)

    return avg_lab

# PA Average
def paAvg(infile):
    # Read PA grades from the file and compute the average
    pa1 = float(infile.readline())
    pa2 = float(infile.readline())
    pa3 = float(infile.readline())

    print("PA Grades:", pa1, pa2, pa3)

    sum_pa = pa1 + pa2 + pa3
    avg_pa = sum_pa / 3  # computes average
    avg_pa = avg_pa / 10  # computes % (assuming PAs are worth 10 points)

    return avg_pa

# EXAM Average
def examAvg(infile):
    # Read exam grade from the file
    exam = float(infile.readline())

    print("Exam Grade:", exam)

    exam = exam / 100  # converts exam score to a percentage

    return exam

# MAIN/DRIVER 
def main():
    # main will call each of your average functions
    # to compute each component of the overall class average
    # call the function to compute your LAB average
    # put the return value in the variable labAverage

    infile = open("lab7_grades.py", 'r')
    labAverage = labAvg(infile)

    # call the function to compute your PA average
    paAverage = paAvg(infile)

    # call the function to compute your EXAM average
    examAverage = examAvg(infile)

    # close the file
    infile.close()

    # compute your OVERALL class average using the weights
    # provided on the lab instruction sheet
    overallAverage = (labAverage * 10 ) + (paAverage * 1.5) + (examAverage * 75)

    # print results
    print("  Lab Average =", labAverage * 100, "%")
    print("   PA Average = {:.2f}%".format(paAverage * 10))
    print(" Exam Average =", examAverage * 100, "%")
    print("---------------")
    print(f"Class Average = {overallAverage:.2f}%")

# Call the main function to run the program
if __name__ == "__main__":
    main()
