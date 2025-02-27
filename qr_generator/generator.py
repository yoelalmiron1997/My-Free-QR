import qrcode
from qrcode.image.svg import SvgImage  # Importa el generador de imágenes SVG
from PIL import Image  # Asegúrate de tener Pillow instalado

def generate_qr(data, output_file="qr_code.png", format="png", error_correction="ERROR_CORRECT_L"):
    """Genera un código QR a partir de un enlace o un número entero."""

    error_correction_map = {
        "ERROR_CORRECT_L": qrcode.constants.ERROR_CORRECT_L,
        "ERROR_CORRECT_M": qrcode.constants.ERROR_CORRECT_M,
        "ERROR_CORRECT_Q": qrcode.constants.ERROR_CORRECT_Q,
        "ERROR_CORRECT_H": qrcode.constants.ERROR_CORRECT_H,
    }

    qr = qrcode.QRCode(
        version=1,  # Controla el tamaño del QR
        error_correction=error_correction_map.get(error_correction, qrcode.constants.ERROR_CORRECT_L),
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    if format.lower() == "svg":
        # Para SVG, utilizamos SvgImage
        img = qr.make_image(image_factory=SvgImage)
        svg_data = img.to_string()  
        with open(output_file, "wb") as f:  
            f.write(svg_data)  
    else:
        img = qr.make_image(fill="black", back_color="white")
        
        if format.lower() == "jpg":

            img = img.convert("RGB")  # Convertir la imagen a RGB, ya que JPG no soporta transparencia
            img.save(output_file, format="JPEG", quality=95)  # Guardar en JPG con calidad 95
        else:
            img.save(output_file, format=format.upper())  

    print(f"QR generado y guardado en {output_file}")
