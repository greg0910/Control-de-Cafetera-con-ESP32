from machine import Pin, PWM
import time
import neopixel

# Inicialización de los relés
rele_1 = Pin(22, Pin.OUT)  # Bomba de agua
rele_2 = Pin(21, Pin.OUT)  # Válvula de agua
rele_3 = Pin(19, Pin.OUT)  # Válvula de café
rele_4 = Pin(23, Pin.OUT)  # Resistencia

# Inicialización del NeoPixel (asegúrate de usar un pin diferente para el servomotor)
np = neopixel.NeoPixel(Pin(15), 1)

# Configuración de los botones
button1 = Pin(16, Pin.IN, Pin.PULL_UP)
button2 = Pin(17, Pin.IN, Pin.PULL_UP)  # Botón para el servo motor

# Configuración del servomotor
servo_pin = Pin(4, Pin.OUT)  # Usa un pin diferente
servo_pwm = PWM(servo_pin, freq=50)  # Configura el PWM para 50 Hz

def set_color(color):
    np[0] = color
    np.write()

def ejecutar_secuencia():
    # Apagar todos los relés al inicio
    rele_1.value(0)
    rele_2.value(0)
    rele_3.value(0)
    rele_4.value(0)
    
    # Paso 1: Encender el relé 4, cambiar el color a rojo y esperar 15 segundos
    set_color((255, 0, 0))  # Rojo
    rele_4.value(1)
    time.sleep(15) #cambiar el tiempo que desee
    
    # Paso 2: Encender los relés 1 y 2 al mismo tiempo y esperar 10 segundos
    set_color((255, 0, 0))  # Rojo
    rele_1.value(1)
    rele_2.value(1)
    time.sleep(10) #cambiar el tiempo que desee
    
    # Paso 3: Apagar el relé 2 y encender el relé 3 durante 5 segundos
    set_color((255, 0, 0))  # Rojo
    rele_2.value(0)
    rele_3.value(1)
    time.sleep(5) #cambiar el tiempo que desee
    
    # Paso 4: Cambiar el color a blanco y apagar los relés 3, 4 y 1
    set_color((255, 255, 255))  # Blanco
    rele_3.value(0)
    rele_4.value(0)
    rele_1.value(0)
    
    print("Secuencia completada.")

def set_angle(angle):
    # Calcula el pulso de acuerdo al ángulo deseado
    pulse_width = int(1000 + (angle / 180) * 1000)  # Pulsos en microsegundos
    servo_pwm.duty_u16(pulse_width * 65535 // 20000)  # Ajusta el pulso

def botonServo(pin):
    if not button2.value():  # Cambia el nombre del botón si es diferente
        set_color((0, 255, 0)) # Verde
        print("Pulso del servo")
        set_angle(0)
        time.sleep(1)
        set_angle(180)  # Ajusta el ángulo , hacer prueba de angulo
        time.sleep(5) #cambiar el tiempo que desee
        set_angle(0)
    else:
        set_color((0, 0, 255)) # Azul
        print("Regreso")
        set_angle(0)

def boton_callback(pin):
    if not button1.value():  # Cambia el nombre del botón si es diferente
        print("Pulso la función")
        ejecutar_secuencia()

# Ejecuta la secuencia inicial
ejecutar_secuencia()

# Configura las interrupciones del botón
button1.irq(trigger=Pin.IRQ_FALLING, handler=boton_callback)
button2.irq(trigger=Pin.IRQ_FALLING, handler=botonServo)

# Loop principal vacío
while True:
    time.sleep(1)  # Mantiene el ESP32 en un bucle vacío
