import machine
import time

# Definir el pin del sensor infrarrojo
SENSOR_PIN = 21

# Configurar el pin
sensor = machine.Pin(SENSOR_PIN, machine.Pin.IN)

while True:
    # Leer el estado del sensor
    if sensor.value() == 1:
        print("Sin movimiento.")
    else:
        print("Movimiento detectado!")
    
    time.sleep(1)  # Espera 1 segundo antes de la próxima lectura
