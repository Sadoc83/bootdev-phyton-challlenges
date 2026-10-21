# =========================================================
# Día 12 - Implementar mapa, filtro y reducción personalizados
# =========================================================

# En el ejercicio de hoy, me enfrentaré a un desafio que amerita estudiarlo, sufrirlo y resolverlo.
# ... vamos pues!!!

# =========================================================
# Escribe tres funciones: my_map , my_filter, y my_reduce.

# Estos deberían comportarse de forma similar a los integrados de Python map, filter, y functools.reduce, 
# pero deben devolver listas regulares de Python (para my_mapy my_filter).

# Se Trabajarán con funciones de primera clase y funciones de orden superior :

# Una función de primera clase es una función que se puede almacenar en una variable, pasar como argumento o 
# devolver desde otra función.
# Una función de orden superior es una función que toma otra función como argumento o devuelve una función.
# En este desafío, my_map, my_filter, y my_reduceson funciones de orden superior porque toman otras funciones 
# como entradas.

# Utilice funciones regulares o funciones anónimas ( lambdaexpresiones de Python) cuando le resulte útil.

# Requisitos

# 1.my_map(function, iterable)
# Recibe una función y un iterable (como una lista).
# Llamadas function(item)para cada uno itemen iterable.
# Devuelve una nueva lista con todos los resultados, en orden.
# Ejemplo:

# from main import my_map

# numbers = [1, 2, 3]
# result = my_map(lambda n: n * n, numbers)
# print(result)
# [1, 4, 9]

# 2.my_filter(function, iterable)
# Recibe una función y un iterable.
# Llamadas function(item)para cada uno item.
# Si el resultado es verdadero (como Trueuna cadena no vacía o un número distinto de cero), conserve el elemento.
# Devuelve una nueva lista de los elementos que superaron la prueba, en su orden original.
# Ejemplo:

# from main import my_filter

# words = ["hi", "there", "a", "wizard"]
# result = my_filter(lambda w: len(w) > 2, words)
# print(result)
# ["there", "wizard"]

# 3.my_reduce(function, iterable, initial=None)
# Combina todos los elementos en iterableun único valor.
# function(accumulator, item)Se llama repetidamente para actualizar el acumulador.
# Si initialse da :
# Comience accumulatorcomo initial.
# Procesar todos los elementos en iterable.
# Si no initialse proporciona ( initiales Nonepor defecto):
# Utilice el primer elemento iterablecomo acumulador inicial.
# Luego procese el resto de los elementos.
# Devuelve el valor final del acumulador.
# Casos extremos:

# Si iterableestá vacío y no initialse proporciona :
# Crea una incidencia TypeErrorcon este mensaje exacto:
# "my_reduce() of empty sequence with no initial value"
# Si iterableestá vacío y initial se proporciona :
# Devolver initial.
# Ejemplo:

# from main import my_reduce

# numbers = [1, 2, 3, 4]

# sum_result = my_reduce(lambda acc, n: acc + n, numbers)
# print(sum_result)
# 10

# product_result = my_reduce(lambda acc, n: acc * n, numbers, 1)
# print(product_result)
# 24

# Detalles de implementación
# No utilice los elementos integrados map, filter, o functools.reducedentro de sus implementaciones.
# Utilice forbucles sencillos para construir los resultados.
# No utilices comprensiones de listas en tus soluciones.
# Puedes suponer que iterablees algo que puedes recorrer en un bucle una sola vez, como una lista.

# Resumen
# Implementa estas tres funciones en main.py:

# my_map(function, iterable)→ lista de valores mapeados
# my_filter(function, iterable)→ lista de elementos que pasaron la prueba
# my_reduce(function, iterable, initial=None)→ valor reducido único, con el comportamiento en casos 
# límite descrito anteriormente
# Las pruebas llamarán a estas funciones con diferentes lambdaexpresiones y listas de entrada.

# =========================================================
# Repuesta paso a paso

def my_map(function, iterable):
    # 1. Creamos una lista vacía para almacenar las transformaciones
    result = []
    # 2. Recorremos cada elemento del iterable
    for item in iterable:
        # 3. Aplicamos la función al elemento y guardamos el resultado
        mapped_item = function(item)
        result.append(mapped_item)
    # 4. Devolvemos la nueva lista transformada
    return result


def my_filter(function, iterable):
    # 1. Creamos una lista vacía para los elementos que pasen la prueba
    result = []
    # 2. Recorremos cada elemento del iterable
    for item in iterable:
        # 3. Evaluamos el elemento con la función condicional
        if function(item):
            result.append(item)
    # 4. Devolvemos la lista filtrada
    return result


