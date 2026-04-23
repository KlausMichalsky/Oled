# ========================================================================
#             🔸 O L E D  -  I 2 C   C O N N E C T I O N 🔸
# ========================================================================
#  Archivo    : I2C_Connection-Test.py
#  Autor      : Klaus Michalsky
#  Fecha      : Feb-2026
#
#  DESCRIPCION
#  -----------------------------------------------------------------------
#  - Inicializa bus I2C0 (GP4=SDA, GP5=SCL) del Pico.
#  - Configura display OLED SSD1306 128x64.
#  - Limpia pantalla y muestra "OLED OK!" en (0,0).
#  - Actualiza OLED con oled.show().
#  - Útil para verificar conexión y funcionamiento del módulo OLED.
#
#  HARDWARE
#  -----------------------------------------------------------------------
#  MCU     : Raspberry Pi Pico
#  OLED    : SSD1306 128x64 0.96” I2C (GP4=SDA, GP5=SCL)
#
#  ESTADO
#  -----------------------------------------------------------------------
#  ✅ Funcional
# ========================================================================

from machine import I2C, Pin
from ssd1306 import SSD1306_I2C

i2c = I2C(0, scl=Pin(5), sda=Pin(4))  # pines válidos para I2C0
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text("OLED OK!", 0, 0)
oled.show()
