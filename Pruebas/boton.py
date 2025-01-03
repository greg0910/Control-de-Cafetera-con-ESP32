from machine import Pin
import time

# Configura el pin del LED como salida
led = Pin(2, Pin.OUT)

# Configura el pin del botón como entrada con pull-up interno
button = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    if not button.value():  # Si el botón está presionado
        led.value(1)  # Enciende el LED
    else:
        led.value(0)  # Apaga el LED
    time.sleep(0.1)  # Espera un poco para evitar lecturas erráticas
