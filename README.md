# My Free QR

My Free QR es una herramienta para generar códigos QR a partir de enlaces o textos mediante una interfaz de línea de comandos (CLI) en Python. Permite crear códigos QR en varios formatos como PNG, JPG y SVG con diferentes niveles de corrección de errores.

## Características

    Generación de QR: Crea códigos QR a partir de enlaces o textos.
    Soporte de formatos: Admite múltiples formatos de salida, como PNG, JPG y SVG.
    Niveles de corrección: Permite elegir entre tres niveles de corrección de errores: Bajo, Medio, Alto.
    Interfaz gráfica: Incluye una interfaz de usuario (UI) para la visualización de los códigos QR generados.

## Estructura

```yaml
qr_generator/
│── qr_generator/         # Carpeta del módulo principal
│   ├── __init__.py       # Indica que es un paquete de Python
│   ├── generator.py      # Lógica principal para generar los QR
│   ├── config.py         # Configuración opcional (ej. tamaño, formato)
│── tests/                # Carpeta para pruebas
│   ├── test_generator.py # Tests para verificar funcionalidad
│── examples/             # Carpeta para ejemplos de uso
│── requirements.txt      # Dependencias necesarias (ej. `qrcode`)
│── README.md             # Descripción del proyecto
│── .gitignore            # Archivos a ignorar en Git
│── main.py               # Script principal para ejecutar el generador
│── setup.py              # Configuración para instalar como paquete (opcional)
```

## Instalación

Para instalar las dependencias del proyecto, sigue estos pasos:

Clona el repositorio:

```bash
git clone https://github.com/ymalmiron1997/my-free-qr.git
cd my-free-qr
```

Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

Usar desde la Interfaz Gráfica

Para usar la herramienta con la interfaz gráfica (GUI), ejecuta el siguiente comando:

```bash
python main.py
```

## Cli

```bash
python -m qr_generator.generator <url_o_texto> --format <formato> --error-correction <nivel>
```

¡Gracias por usar My Free QR!