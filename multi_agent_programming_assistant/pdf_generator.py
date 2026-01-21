from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import textwrap

def generate_pdf(content: str, file_path="output.pdf"):
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    x_margin = 40
    y_margin = 800
    max_width = 90

    wrapped_lines = []
    for line in content.split("\n"):
        wrapped_lines.extend(textwrap.wrap(line, max_width) or [""])

    y = y_margin
    for line in wrapped_lines:
        if y < 50:   # new page
            c.showPage()
            y = y_margin
        c.drawString(x_margin, y, line)
        y -= 14

    c.save()
    return file_path
