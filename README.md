# Implementacion del OLED SSD1306 y SH1106 128x64 1.3" or 2.42" I2C
####  ALGORITMO:
  - Mandar y recibir datos para mosrtarlos en la panalla OLED
  - Uso de UART para comunicacion entre microcontroladores
  - framebuf_SSD1306.py - Driver para la pantalla OLED (subir al Pi Pico)
  - ssd1306.py  - Firmware para comunicacion I2C de la pantalla OLED (subir al Pi Pico)
  - para SH1106 usar otro framebuf.py
  - Usa Wire1 para I2C independiente de los pines por defecto
#### HARDWARE:
  - MCU        : Raspberry Pi Pico y RP2040-Zero
  - Display : OLED SSD1306 128x64 1.3" or 2.42" I2C
  - Display : OLED SH1106 128x64 1.3" I2C
