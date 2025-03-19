#include <Wire.h>
#include <Adafruit_SSD1306.h>

Adafruit_SSD1306 display(128, 64, &Wire, -1);

void setup() {
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) for (;;);
  display.setTextSize(2);
  display.setTextColor(WHITE);
}

void loop() {
  for (int i = 1; i <= 10; i++) {
    display.clearDisplay();
    display.setCursor(10, 10);
    display.println("Hola Mundo");
    display.setCursor(50, 40);
    display.print(i);
    display.display();
    delay(1000);
  }
}
