from ST7735 import TFT, TFTColor
from machine import SPI, Pin
import time

# Configuración del SPI y la pantalla TFT
spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))  # 10 MHz en vez de 20 MHz

tft = TFT(spi, 16, 17, 18)
tft.initr()
tft.rgb(True)
tft.fill(TFT.BLACK)

# Función para cargar y mostrar una imagen BMP
def mostrar_imagen(nombre):
    try:
        f = open(nombre, 'rb')
        if f.read(2) == b'BM':  # Verifica que es un archivo BMP
            f.seek(10)
            offset = int.from_bytes(f.read(4), 'little')
            f.seek(18)
            width = int.from_bytes(f.read(4), 'little')
            height = int.from_bytes(f.read(4), 'little')
            f.seek(28)
            depth = int.from_bytes(f.read(2), 'little')

            if depth == 24:  # Verifica que sea una imagen de 24 bits sin compresión
                rowsize = (width * 3 + 3) & ~3
                flip = height > 0  # Determina si la imagen está invertida
                height = abs(height)

                w, h = min(width, 128), min(height, 160)
                tft._setwindowloc((0, 0), (w - 1, h - 1))

                for row in range(h):
                    pos = offset + (height - 1 - row) * rowsize if flip else offset + row * rowsize
                    f.seek(pos)

                    for col in range(w):
                        bgr = f.read(3)
                        tft._pushcolor(TFTColor(bgr[2], bgr[1], bgr[0]))

        f.close()
    except OSError:
        print(f"Error: No se pudo abrir {nombre}")

while True:
    # Mostrar la primera imagen
    mostrar_imagen("imagen.bmp")
    time.sleep(2)  # Espera 5 segundos

    
    mostrar_imagen("inverna.bmp")
    time.sleep(2)

# Cierra SPI cuando termina
spi.deinit()
