from esp32_lcd import GpioLcd
from time import sleep

# Configuración de pines del ESP32
rs = 2        # Pin RS del LCD conectado al pin D2 del ESP32
e = 4         # Pin Enable del LCD conectado al pin D4 del ESP32
d4 = 14       # Pin D4 del LCD conectado al pin D14 del ESP32
d5 = 27       # Pin D5 del LCD conectado al pin D27 del ESP32
d6 = 26       # Pin D6 del LCD conectado al pin D26 del ESP32
d7 = 25       # Pin D7 del LCD conectado al pin D25 del ESP32

# Configuración de la pantalla LCD (2 líneas y 16 caracteres)
lcd = GpioLcd(rs_pin=rs, enable_pin=e, d4_pin=d4, d5_pin=d5, d6_pin=d6, d7_pin=d7, num_lines=2, num_columns=16)

# Escribiendo en la pantalla LCD
lcd.clear()
lcd.putstr("Hola, ESP32!")
lcd.move_to(1, 0)
lcd.putstr("LCD en MicroPython")

# Ejemplo de actualización de texto
while True:
    lcd.clear()
    lcd.putstr("Actualizando...")
    sleep(2)
    lcd.clear()
    lcd.putstr("ESP32 con LCD")
    lcd.move_to(1, 0)
    lcd.putstr("MicroPython")
    sleep(2)
