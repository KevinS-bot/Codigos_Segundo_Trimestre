#include <Adafruit_GFX.h>    // Librería base para gráficos
#include <Adafruit_ST7735.h> // Librería para el ST7735

// Definir los pines
#define TFT_CS     5
#define TFT_RST    17
#define TFT_DC     16

// Crear el objeto de la pantalla
Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);

void setup() {
  // Inicializar la pantalla
  tft.initR(INITR_144GREENTAB);  // Usar el modelo adecuado
  tft.setRotation(1);  // Ajustar la orientación de la pantalla
  tft.fillScreen(ST77XX_BLACK); // Limpiar la pantalla con negro
  tft.setTextColor(ST77XX_WHITE); // Establecer color de texto
  
  // Escribir "Hola Mundo"
  tft.setTextSize(2);  // Tamaño del texto
  tft.setCursor(10, 10);  // Posición del cursor
  tft.print("Hola Mundo!");
  
  delay(1000); // Esperar un segundo
  
  // Contador del 1 al 10
  for (int i = 1; i <= 10; i++) {
    tft.fillScreen(ST77XX_BLACK); // Limpiar pantalla
    tft.setCursor(10, 10);  // Posición del cursor
    tft.print("Contador: ");
    tft.print(i);  // Mostrar el número
    delay(1000);  // Esperar un segundo
  }
}

void loop() {
  // No es necesario hacer nada en el loop para este ejemplo
}
