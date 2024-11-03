from esp32_lcd import GpioLcd
from time import sleep

# Configuración de pines del ESP32 WROOM-32
rs = 2        # Pin RS del LCD conectado al pin GPIO 2 del ESP32
e = 4         # Pin Enable del LCD conectado al pin GPIO 4 del ESP32
d4 = 5       # Pin D4 del LCD conectado al pin GPIO 14 del ESP32
d5 = 18       # Pin D5 del LCD conectado al pin GPIO 27 del ESP32
d6 = 19       # Pin D6 del LCD conectado al pin GPIO 26 del ESP32
d7 = 22       # Pin D7 del LCD conectado al pin GPIO 25 del ESP32

# Configuración de la pantalla LCD (2 líneas y 16 caracteres)
lcd = GpioLcd(rs_pin=rs, enable_pin=e, d4_pin=d4, d5_pin=d5, d6_pin=d6, d7_pin=d7, num_lines=2, num_columns=16)

# Escribiendo en la pantalla LCD con coordenadas específicas
lcd.clear()

# Mostrar "Hola, ESP32!" en la primera línea, a partir de la columna 0
lcd.move_to(0, 0)
lcd.putstr("Hola, ESP32!")

# Mostrar "LCD en MicroPython" en la segunda línea, a partir de la columna 0
lcd.move_to(0, 1)
lcd.putstr("LCD en MicroPython")

# Ejemplo de actualización de texto con coordenadas específicas
while True:
    # Actualización del mensaje en diferentes posiciones
    lcd.clear()
    
    # Mostrar "Actualizando..." en la primera línea, columna 3
    lcd.move_to(3, 0)
    lcd.putstr("Actualizando...")
    sleep(2)
    
    lcd.clear()
    
    # Mostrar "ESP32 con LCD" en la primera línea, columna 1
    lcd.move_to(1, 0)
    lcd.putstr("ESP32 con LCD")
    
    # Mostrar "MicroPython" en la segunda línea, columna 2
    lcd.move_to(2, 1)
    lcd.putstr("MicroPython")
    
    sleep(2)
