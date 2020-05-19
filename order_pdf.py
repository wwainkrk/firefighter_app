from reportlab.pdfgen import canvas

# Creating document
pdf = canvas.Canvas("firefighter_test.pdf")
pdf.save()

