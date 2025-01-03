from machine import Pin, PWM
from time import sleep
import neopixel
import _thread

# Pines de la ESP32
rele_1 = Pin(22, Pin.OUT)  # Bomba de agua
rele_2 = Pin(21, Pin.OUT)  # Válvula de agua
rele_3 = Pin(19, Pin.OUT)  # Válvula de café
rele_4 = Pin(23, Pin.OUT)  # Resistencia
button = Pin(18, Pin.IN, Pin.PULL_UP)  # Botón
servo_pin = Pin(17, Pin.OUT)
servo_pwm = PWM(servo_pin, freq=50)  # Configura el PWM para 50 Hz
np = neopixel.NeoPixel(Pin(15), 1)

event_resistencia = _thread.allocate_lock()
event_bomba_agua = _thread.allocate_lock()
event_valvula_agua_cafe = _thread.allocate_lock()
event_button = _thread.allocate_lock()

def resistencia():
    try:
        with event_resistencia:
            print("Activando relé 4")
            rele_4.value(1)  # Activa el relé 4
            sleep(5)  # Espera 5 segundos
            print("Esperando a que bomba de agua termine")
            event_bomba_agua.acquire()  # Espera a que el relé de la bomba de agua termine
            print("Desactivando relé 4")
            rele_4.value(0)  # Desactiva el relé 4
            event_resistencia.release()
    except Exception as e:
        print(f"Error en resistencia: {e}")

def releBombaDeAgua():
    try:
        with event_bomba_agua:
            np[0] = (255, 0, 0)  # Rojo brillante
            np.write()
            rele_1.value(0)
            sleep(5)
            print("Activando relé 1")
            rele_1.value(1)
            sleep(10)  # Espera 10 segundos
            rele_1.value(0)  # Desactiva el relé de la bomba de agua
            print("Liberando event_valvula_agua_cafe")
            event_valvula_agua_cafe.acquire()  # Espera a que la válvula de agua y café termine
            np[0] = (255, 255, 255)  # Blanco brillante
            np.write()
            event_bomba_agua.release()
    except Exception as e:
        print(f"Error en releBombaDeAgua: {e}")

def releValvulaDeAguaYCafe():
    try:
        with event_valvula_agua_cafe:
            rele_2.value(0)
            sleep(5)
            print("Activando relé 2")
            rele_2.value(1)  # Activa la válvula de agua
            sleep(5)  # Espera 5 segundos
            rele_2.value(0)  # Desactiva la válvula de agua
            rele_3.value(1)  # Activa la válvula de café
            sleep(5)  # Espera 5 segundos
            rele_3.value(0)  # Desactiva la válvula de café
            sleep(1)
            event_valvula_agua_cafe.release()
    except Exception as e:
        print(f"Error en releValvulaDeAguaYCafe: {e}")

def set_angle(angle):
    pulse_width = int(500 + (angle / 180) * 2000)  # Pulsos en microsegundos
    servo_pwm.duty_u16(int(pulse_width * 65535 / 20000))  # Ajusta el pulso

def botonServo(pin):
    if not button.value():  # Verifica si el botón está presionado (activo bajo)
        np[0] = (0, 255, 0)  # Verde brillante
        np.write()
        set_angle(0)
        sleep(1)
        set_angle(90)
        sleep(5)
    else:
        set_angle(0)
        np[0] = (0, 0, 255)  # Azul brillante
        np.write()
    sleep(0.1)  # Espera un poco para evitar lecturas erráticas

def ejecutar_tareas():
    try:
        if not event_resistencia.locked():
            _thread.start_new_thread(resistencia, ())
        if not event_bomba_agua.locked():
            _thread.start_new_thread(releBombaDeAgua, ())
        if not event_valvula_agua_cafe.locked():
            _thread.start_new_thread(releValvulaDeAguaYCafe, ())
    except Exception as e:
        print(f"Error en ejecutar_tareas: {e}")


# Configura la interrupción en el pin del botón
button.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=botonServo)

while True:
    # Ejecutar tareas en hilos
    ejecutar_tareas()
    sleep(0.1)  # Mantiene el hilo principal en ejecución
