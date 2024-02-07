from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a PDF document
c = canvas.Canvas("exam_answers.pdf", pagesize=letter)

# Add your numbered answers to the PDF
answers = [
    "1. Output of Python Statements:\n   a) print(5*5) will output: 25\n   b) print('5 * 5') will output: 5 * 5",
    "2. Legal or Illegal Identifiers in Python:\n   a) _Hello_ - Legal\n   b) pay-check - Illegal\n   c) 40_days - Legal",
    "3. Expression Values in Python:\n   a) 5 * 3 = 15 (integer)\n   c) float(2 / float(5)) = 0.4 (floating-point)",
    "4. Range Expression for the Given List:\n   my_list = list(range(10, 1, -2))",
    "5. Calculation of Surface Area of a Sphere:\n   surface = 4 * pi * (radius ** 2)",
    "6. Lean Body Weight (LBW) Calculation:\n   a) Input Statements:\n      weight_kg = ...\n      height_cm = ...",
    "   b) LBW Calculation:\n      LBW_woman = ...",
    "   c) Print Statement:\n      print('Your Lean Body Weight (LBW) is:', LBW_woman)"
]

# Set the font and size for the text
c.setFont("Helvetica", 12)

# Write each answer to the PDF
for answer in answers:
    c.drawString(20, 750, answer)
    c.showPage()

# Save the PDF file
c.save()
