# =========================================================
# Día 8 - Total del carrito de compras
# =========================================================

# Complete ambas funciones en main.py:

# calculate_subtotal(prices)Devuelve la suma de todos los precios en el carrito. Un carrito vacío tiene un subtotal de 0.
# calculate_total(prices, discount)Devuelve el subtotal después de restar un descuento fijo. El resultado nunca debe ser menor que 0.
# Utilice defesta función para definir cada una de sus funciones y una returninstrucción explícita para devolver cada resultado.

# Por ejemplo:

# prices = [12, 8, 5]

# calculate_subtotal(prices)
# 25

# calculate_total(prices, 7)
# 18

# Un descuento mayor que el subtotal reduce el total a 0:

# calculate_total([4, 6], 15)

def calculate_subtotal(prices):
    pass


def calculate_total(prices, discount):
    pass
# =========================================================
# Solución paso a paso:

def calculate_subtotal(prices):
    
    return sum(prices)
    # Sumamos todos los elementos de la lista de precios


def calculate_total(prices, discount):
            # 1. Calculamos el subtotal usando nuestra función anterior
    subtotal = calculate_subtotal(prices)
           
            # 2. Restamos el descuento
    total_con_descuento = subtotal - discount

            # 3. Aseguramos que el total no sea menor que 0
            # Si el total es menor a 0, devolvemos 0. Si no, devolvemos el total.
    if total_con_descuento < 0:
        return 0
    return total_con_descuento
    

# 📊 Comprobando el flujo con los ejemplos:

# • Si corremos calculate_subtotal([12, 8, 5]), 
#   la función sum() procesa la lista y nos devuelve 25.
# • Si corremos calculate_total([12, 8, 5], 7), 
#   el subtotal es 25, restamos 7 y nos da 18. max(0, 18) devuelve 18.
# • Si corremos el caso del descuento gigante calculate_total([4, 6], 15), el subtotal es 10. 
#   Al restar 15 nos da -5. Como max(0, -5) evalúa cuál es mayor, elige el 0. 
#   ¡Funciona a la perfección!