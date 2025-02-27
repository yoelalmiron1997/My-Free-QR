from setuptools import setup, find_packages

setup(
    name="qr_generator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "qrcode[pil]",
    ],
    entry_points={
        "console_scripts": [
            "qrgen=qr_generator.generator:generate_qr",
        ],
    },
)
