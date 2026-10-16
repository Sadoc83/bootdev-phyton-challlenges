# =========================================================
# Día 9 - Reparar ayudantes del Festival
# =========================================================

# =========================================================
# Varias funciones auxiliares del festival no funcionan correctamente. 
# Algunas contienen def instrucciones no válidas, mientras que otras imprimen sus resultados en 
# lugar de devolverlos.

# Corrige las cuatro funciones:

# calculate_ticket_cost(price, quantity)devuelve el costo total.
# format_performer(name, act)devuelve texto formateado como name - act.
# calculate_seats_left(capacity, reserved)Devuelve el número de asientos disponibles.
# format_show_time(show, hour)devuelve texto formateado como show starts at hour.
# Cada función debe usar una definstrucción válida y devolver su resultado. No debe imprimir nada.

# Ejemplo
# calculate_ticket_cost(8, 3)       # 24
# format_performer("Mira", "Magic") # "Mira - Magic"
# calculate_seats_left(50, 18)      # 32
# format_show_time("Fire Dance", 7) # "Fire Dance starts at 7"

def calculate_ticket_cost price, quantity:
    print(price * quantity)


def format_performer(name, act)
    print(f"{name} - {act}")


def calculate_seats_left(capacity, reserved):
    print(capacity - reserved)


def format_show_time show, hour:
    print(f"{show} starts at {hour}")


# =========================================================
# Solución paso a paso:

def calculate_ticket_cost (price, quantity):
    return price * quantity
#1

def format_performer (name, act):
    return f"{name} - {act}"
#2

def calculate_seats_left (capacity, reserved):
    return capacity - reserved
#3

def format_show_time (show, hour):
    return f"{show} starts at {hour}"
#4

# 🕵️‍♂️ Análisis a detalle y pasos intermedios
# El desafío nos advierte que los "ayudantes" están rotos por dos razones: instrucciones def 
# inválidas e impresiones en lugar de retornos. El camino a la respuesta adecuada, 
# se debe considerar evaluar y corregir cada caso así:

# 1. Calcular el costo de los boletos (calculate_ticket_cost)

# • El problema: Es necesario calcular el costo total basado en el precio individual (price) y 
#   la cantidad de boletos (quantity). Si venía con un print(), el validador fallaría porque 
#   la plataforma recibe un None.
# • Toma de decisiones: La operación matemática que junta un precio repetido varias veces es 
#   la multiplicación (*).
# • Paso intermedio / Opción: Pudiste haber creado una variable intermedia como 
#   total = price * quantity y luego hacer return total. Sin embargo, para mantener el código 
#   limpio y eficiente, la mejor opción es devolver la multiplicación directamente.

# 2. Formatear al artista (format_performer)

# • El problema: Se debe unir el nombre (name) y su espectáculo (act) con el formato 
#   exacto: "name - act".
# • Evaluación de opciones:
#	• Opción A (Concatenación con +): Escribir return name + " - " + act. Es válida y funciona, 
#               pero se corre el riesgo de equivocación con los espacios.
#	• Opción B (f-strings - Recomendada): Utilizar f"{name} - {act}". Es la opción más profesional 
#              en Python. Al poner el guion y los espacios físicamente dentro de las comillas, nos aseguramos de 
#              cumplir exactamente con la ortografía que exige el validador.

# 3. Calcular asientos restantes (calculate_seats_left)

# • El problema: Conocer cuántos lugares quedan libres a partir de la capacidad total (capacity) y 
#   los que ya están reservados (reserved).
# • Toma de decisiones: Al restarle una parte a un total, la operación lógica obligatoria es 
#   la resta (-). Nuevamente, nos aseguramos de usar return en lugar de print.

# 4. Formatear la hora del show (format_show_time)

# • El problema: Generar el texto dinámico "show starts at hour".
# • Toma de decisiones: Al igual que con el artista, la mejor herramienta es una f-string. 
#   Al declarar f"{show} starts at {hour}", Python tomará el texto del show y el número de la hora, 
#   inyectándolos limpiamente en la cadena.

# =========================================================
# 🔏 La Regla de Oro del Calabozo: print vs return

# Existe un detalle que es bueno tener presente siempre "entender como funcionan las piezas" por 
# decirlo de alguna manera, print() es solo un "espejo" que le muestra cosas al usuario en la pantalla,
# pero la computadora no puede usar esa información para nada más. 
# En cambio, return es la mano que le entrega el objeto al programa para que este pueda guardarlo, 
# validar las pruebas del festival y pues nada ganar los puntos de XP en Boot.dev 😅.

# 🔑 Para recordar: 
# Una f-string (literal de cadena formateado) es una forma de escribir cadenas de texto en Python 
# que permite insertar variables, operaciones y funciones directamente dentro del texto.