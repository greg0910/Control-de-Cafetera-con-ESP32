from machine import Pin, PWM
import time

# Configura el pin donde está conectado el servo (por ejemplo, GPIO 15)
servo_pin = Pin(15, Pin.OUT)
servo_pwm = PWM(servo_pin)

# Establece la frecuencia del PWM (generalmente 50Hz para servos)
servo_pwm.freq(50)

def set_angle(angle):
    # Calcula el pulso de acuerdo al ángulo deseado
    pulse_width = int(1000 + (angle / 180) * 1000)  # Pulsos en microsegundos
    servo_pwm.duty_u16(pulse_width * 65535 // 20000)  # Ajusta el pulso
    
while True:
    
    # Mueve el servo a 45 grados
    set_angle(0)
    time.sleep(1)

# Mueve el servo a 90 grados
    set_angle(180)
    time.sleep(1)



