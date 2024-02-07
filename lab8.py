# Author    : Vienne Mueller
# ID/Section: 001395990 CS170 - 03

#****************** LAB Average  ******************
def LabAvg(infile1, num):
    print("Lab Grades: ", end='')
    lab8 = []  # create a list for lab grades

    # Append the lab grades from the lab8_labGrades.py
    # Create a list for lab grades
    for i in range(num):
        grade = eval(infile1.readline())
        lab8.append(grade)

    if num > 0:
        # computes sum of all lab grades (number between 1 & 10, because labs are 10 pts)
        sumOfLabs = sum(lab8)
        # computes avg (number between 1 & 10, because labs are 10 pts)
        avgLabs = sumOfLabs / num
    else:
        avgLabs = 0

    return avgLabs  # return the lab average

#****************** PA Average  ******************
def PaAvg(infile2, num):
    print("PA Grades: ", end='')
    paGrade = []  # create a list for PA grades

    # Append the PA grades from the lab8_paGrades.py
    # Create a list for PA grades
    for i in range(num):
        grade = eval(infile2.readline())
        paGrade.append(grade)

    if num > 0:
        # computes sum of all PA grades (number between 1 & 100, because PAs are 100 pts)
        sumOfPA = sum(paGrade)
        # computes avg (number between 1 & 100, because PAs are 100 pts)
        avgPA = sumOfPA / num
    else:
        avgPA = 0

    return avgPA   # return the PA average

#****************** EXAM Average  ******************
def ExamAvg(infile3, num):
    print("Exam Grades: ", end='')
    examGrades = []  # create a list for exams

    # Append the exam grades from the lab8_examGrades.py
    # Create a list for exam grades
    for i in range(num):
        grade = eval(infile3.readline())
        examGrades.append(grade)

    if num > 0:
        # computes sum of all exam grades (number between 1 & 100, because exams are 100 pts)
        sumOfExams = sum(examGrades)
        # computes avg (number between 1 & 100, because exams are 100 pts)
        avgExam = sumOfExams / num
    else:
        avgExam = 0

    return avgExam   # return the Exam average

#****************** MAIN/DRIVER  ******************
def main():
    # main function will call each of your average functions to compute each component of the overall class average

    # Open the files for reading and get the number of grades
    infile1 = open("lab8_labGrades.py", "r")
    num1 = eval(input("How many lab grades are in the file? "))

    infile2 = open("lab8_paGrades.py", "r")
    num2 = eval(input("How many PA grades are in the file? "))

    infile3 = open("lab8_examGrades.py", "r")
    num3 = eval(input("How many exam grades are in the file? "))

    print()

    # Call functions LabAvg, PaAvg, ExamAvg
    # Send corresponding file names and number of elements in the file
    labAverage = LabAvg(infile1, num1)
    paAverage = PaAvg(infile2, num2)
    examAverage = ExamAvg(infile3, num3)

    # Convert average to percentages
    labPct = labAverage / 100
    paPct = paAverage / 100  # Assuming PA grades are out of 100
    examPct = examAverage / 100  # Assuming exam grades are out of 100

    # Calculate the overall class average using the given weights
    overallAverage = (labPct * 0.10) + (paPct * 0.20) + (examPct * 0.70)

    # Print results
    print()
    print("  Lab Average =", format(labPct * 100, '6.2f'), '%')
    print("   PA Average =", format(paPct * 100, '6.2f'), '%')
    print(" Exam Average =", format(examPct * 100, '6.2f'), '%')
    print("-------------")
    print("Class Average =", format(overallAverage * 100, '6.2f'), '%')
    print()

main()   # Call the main function to start the program
