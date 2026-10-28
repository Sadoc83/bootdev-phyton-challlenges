# Día 14 - Configurar un controlador PWM, sistemas embebidos

Configurar controlador PWM (Python para sistemas embebidos)
Completa la función configure_pwm.

Se esta simulando un sistema embebido donde los registros de hardware se almacenan en un diccionario de Python. Cada registro es un valor entero donde los bits individuales controlan diferentes características.

La idea es que voy a configurar un controlador PWM (Modulación por Ancho de Pulso) sencillo que se utiliza para controlar un motor o un LED.

## Diseño del registro
El diccionario registers siempre contendrá estas claves:

+ "PWM_CTRL"– registro de control (campo de bits)
+ "PWM_DUTY"– Registro del ciclo de trabajo (0–255)

## bits PWM_CTRL
+ Bit 0 – Bit de habilitación
  * 0= deshabilitado
  * 1= habilitado

+ Campo de modo : dos bits que a configurarse según el patrón 10(bit 2 = 1, bit 1 = 0).
  * Estos son los dos bits de modo que intentaré controlar 🤓.
+ Todos los demás elementos deben dejarse sin cambios.

## valor PWM_DUTY
* Almacena el ciclo de trabajo en una escala de 0 a 255.
* La función recibe como duty_percent un entero de 0 a 100.
* Lo convertiré a un valor de 0 a 255 usando aritmética de enteros (sin números de coma flotante). Por ejemplo:

*scaled_value = duty_percent * 255 // 100*

## Requisitos de la función
Implementar:

*def configure_pwm(registers, duty_percent, enable):
    ...*

### La función debería:

1. Actualizar PWM_CTRL:

   * Empezaré desde el valor actual en registers["PWM_CTRL"].
   * Luego borraré el bit 0 (habilitación) y los dos bits de modo (bit 1 y bit 2), sin cambiar ningún otro bit.
   * Si enable es True, estableceré el bit 0 en 1. Si es False, ahí se quedá como está 0.
   * Entre mejor deje en paz los bits de modo al patrón 10(bit 2 = 1, bit 1 = 0) mejor, no?.
   * El nuevo valor de nuevo en registers["PWM_CTRL"] lo guardaré igual.

2. Actualizar PWM_DUTY:

   * Conviertiré duty_percentun valor entre 0 y 100 a un valor entre 0 y 255 utilizando aritmética de enteros.
   * Limitaré duty_percental rango de 0 a 100 antes de escalar.
   * Almacenaré ese valor en registers["PWM_DUTY"].

3. Devuelveré (bueno yo no Python, pero se entiende lo empatico que intento ser) el diccionario registers (después de la modificación).

Utilizaré operadores bit a bit como &, |, y ~ para borrar y establecer bits. Trataré los números enteros como campos de bits y actualizaré solo los bits que controle, conservando todo lo demás.

## Ejemplos
registers = {
    "PWM_CTRL": 0b00010010,  # some other features already set
    "PWM_DUTY": 0,
}

