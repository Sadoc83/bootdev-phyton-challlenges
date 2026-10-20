# =========================================================
# Día 10 - Planifica la cosecha
# =========================================================


# Completa ambas funciones utilizando múltiples valores de retorno.

# divide_harvest
# Los datos de entrada son el peso cosechado en kilogramos y los porcentajes reservados para semillas y para la venta.

# Devuelva estos tres pesos, en orden:

# 1. La cantidad reservada para semillas.
# 2. La cantidad reservada para la venta.
# 3. La cantidad que queda para almacenamiento.

# Ambos porcentajes se aplican al peso original cosechado . Son no negativos y su suma es como máximo 100.

# plan_harvest
# Los insumos son los mismos, más un precio de venta por kilogramo.

# Llama a divide_harvesty y desempaqueta sus tres valores devueltos en variables separadas. 
# Devuelve estos tres resultados, en orden:

# 1. Los ingresos procedentes de la venta de la parte correspondiente a la venta.
# 2. El peso reservado para las semillas.
# 3. El peso restante para almacenamiento.

# No redondee los resultados.

# Ejemplo
# Para una cosecha de 200kilogramos, 10porcentaje para semillas, 60porcentaje para la venta y un precio de 3por kilogramo:

# divide_harvestdevuelve 20, 120, y 60.
# plan_harvestdevuelve 360, 20, y 60.

def divide_harvest(harvest_kg, seed_percent, sale_percent):
    pass


def plan_harvest(harvest_kg, seed_percent, sale_percent, price_per_kg):
    pass

# =========================================================
# Solución paso a paso:

def divide_harvest(harvest_kg, seed_percent, sale_percent):
    
    #1 Calcular el peso para semillas (porcentaje del peso total)
    seed_kg = harvest_kg * (seed_percent / 100)
    
    #2 Calcular el peso para la venta (porcentaje del peso total)
    sale_kg = harvest_kg * (sale_percent / 100)

    #3 Calcular el peso sobrante para almacenamiento (peso total menos semillas y venta)
    storage_kg = harvest_kg - seed_kg - sale_kg

    #4 Devolver los tres valores en el orden exacto solicitado: semillas, venta, almacenamiento
    return seed_kg, sale_kg, storage_kg

def plan_harvest(harvest_kg, seed_percent, sale_percent, price_per_kg):

    #1 Llamar a divide_harvest y desempaquetar sus tres valores devueltos
    seed_kg, sale_kg, storage_kg = divide_harvest(harvest_kg, seed_percent, sale_percent)

    #2 Calcular los ingresos de la venta (peso vendido por precio por kilogramo)
    sale_revenue = sale_kg * price_per_kg

    #3 Devolver los resultados en el nuevo orden requerido
    return sale_revenue, seed_kg, storage_kg


# 📋 Explicación paso a pasito y toma de decisiones

# Vamos a desglosar el proceso de pensamiento de forma súper explícita para que veas cómo se conectan 
# los cables matemáticos y lógicos:

# 🛑 Función 1: divide_harvest

# Esta función recibe la cosecha total y dos porcentajes enteros (por ejemplo, 10 para el 10% y 60 para el 60%).
# 1. Conversión matemática de porcentajes:
# En matemáticas, para aplicar un porcentaje, primero debemos dividir el número entre 100 
# (ej. 10 / 100 = 0.1 o 60 / 100 = 0.6). Luego, multiplicamos ese decimal por el peso original (harvest_kg).
#	• Semillas: seed_kg = harvest_kg * (seed_percent / 100)
#	• Venta: sale_kg = harvest_kg * (sale_percent / 100)
# 2. Calcular el almacenamiento (Resto):
# El problema te dice que el almacenamiento es lo que queda. La decisión lógica aquí es tomar el peso original de la cosecha y restarle lo que ya apartamos para semillas y para venta.
#	• storage_kg = harvest_kg - seed_kg - sale_kg
# 3. Múltiple retorno en orden:
# Python nos permite regresar varias variables separándolas con comas en una sola línea. 
# Las instrucciones exigen un orden estricto: primero semillas, luego venta y al final almacenamiento.
#	• return seed_kg, sale_kg, storage_kg

# 🛑 Función 2: plan_harvest

# Esta función es la "orquestadora". Recibe los mismos datos más el precio por kilo, y 
# pide explícitamente reutilizar la función anterior.

# 1. Desempaquetado de tuplas (El truco Pro):
# Como sabemos que divide_harvest nos avienta 3 resultados en sus manos de regreso, nosotros podemos 
# crear 3 variables separadas por comas a la izquierda de un signo = para atraparlas al mismo tiempo:
# 	• seed_kg, sale_kg, storage_kg = divide_harvest(...)

# 2. Calcular ingresos (sale_revenue):
# Para saber cuánto dinero ganamos, multiplicamos los kilogramos que destinamos a la venta 
# (sale_kg, que acabamos de desempaquetar) por el precio de cada kilo (price_per_kg).
# 	• sale_revenue = sale_kg * price_per_kg

# 3. El nuevo orden de retorno:
# ¡Ojo aquí! El acertijo aquí cambia el orden de salida en esta función. 
# Ahora pide: 1° Ingresos, 2° Peso de semillas y 3° Peso de almacenamiento. 

# Acomodemos nuestro return para cumplir la regla al pie de la letra:
#	• return sale_revenue, seed_kg, storage_kg

# 📊 Comprobando con el ejemplo del Arena

# Si pasamos los datos del ejemplo: harvest_kg = 200, seed_percent = 10, sale_percent = 60, price_per_kg = 3

# • divide_harvest:
#	• Semillas: 200 x 0.10 = 20
#	• Venta: 200 x 0.60 = 120
#	• Almacenamiento: 200 - 20 - 120 = 60
#	• Devuelve: 20, 120, 60 (¡Exacto al ejemplo, del ejercicio que aparece en el ejercicio!)

# • plan_harvest:
#	• Recibe los pesos anteriores mediante el desempaquetado.
#	• Ingresos: 120 kg de venta × 3 de precio = 360
#	• Devuelve: 360, 20, 60 (¡Coincide al 100%!)
