# ========================================================================
#                 🔸 O L E D  -  S E N D   R E C E I V E 🔸
# ========================================================================
#  Archivo    : OLED--SH1106_128x64_send_receive.py
#  Autor      : Klaus Michalsky
#  Fecha      : Feb-2026
#
#  DESCRIPCION
#  -----------------------------------------------------------------------
#  - Pico envía un ángulo de prueba al RP2040 Zero mediante UART0.
#  - Zero suma 1 y devuelve respuesta.
#  - Pico muestra ángulo enviado y respuesta en OLED SH1106 128x64.
#  - Pantalla actualiza cada 0.5s.
#
#  HARDWARE
#  -----------------------------------------------------------------------
#  MCU     : Raspberry Pi Pico y RP2040-Zero
#  OLED    : SH1106 128x64 1.3" or 2.42" I2C (SDA=GP4, SCL=GP5)
#  UART0   : GP0=TX, GP1=RX
#
#  ESTADO
#  -----------------------------------------------------------------------
#  ✅ Funcional
# ========================================================================


import utime
from machine import UART, Pin, I2C
from sh1106 import SH1106_I2C


# -----------------------------
# CONFIG UART
# -----------------------------
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))


# -----------------------------
# CONFIG OLED I2C (SH1106)
# -----------------------------
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
oled = SH1106_I2C(128, 64, i2c)

# -----------------------------
# ANGULO DE PRUEBA
# -----------------------------
angulo = 123


def mostrar(texto1, texto2):
    oled.fill(0)
    oled.text(texto1, 0, 0)
    oled.text(texto2, 0, 16)
    oled.show()


# Inicializar pantalla
respuesta = ""  # definir respuesta como string
mostrar("Esperando...", "")

while True:
    # Enviar angulo al Zero
    uart.write(str(angulo) + "\n")
    print("Pico -> Zero:", angulo)

    # Leer respuesta si hay datos
    if uart.any():
        respuesta = uart.readline().decode().strip()
        print("Zero -> Pico", respuesta)

    # Mostrar en OLED
    mostrar(f"Enviado: {angulo}", f"Recibido: {respuesta}")

    utime.sleep(0.5)