def my_reduce(function, iterable, initial=None):
    # Convertimos a lista para manejar los índices y verificar si está vacío
    items = list(iterable)
    
    # --- CASOS EXTREMOS (Manejo de listas vacías) ---
    if len(items) == 0:
        if initial is None:
            # Si está vacío y no hay valor inicial, lanzamos el error exacto exigido
            raise TypeError("my_reduce() of empty sequence with no initial value")
        # Si está vacío pero hay valor inicial, devolvemos el inicial
        return initial

    # --- FLUJO PRINCIPAL ---
    if initial is not None:
        # Si nos dan un valor inicial, el acumulador arranca con él
        accumulator = initial
        start_index = 0
    else:
        # Si initial es None, el acumulador arranca con el primer elemento de la lista
        accumulator = items[0]
        start_index = 1  # Empezamos a procesar desde el segundo elemento

    # Recorremos el resto de los elementos basándonos en el índice de inicio
    for item in items[start_index:]:
        # Actualizamos el acumulador llamando a la función con sus dos ingredientes
        accumulator = function(accumulator, item)
        
    return accumulator

---------------------------------
Case:  map_squares
Input: [1, 2, 3]

Expected: [1, 4, 9]
Actual:   [1, 4, 9]
Pass
---------------------------------
Case:  filter_even
Input: [1, 2, 3, 4, 5, 6]

Expected: [2, 4, 6]
Actual:   [2, 4, 6]
Pass
---------------------------------
Case:  reduce_sum_with_initial
Input: [5, 10, 15]

Expected: 30
Actual:   30
Pass
---------------------------------
Case:  map_to_strings
Input: [2, 4, 6]

Expected: ['lvl 2', 'lvl 4', 'lvl 6']
Actual:   ['lvl 2', 'lvl 4', 'lvl 6']
Pass
---------------------------------
Case:  filter_long_words
Input: ['a', 'dragon', 'hi', 'sorcerer']

Expected: ['dragon', 'sorcerer']
Actual:   ['dragon', 'sorcerer']
Pass
---------------------------------
Case:  reduce_max_no_initial
Input: [7, 3, 9, 2, 9, 1]

Expected: 9
Actual:   9
Pass
============= PASS ==============
6 passed, 0 failed


# 🕵️‍♂️ Análisis a detalle y Toma de Decisiones Paso a Paso

# Para avanzar al nivel profesional en programación 🧐 (oiloooo ... jajaja), 
# veamos el razonamiento detrás de cada bloque: 

# 1. Recreando la transformación (my_map)

# • El problema: Tomar una lista y aplicarle una fórmula a cada elemento uno por uno, 
#   devolviendo una lista idéntica en tamaño pero modificada.
# • Toma de decisiones: Necesitamos recolectar las respuestas. La mejor estructura para ir acumulando 
#   en orden es una lista vacía (result = []). Mediante un bucle for, extraemos el ingrediente, se lo pasamos 
#   a function(item) y lo inyectamos con .append().

# 2. Recreando el colador matemático (my_filter)

# • El problema: Recorrer un iterable y conservar únicamente los datos que cumplan con una condición verdadera 
#   (por ejemplo, palabras con más de 2 letras).
# • Toma de decisiones: La lógica es idéntica a my_map, pero con un guardián de entrada: un bloque if function(item):. 
#   Recuerda la lección de Truthiness del Día 11: Python no solo evalúa si da True estricto; si la función 
#   devuelve un número que no es cero o un texto con letras, Python lo tomará como verdadero y meterá el elemento 
#   al colador.

# 3. El titán modular (my_reduce)

# Este es el desafío más complejo debido a sus reglas especiales e interacciones con el inventario (el acumulador).
# • Pasos intermedios y casos extremos:

#	• Paso A (Evitar errores ocultos): Al hacer items = list(iterable), nos aseguramos de poder medir cuántos 
#       elementos tiene el grupo usando len(). Si está vacío y no nos dieron un escudo (initial), usamos 
#       raise TypeError(...) con el texto exacto pedido para detener el juego con una alerta controlada.
#	
#   • Paso B (La bifurcación del acumulador): Si hay un valor initial, este se convierte en el cimiento de 
#       nuestra suma/producto (accumulator = initial), evaluando la lista desde la posición 0. Si no hay valor 
#       inicial, las reglas dictan que el primer elemento de la lista toma ese rol, por lo que debemos alterar 
#       nuestro punto de partida al índice 1 (items[1:]) para no duplicar el primer dato en la operación.
#	
#   • Paso C (La reducción): En cada ciclo del bucle, la función procesa dos cosas a la vez: lo que llevamos 
#       guardado hasta el momento (accumulator) y el elemento nuevo (item).
    