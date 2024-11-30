import os
from PyPDF2 import PdfWriter, PdfReader
from reportlab.lib.pagesizes import letter
from lib.utils import add_number_to_canvas
from io import BytesIO
from reportlab.pdfgen import canvas

# Directorio de salida de los PDFs
outoput_path = os.path.join(os.path.dirname(__file__), "assets", "output_grouped")
os.makedirs(outoput_path, exist_ok=True)

# Números a generar
ticket_numbers = (971, 975)
group_by_count = 20  # 20 tickets por archivo

"""
    Genera varios tickets agrupados en un solo archivo PDF
"""
def generate_grouped_tickets(template, start_number, end_number, group_by_count):
    for number in range(start_number, end_number + 1, group_by_count):
        # new_pdf = os.path.join(outoput_path, f"ticket_{number}-{number + group_by_count - 1}.pdf")
        print(f"Generando tickets {number} a {number + group_by_count - 1}")
        output_pdf = os.path.join(
            outoput_path, f"ticket_{number}-{number + group_by_count - 1}.pdf")
        new_pdf_writer = PdfWriter()
        for i in range(number, min(number + group_by_count, end_number + 1)):
            # Crear un canvas en memoria con el número de ticket
            packet = BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)

            # Dibujar el número de ticket
            add_number_to_canvas(can, i)
            
            can.showPage()
            can.save()

            # Mover a la posición de inicio
            packet.seek(0)
            # Leer el PDF original
            reader = PdfReader(template)
            overlay_pdf = PdfReader(packet)

            # Verificar que overlay_pdf tenga páginas
            if len(overlay_pdf.pages) == 0:
                raise ValueError(
                    "El PDF generado en memoria no tiene páginas.")

            # Mezclar la página original con el nuevo número
            page = reader.pages[0]
            page.merge_page(overlay_pdf.pages[0])
            new_pdf_writer.add_page(page)

        # Guardar el nuevo PDF con el grupo de tickets
        with open(output_pdf, "wb") as output_file:
            new_pdf_writer.write(output_file)


# Generar PDFs
template_path = os.path.join(os.path.dirname(__file__), "assets", "template.pdf")
generate_grouped_tickets(template_path, ticket_numbers[0], ticket_numbers[1], group_by_count)
