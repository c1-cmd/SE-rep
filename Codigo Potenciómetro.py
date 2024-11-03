import machine
import time

# Definir el pin del potenciómetro
POT_PIN = 34

# Configurar el pin como entrada analógica
pot = machine.ADC(machine.Pin(POT_PIN))

# Configurar el rango de lectura (0-4095)
pot.atten(machine.ADC.ATTN_0DB)  # Rango 0-1.1V
# pot.atten(machine.ADC.ATTN_11DB)  # Rango 0-3.6V

while True:
    # Leer el valor analógico
    lectura = pot.read()
    
    # Convertir a voltaje (considerando un rango de 0-1.1V)
    voltaje = (lectura / 4095) * 1.1  # Ajusta según el rango

    print("Lectura: {}, Voltaje: {:.2f} V".format(lectura, voltaje))
    time.sleep(1)  # Espera 1 segundo antes de la próxima lectura
