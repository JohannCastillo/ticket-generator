from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from io import BytesIO

def add_number_to_canvas(canvas, ticket_number):
    # configuración de fuente
    canvas.setFont("Helvetica-Bold", 27)
    canvas.setFillColor("white")

    # dibujar un rectángulo
    cords = (500, 80)
    width = 70
    height = 30
    # canvas.setFillColor("black")
    # canvas.rect(cords[0], cords[1], width, height, fill=1)

    # Dibujar número de  ticket centrado en el rectángulo
    text_width = canvas.stringWidth(str(ticket_number), "Helvetica-Bold", 27)
    text_x = cords[0] + (width - text_width) / 2
    text_y = cords[1] + (height - 27) / 2
    canvas.drawString(text_x, text_y, str(ticket_number))
