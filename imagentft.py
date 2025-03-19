from ST7735 import TFT, TFTColor
from machine import SPI, Pin
import time

spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
tft = TFT(spi, 16, 17, 18)
tft.initr()
tft.rgb(True)
tft.fill(TFT.BLACK)

def mostrar_imagen(nombre):
    try:
        f = open(nombre, 'rb')
        if f.read(2) == b'BM':
            f.seek(10)
            offset = int.from_bytes(f.read(4), 'little')
            f.seek(18)
            width = int.from_bytes(f.read(4), 'little')
            height = int.from_bytes(f.read(4), 'little')
            f.seek(28)
            depth = int.from_bytes(f.read(2), 'little')

            if depth == 24:
                rowsize = (width * 3 + 3) & ~3
                flip = height > 0
                height = abs(height)

                w, h = min(width, 128), min(height, 160)
                tft._setwindowloc((0, 0), (w - 1, h - 1))

                buffer = bytearray(2 * w)

                for row in range(h):
                    pos = offset + (height - 1 - row) * rowsize if flip else offset + row * rowsize
                    f.seek(pos)
                    row_data = f.read(w * 3)

                    for col in range(w):
                        bgr = row_data[col * 3: col * 3 + 3]
                        color = TFTColor(bgr[2], bgr[1], bgr[0])
                        buffer[col * 2] = color >> 8
                        buffer[col * 2 + 1] = color & 0xFF

                    tft._writedata(buffer)

        f.close()
    except OSError:
        print(f"Error: No se pudo abrir {nombre}")

mostrar_imagen("test128x160.bmp")

spi.deinit()
