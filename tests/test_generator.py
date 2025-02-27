import os
import pytest
from qr_generator.generator import generate_qr

def test_generate_qr():
    """Prueba la generación de un código QR."""
    test_file = "test_qr.png"
    generate_qr("https://example.com", test_file)
    assert os.path.exists(test_file), "El archivo QR no se generó correctamente"
    os.remove(test_file)  # Limpieza tras la prueba

if __name__ == "__main__":
    pytest.main()
