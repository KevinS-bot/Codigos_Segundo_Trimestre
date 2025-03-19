from machine import Pin, SPI
import dht
import time
import ST7735
import sysfont

spi = SPI(1, baudrate=20000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13))
tft = ST7735.TFT(spi, aDC=16, aReset=17, aCS=18)
tft.initr()

sensor = dht.DHT11(Pin(4))

def mostrar_temperatura():
    while True:
        try:
            sensor.measure()
            temp = sensor.temperature()
            hum = sensor.humidity()
            
            tft.fill(tft.BLACK)  
            tft.text((10, 20), "Temp: {:.1f} C".format(temp), tft.WHITE, sysfont.sysfont)
            tft.text((10, 40), "Humedad: {:.1f}%".format(hum), tft.CYAN, sysfont.sysfont)

            time.sleep(1)

        except Exception as e:
            print("Error:", e)
            time.sleep(1)

mostrar_temperatura()


