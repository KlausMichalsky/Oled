# ========================================================================
# 🔸 O L E D  -  A S 5 6 0 0   S H O W S   A N G L E   N O   L A T E N C Y🔸
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
#  - Evita latencia mostrando el último valor recibido del Zero,
#    no el actual del AS5600.
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

# Posiciones
LABEL_X = 0
LABEL_Y = 0
VALUE_X = 0
VALUE_Y = 20

# Dibujar etiqueta fija
oled.fill(0)
oled.text("Angulo:", LABEL_X, LABEL_Y)
oled.show()

# Variables
degrees_1decimal = "0.0"
last_displayed = ""
smooth_val = 0.0
alpha = 0.3  # factor suavizado


def mostrar_numero(valor):
    oled.fill_rect(VALUE_X, VALUE_Y, 128, 20, 0)
    oled.text(valor, VALUE_X, VALUE_Y)
    oled.show()


while True:
    # Leer UART
    while uart.any():
        try:
            line = uart.readline()
            if line:
                s = line.decode().strip()
                # Intentar convertir a float, descartar si falla
                try:
                    val_float = float(s)
                    # Suavizado exponencial
                    smooth_val = alpha * val_float + (1 - alpha) * smooth_val
                    degrees_1decimal = "{:.1f}".format(smooth_val)
                except:
                    pass
        except Exception as e:
            print("Error UART:", e)

    # Actualizar OLED solo si cambió
    if degrees_1decimal != last_displayed:
        mostrar_numero(degrees_1decimal)
        last_displayed = degrees_1decimal

    utime.sleep(0.02)  # ~50FPS máximo
