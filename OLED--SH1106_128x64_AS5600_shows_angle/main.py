# ========================================================================
#           🔸 O L E D - A S 5 6 0 0   S H O W S   A N G L E 🔸
# ========================================================================
#  Archivo    : OLED--SH1106_128x64_AS5600_shows_angle.py
#  Autor      : Klaus Michalsky
#  Fecha      : Feb-2026
#
#  DESCRIPCION
#  -----------------------------------------------------------------------
#  - Lee ángulo del sensor AS5600 vía I2C (Wire1) en GP26=SDA, GP27=SCL.
#  - Convierte valor crudo 12 bits (0–4095) a grados (0°–360°).
#  - Muestra ángulo en OLED SH1106 128x64 cada 200 ms.
#  - Recibe valor desde Zero por UART0 (GP0=TX, GP1=RX).
#
#  HARDWARE
#  -----------------------------------------------------------------------
#  MCU     : Raspberry Pi Pico
#  Sensor  : AS5600 I2C (GP26=SDA, GP27=SCL)
#  OLED    : SH1106 128x64 1.3" or 2.42" I2C (GP4=SDA, GP5=SCL)
#  UART0   : GP0=TX, GP1=RX (Zero)
#
#  ESTADO
#  -----------------------------------------------------------------------
#  ✅ Funcional
# ========================================================================

import utime
from machine import UART, Pin, I2C
from sh1106 import SH1106_I2C

# UART al Zero
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

# OLED SH1106
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
oled = SH1106_I2C(128, 64, i2c)

# Valor inicial
degrees_1decimal = "0.0"


# Función para mostrar en OLED
def mostrar(texto1, texto2):
    oled.fill(0)
    oled.text(texto1, 0, 0)
    oled.text(texto2, 0, 16)
    oled.show()


# Inicialización
mostrar("Esperando...", degrees_1decimal)
utime.sleep(1)  # espera 1 segundo para que el Zero arranque


while True:
    # Leer datos del Zero
    if uart.any():
        try:
            line = uart.readline()
            if line:
                degrees = line.decode().strip()
                if len(degrees) > 1:  # evitar strings vacíos
                    # quitar segundo decimal si hay
                    degrees_1decimal = degrees[:-1]
                    print("Zero -> Pico:", degrees_1decimal)
        except Exception as e:
            print("Error UART:", e)

    # Mostrar en OLED el último valor recibido
    mostrar("Angulo:", degrees_1decimal)

    utime.sleep(0.05)  # 50ms
