# =========================================================
# Día 5 - 3 Desafío de funciones simples
# Completa las tres funciones en main.py.
# Cada función debe usar la def instrucción, aceptar los parámetros 
# mostrados y usar return para devolver el valor correcto.
# =========================================================

# La tareas
# add_tokens(current_tokens, bonus_tokens)debería devolver el total después de sumar los dos números
# build_team_name(city, mascot)debería devolver las dos cadenas unidas por un espacio entre ellas.
# spend_coins(coins, cost)debe devolver el número de monedas restantes después de restar costdecoins
# Las llamadas proporcionadas print()pondrán a prueba sus funciones.

# Salida esperada
# Cuando se ejecute tu código, debería imprimir exactamente:
# 20
# Solar Squad
# 16

def add_tokens(current_tokens, bonus_tokens):
    pass


def build_team_name(city, mascot):
    pass


def spend_coins(coins, cost):
    pass


print(add_tokens(14, 6))
print(build_team_name("Solar", "Squad"))
print(spend_coins(25, 9))

# =========================================================
# Solución paso a paso

def add_tokens(current_tokens, bonus_tokens):
    return current_tokens + bonus_tokens 
# • ¿Qué operación matemática une dos cantidades? La adición (+).
# • ¿Necesitamos guardar el resultado en una variable antes? 
# Podríamos hacer total = current_tokens + bonus_tokens y luego return total. 
# Sin embargo, como es una operación simple, la decisión más eficiente es sumar y 
# devolver el valor directamente en la misma línea.


def build_team_name(city, mascot):
    return f"{city} {mascot}" 
# • Opción 1 (Concatenación tradicional): city + " " + mascot. Funciona, pero si tienes muchos 
#   textos, se vuelve confuso de leer debido a tantos signos + y comillas.
# • Opción 2 (Cadenas formateadas o f-strings): En Python, anteponer una f a las comillas (f"...") 
#   te permite incrustar variables directamente dentro del texto usando llaves {}. Decidimos usar f-strings 
#   porque es el estándar moderno en la industria, es mucho más limpio visualmente y evita errores de espacios.


def spend_coins(coins, cost):
    return coins - cost
# • Cuando "gastas" o "quitas" algo de un total, la operación lógica es la resta (-).
# • El orden importa: a las monedas que ya tienes le restas el costo, por lo que escribimos 
#   coins - cost.

print(add_tokens(14, 6))
print(build_team_name("Solar", "Squad"))
print(spend_coins(25, 9))