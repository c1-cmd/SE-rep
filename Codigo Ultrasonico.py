import machine
import time

# Definir los pines
TRIG_PIN = 23
ECHO_PIN = 22

# Configurar los pines
trig = machine.Pin(TRIG_PIN, machine.Pin.OUT)
echo = machine.Pin(ECHO_PIN, machine.Pin.IN)

def medir_distancia():
    # Limpia el TRIG
    trig.value(0)
    time.sleep_us(2)

    # Enviar un pulso de 10 microsegundos
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    # Leer el tiempo de duración del pulso en ECHO
    while echo.value() == 0:
        start_time = time.ticks_us()

    while echo.value() == 1:
        end_time = time.ticks_us()

    # Calcular la distancia
    duration = time.ticks_diff(end_time, start_time)
    distance = (duration * 0.034) / 2  # en centímetros
    return distance

while True:
    distancia = medir_distancia()
    print("Distancia: {:.2f} cm".format(distancia))
    time.sleep(1)
