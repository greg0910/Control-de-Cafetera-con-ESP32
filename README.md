# Control de Relés, NeoPixel y Servomotor con Raspberry Pi Pico

Este código controla relés, un NeoPixel y un servomotor mediante botones conectados a una Raspberry Pi Pico. También permite realizar secuencias automáticas y ajustar el ángulo del servomotor.

---

## **Requisitos**

- Raspberry Pi Pico con microcontrolador RP2040.
- Relés para controlar dispositivos como bomba de agua, válvulas y resistencia.
- NeoPixel para indicar estados mediante colores.
- Servomotor para control de ángulo.
- Botones para iniciar secuencias y ajustar el servomotor.

---

## **Instalación**

1. Instala MicroPython en la Raspberry Pi Pico.
2. Usa Thonny o un entorno compatible para cargar el código.
3. Conecta los componentes según el esquema descrito.
4. Sube el archivo al microcontrolador y ejecútalo.

---

## **Funciones Principales**

### **1. Control de Relés:**

- **Relé 1 (GPIO 22):** Controla la bomba de agua.
- **Relé 2 (GPIO 21):** Controla la válvula de agua.
- **Relé 3 (GPIO 19):** Controla la válvula de café.
- **Relé 4 (GPIO 23):** Controla la resistencia.

### **2. NeoPixel:**

- **Indicador de Color:** Muestra estados mediante colores:
  - Rojo: Operación en progreso.
  - Blanco: Finalización.
  - Verde: Movimiento del servomotor.
  - Azul: Retorno del servomotor.

### **3. Servomotor:**

- Controla el ángulo de giro (0° a 180°).
- Se ajusta mediante el botón 2.

### **4. Botones:**

- **Botón 1 (GPIO 16):** Inicia la secuencia automática.
- **Botón 2 (GPIO 17):** Controla el movimiento del servomotor.

---

## **Secuencia Automática**

1. Apaga todos los relés.
2. Enciende el relé 4 (resistencia) y espera 15 segundos.
3. Enciende los relés 1 (bomba) y 2 (válvula de agua) durante 10 segundos.
4. Apaga el relé 2 y enciende el relé 3 (válvula de café) durante 5 segundos.
5. Apaga los relés restantes y cambia el color del NeoPixel a blanco.


## **Notas Finales**

Este proyecto es útil para automatizar procesos como preparación de bebidas o sistemas de riego. Además, permite expandir la funcionalidad agregando sensores adicionales o ampliando las secuencias.

