# ========================================================================
#                  🔸 O L E D  -  I 2 C   S C A N 🔸
# ========================================================================
#  Archivo    : I2C_Scan-Test.py
#  Autor      : Klaus Michalsky
#  Fecha      : Feb-2026
#
#  DESCRIPCION
#  -----------------------------------------------------------------------
#  - Inicializa bus I2C0 (GP4=SDA, GP5=SCL) del Pico.
#  - Escanea todos los dispositivos conectados al bus I2C.
#  - Muestra en consola las direcciones encontradas.
#  - Útil para verificar conexión y dirección de módulos I2C (OLED, sensores, etc.).
#  - No altera los dispositivos, solo detecta su presencia.
#
#  HARDWARE
#  -----------------------------------------------------------------------
#  MCU     : Raspberry Pi Pico
#  I2C0    : GP4=SDA, GP5=SCL
#
#  ESTADO
#  -----------------------------------------------------------------------
#  ✅ Funcional
# ========================================================================

from machine import Pin, I2C
i2c = I2C(0, scl=Pin(5), sda=Pin(4))  # tus pines I2C
print(i2c.scan())  # devuelve lista de direcciones detectadas
