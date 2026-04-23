// ========================================================================
//                 🔸 O L E D  -  S E N D   R E C E I V E 🔸
// ========================================================================
//  Archivo    : SH1106_128x64-Send-Receive.ino
//  Autor      : Klaus Michalsky
//  Fecha      : Feb-2026
//
//  DESCRIPCION
//  -----------------------------------------------------------------------
//  - Zero recibe ángulo del Pico por UART0.
//  - Suma 1 y envía la respuesta de vuelta.
//  - Debug por Serial USB.
//
//  HARDWARE
//  -----------------------------------------------------------------------
//  MCU     : RP2040-Zero
//  OLED    : SH1106_128x64 1.3" or 2.42"
//  UART0   : GP0=TX, GP1=RX
//  Conexión Pico: GP0↔GP1, GND y 3.3V comunes
//
//  ESTADO
//  -----------------------------------------------------------------------
//  ✅ Funcional
// ========================================================================

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
