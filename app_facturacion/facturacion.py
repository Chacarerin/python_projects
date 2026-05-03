carpeta_facturas = './facturas/'  # Carpeta donde están las facturas
archivo_excel = './plantilla_facturas.xlsx'  # Plantilla Excel donde se guardarán los datos

import pdfplumber
import re

def extraer_datos_factura(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        texto = ""
        for pagina in pdf.pages:
            texto += pagina.extract_text()

    # Extrae datos usando patrones de ejemplo (ajusta según el formato de tus facturas)
    numero_factura = re.search(r'Número de Factura:\s+(\d+)', texto).group(1)
    fecha = re.search(r'Fecha:\s+(\d{2}/\d{2}/\d{4})', texto).group(1)
    monto_total = re.search(r'Monto Total:\s+\$([\d,]+.\d{2})', texto).group(1)

    return {
        "Número de Factura": numero_factura,
        "Fecha": fecha,
        "Monto Total": monto_total
    }