result = configure_pwm(registers, 50, True)


 50% → 127 (50 * 255 // 100 = 127)
print(result["PWM_DUTY"])  # 127

 Bit 0 should be 1 (enabled)
Mode bits (bit1, bit2) should be 10
Other bits should be preserved

## Resultado paso a paso

Pasamos del software puro a la simulación de sistemas embebidos y manipulación de bits a bajo nivel (Bitwise Operations) en Python. 

# 🤖⚙️ 

Este tipo de problemas es muy común en hardware para asegurar que encendemos o apagamos funciones específicas sin corromper el resto de la configuración del microcontrolador.

Para resolver este acertijo de Boot.dev, debemos reemplazar el bloque pass aplicando máscaras lógicas (&, |, ~) y corrimientos de bits (<<).
Aquí tienes la solución completa, explicada paso a paso y estructurada para tu archivo main.py:

## 🛠️ Código

PWM_ENABLE_BIT = 1 << 0
# Mode uses bits 1 and 2
PWM_MODE_BITS_MASK = (1 << 1) | (1 << 2)


def configure_pwm(registers, duty_percent, enable):
    # =========================================================
    # PASO 1: MODIFICACIÓN DEL REGISTRO DE CONTROL (PWM_CTRL)
    # =========================================================
    
    # 1.1 Obtener el valor actual del registro
    ctrl = registers["PWM_CTRL"]
    
    # 1.2 Limpiar (apagar) los bits 0, 1 y 2 usando una máscara inversa (~ y &)
    # Combinamos el bit de habilitación y los bits de modo en una sola máscara
    clear_mask = PWM_ENABLE_BIT | PWM_MODE_BITS_MASK
    ctrl = ctrl & ~clear_mask
    
    # 1.3 Si 'enable' es True, encendemos el bit 0 usando el operador OR (|)
    if enable:
        ctrl = ctrl | PWM_ENABLE_BIT
        
    # 1.4 Configurar el modo al patrón binario '10' (bit 2 = 1, bit 1 = 0)
    # El patrón '10' en los bits 2 y 1 equivale al número binario 0b100 (un 4 en decimal)
    mode_pattern = 1 << 2  # bit 2 en 1, bit 1 se queda en 0 por la limpieza previa
    ctrl = ctrl | mode_pattern
    
    # 1.5 Guardar el registro de control modificado
    registers["PWM_CTRL"] = ctrl

    # =========================================================
    # PASO 2: MODIFICACIÓN DEL REGISTRO DE TRABAJO (PWM_DUTY)
    # =========================================================
    
    # 2.1 Limitar (clamp) el porcentaje de trabajo entre 0 y 100
    if duty_percent < 0:
        duty_percent = 0
    elif duty_percent > 100:
        duty_percent = 100
        
    # 2.2 Escalar el valor a una resolución de 8 bits (0-255) usando aritmética entera
    scaled_value = duty_percent * 255 // 100
    
    # 2.3 Guardar el valor escalado
    registers["PWM_DUTY"] = scaled_value

    # =========================================================
    # PASO 3: RETORNO DEL INVENTARIO DE HARDWARE
    # =========================================================
    return registers

## 🕵️‍♂️ Análisis a detalle y Toma de Decisiones Paso a Paso

Desglosando qué hace la computadora en los puntos más complejos y por qué lo hace así:

1. ¿Cómo se limpian bits específicos sin romper los demás? (ctrl & ~clear_mask)

    * El problema: Queremos apagar los bits 0, 1 y 2 de registers["PWM_CTRL"], pero dejar intactos los bits del 3 al 7.
    * Toma de decisiones: Si sumamos con un OR lógico (|) el bit 1 << 0 (bit 0) y la máscara (1 << 1) | (1 << 2) (bits 1 y 2), obtenemos en binario el número 0b00000111. Al aplicarle el operador de inversión NOT (~), este número se convierte en 0b11111000.
    * Por qué funciona: Al hacer un AND (&) entre el registro original y 0b11111000, cualquier bit que multiplique a los 1s mantendrá su estado original, mientras que los bits que multipliquen a los 0s (nuestros objetivos 0, 1 y 2) se apagarán por completo de forma segura.

2. Establecer el patrón de Modo 10 (1 << 2)

    * El problema: Las instrucciones piden que los bits de modo queden configurados exactamente como bit 2 = 1 y bit 1 = 0.
    * Toma de decisiones: Como en el paso anterior dejamos los bits 1 y 2 completamente limpios (en 0), para lograr el patrón 10 solo hace falta encender el bit 2. Hacemos un corrimiento hacia la posición 2 (1 << 2), lo que nos da en binario 0b00000100, y lo inyectamos usando el operador OR (|). El bit 1 se queda automáticamente en 0 como queríamos.

3. Restricción del ciclo de trabajo (Clamping)

    * El problema: El porcentaje de potencia de entrada (duty_percent) debe escalarse a una escala de hardware de 0 a 255, pero antes debemos asegurarnos de que el usuario no envíe un número inválido (como -50 o 150).
    * Toma de decisiones: Usamos condicionales if/elif clásicos para limitar el valor antes de procesarlo matemáticamente. Si es menor a 0 se queda en 0, y si supera 100 se queda en 100. Finalmente aplicamos la división entera // para garantizar que la salida sea un entero puro compatible con los registros de hardware.
