#include <Arduino.h>
#line 1 "C:\\Users\\Benutzer1\\Documents\\# Github repositories\\OLED--SH1106_128x64\\OLED--SH1106_128x64_Send_angle\\OLED--SH1106_128x64_Send_angle.ino"
// ========================================================================
//                 🔸 O L E D  -  S E N D   A N G L E 🔸
// ========================================================================
//  Archivo    : OLED--SH1106_128x64_Send_angle.ino
//  Autor      : Klaus Michalsky
//  Fecha      : Feb-2026
//
//  DESCRIPCION
//  -----------------------------------------------------------------------
//  1. Pico envía ángulo.
//  2. Zero recibe, suma 1 y envía respuesta.
//  3. Pico recibe respuesta y la muestra en OLED y Serial.
//
//  HARDWARE
//  -----------------------------------------------------------------------
//  MCU     : Raspberry Pi Pico y RP2040-Zero
//  OLED    : SH1106_128x64
//
// ESQUEMA DE CONEXIONES:
//  -----------------------------------------------------------------------
/*
 ┌──────────────┐          ┌───────────────┐
 │   Pico       │          │   Zero        │
 ├──────────────┤          ├───────────────┤
 │ GP0 (TX) ─────────────────▶ GP1 (RX)    │
 │ GP1 (RX) ◀───────────────── GP0 (TX)    │
 │ GND ─────────────────────── GND         │
 │ 3V3 ─────────────────────── 3V3         │
 └──────────────┘          └───────────────┘

 OLED SH1106 <-> Pico
 ┌──────────────┐
 │ SDA → GP4    │
 │ SCL → GP5    │
 │ VCC → 3.3V   │
 │ GND → GND    │
 └──────────────┘
*/
//  ESTADO
//  -----------------------------------------------------------------------
//  ✅ Funcional
// ========================================================================

#line 44 "C:\\Users\\Benutzer1\\Documents\\# Github repositories\\OLED--SH1106_128x64\\OLED--SH1106_128x64_Send_angle\\OLED--SH1106_128x64_Send_angle.ino"
void setup();
#line 54 "C:\\Users\\Benutzer1\\Documents\\# Github repositories\\OLED--SH1106_128x64\\OLED--SH1106_128x64_Send_angle\\OLED--SH1106_128x64_Send_angle.ino"
void loop();
#line 44 "C:\\Users\\Benutzer1\\Documents\\# Github repositories\\OLED--SH1106_128x64\\OLED--SH1106_128x64_Send_angle\\OLED--SH1106_128x64_Send_angle.ino"
void setup()
{
    Serial.begin(115200);  // Debug USB
    Serial1.setTX(0);      // TX al Pico
    Serial1.setRX(1);      // RX del Pico
    Serial1.begin(115200); // UART a 115200

    Serial1.setTimeout(50); // 🔹 evitar bloqueos largos
}

void loop()
{
    if (Serial1.available())
    {
        Serial.println("Zero vivo");
        String angulo = Serial1.readStringUntil('\n');

        if (angulo.length() > 0) // 🔹 validar que no esté vacío
        {
            int valor = angulo.toInt();

            Serial.print("Zero recibio: ");
            Serial.println(valor);

            int respuesta = valor + 1;

            Serial1.print(respuesta);
            Serial1.print("\n");

            Serial.print("Zero envio: ");
            Serial.println(respuesta);
        }
    }
}

/*
void loop()
{
    // revisar si hay datos en UART1
    if (Serial1.available())
    {
        String angulo = Serial1.readStringUntil('\n'); // leer ángulo enviado por Pico
        int valor = angulo.toInt();

        Serial.print("Zero recibio: ");
        Serial.println(valor);

        int respuesta = valor + 1;

        Serial1.println(respuesta); // enviar de vuelta al Pico
        Serial.print("Zero envio: ");
        Serial.println(respuesta);
    }
}
*/

