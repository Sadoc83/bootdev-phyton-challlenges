# =========================================================
# Día 4 - Desafíos de funciones
# La misión del día será, Familiarizarme con la sintaxis de las funciones, 
# y comprender el alcance de las variables en Python.
# =========================================================

# Desafio 1: Sumar dos números
def add_numbers(first_number, second_number):
    pass

# Al igual que en los desafíos anteriores, la palabra clave pass debe removerse por completo. 
# En su lugar, sumaremos los dos parámetros provistos por la plataforma (first_number y second_number) y 
# enviaremos el resultado al exterior utilizando directamente la instrucción return.

def add_numbers(first_number, second_number):
    # Sumamos ambos parámetros y devolvemos el resultado de inmediato
    return first_number + second_number


# 🔍 ¿Qué reglas estamos cumpliendo aquí?
# • Uso de return: El valor resultante de la suma es enviado de vuelta a la línea que invocó la función, 
# permitiendo que se asigne correctamente a variables como result.
# • No usar print(): Tal como lo pide explícitamente la asignación, la función no genera salidas de texto 
# en consola por sí misma, manteniendo el código limpio y enfocado únicamente en el procesamiento matemático.

# =========================================================

# Desafio 2: Combinar distancias de senderos
# Completa la combine_distancesfunción.

def combine_distances(first_distance, second_distance):
    pass


morning_distance = 4
evening_distance = 7

total_distance = None
print(total_distance)


# La función debería:

# Aceptar dos parámetros de distancia
# Devuelve su suma usando una returninstrucción
# Luego llama a la función con morning_distancey evening_distance, guarda el valor devuelto en total_distance, 
# e imprímelo.

# =========================================================
# Explicación de la solución paso a paso.
 
def combine_distances(first_distance, second_distance):
    return first_distance + second_distance # 4. Lo que hace Python: Adentro de la función, suma 4 + 7, lo que da 11.
    
    # 1. Lo que hace Python es que lee las lineas pero no las ejecuta. Solo toma nota en su memoria.

morning_distance = 4
evening_distance = 7
    # 2. Creación de las cajas de datos. Lo que hace Python es crear dis variables (cajas) en la memoria 
    # global de la computadora.
    
    # 3. El gran salto a la función. Python ve 3l nombre de la dunción con paréntesis, lo que significa: 
    # "¡Es hora de trabajar!"
    # Python toma los valores que estaban en las cajas globales (4 y 7) y viaja (salta) de regreso a la línea 1.
    # •  Al entrar a la función, los números se renombran en variables locales temporales:
	#       • first_distance ahora vale 4.
	#       • second_distance ahora vale 7.
total_distance = combine_distances(morning_distance, evening_distance)
    # 5. • Lo que hace Python: El signo de igual (=) atrapa el número 11 que traía el mensajero y lo guarda 
    # de forma permanente en una nueva caja global llamada total_distance.

print(total_distance)
    # 6. Lo que hace Python: Abre la caja total_distance, ve que tiene un 11 y lo proyecta en la pantalla de tu juego. 
    # El programa termina con éxito.