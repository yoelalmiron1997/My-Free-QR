import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtSvg import QSvgWidget
from qr_generator.generator import generate_qr  

class QRApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Free QR - Generador de Códigos QR")
        self.setGeometry(100, 100, 500, 500)

        layout = QVBoxLayout()

        # TÍTULO PRINCIPAL
        self.title_label = QLabel("My Free QR", self)
        self.title_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        # Etiqueta de instrucción
        self.label = QLabel("Ingrese la URL o texto:")
        layout.addWidget(self.label)

        # Campo de texto
        self.url_input = QLineEdit(self)
        layout.addWidget(self.url_input)

        # Selector de tipo de QR
        self.type_label = QLabel("Selecciona el tipo de QR:")
        layout.addWidget(self.type_label)
        
        self.type_combo = QComboBox(self)
        self.type_combo.addItems(["Alto", "Medio", "Bajo"])
        layout.addWidget(self.type_combo)

        # Selector de formato de salida
        self.format_label = QLabel("Selecciona el formato de imagen:")
        layout.addWidget(self.format_label)

        self.format_combo = QComboBox(self)
        self.format_combo.addItems(["PNG", "JPG", "SVG"])
        layout.addWidget(self.format_combo)

        # Botón para generar el QR
        self.button = QPushButton("Generar QR")
        self.button.clicked.connect(self.generate_qr)
        layout.addWidget(self.button)

        # Imagen del QR
        self.qr_label = QLabel(self)  # Para PNG y JPG
        self.qr_svg_widget = QSvgWidget(self)  # Para SVG
        self.qr_svg_widget.setVisible(False)  # Inicialmente oculto
        layout.addWidget(self.qr_label)
        layout.addWidget(self.qr_svg_widget)

        # Créditos
        self.credits_label = QLabel("© Tecnobear (Yoel Almiron)")
        self.credits_label.setFont(QFont("Arial", 10, QFont.StyleItalic))
        self.credits_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.credits_label)

        self.setLayout(layout)

    def generate_qr(self):
        url = self.url_input.text()
        qr_type = self.type_combo.currentText().lower()
        qr_format = self.format_combo.currentText().lower()

        # Cambiar el color del botón a verde cuando se presiona
        self.button.setStyleSheet("background-color: green; color: white;")

        # Determinar el nivel de corrección de error
        error_correction = {
            "bajo": "ERROR_CORRECT_L",
            "medio": "ERROR_CORRECT_M",
            "alto": "ERROR_CORRECT_H"
        }.get(qr_type, "ERROR_CORRECT_L")

        if url:
            output_file = f"qr_code.{qr_format}"
            generate_qr(url, output_file, format=qr_format, error_correction=error_correction)
            
            # Mostrar el QR generado en la UI
            if qr_format == "svg":
                self.qr_svg_widget.setVisible(True)  # Mostrar el QSvgWidget
                self.qr_label.setVisible(False)  # Ocultar QLabel

                # Cargar directamente el archivo SVG
                self.qr_svg_widget.load(output_file)

                # Ajustar el tamaño del QSvgWidget para que coincida con el tamaño de la imagen
                self.qr_svg_widget.setFixedSize(QSize(300, 300))  # Tamaño fijo de ejemplo, ajusta según sea necesario

            else:
                self.qr_svg_widget.setVisible(False)  # Ocultar QSvgWidget
                self.qr_label.setVisible(True)  # Mostrar QLabel
                self.qr_label.setPixmap(QPixmap(output_file))  # Mostrar PNG o JPG en QLabel

# Función para ejecutar la aplicación
def main():
    app = QApplication(sys.argv)
    window = QRApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
