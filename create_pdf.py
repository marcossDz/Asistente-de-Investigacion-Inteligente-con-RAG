from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

pdf_path = "data/raw/test.pdf"
c = canvas.Canvas(pdf_path, pagesize=letter)
text = """Este es un documento de prueba. Vamos a ver si el procesador lo divide en chunks correctamente. Aquí hay más texto para que sea lo suficientemente largo. Este es un texto adicional que debería ser lo suficientemente extenso como para que el procesador de documentos lo divida en varios fragmentos según el tamaño de chunk configurado en el archivo de configuración. Añadimos más palabras para asegurarnos de que supere el límite de 500 caracteres y veamos cómo se comporta el sistema al indexar y buscar en una base de datos vectorial con múltiples fragmentos de un solo documento. Esto es solo una prueba para verificar el funcionamiento completo del pipeline."""
c.drawString(100, 750, text[:200])
c.drawString(100, 700, text[200:400])
c.drawString(100, 650, text[400:])
c.showPage()
c.save()
print(f"PDF creado en {pdf_path}")