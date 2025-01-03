import machine
import neopixel

# Configura el pin 15 para controlar un solo Neopixel
np = neopixel.NeoPixel(machine.Pin(15), 1)

# Establece el color del Neopixel
np[0] = (0, 255, 255)  # Rojo brillante

# Actualiza el Neopixel para reflejar el cambio
np.write()
