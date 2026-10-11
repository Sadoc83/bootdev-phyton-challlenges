# =========================================================
# Alcance
# El ambito de la clase se refiere a dónde está disponible una variable o función. 
# Por ejemplo, cuando creamos variables dentro de una función (como al asigniar nuestos parámetros),
# esos datos no están disponibles fuera de esa función.
# =========================================================

# ejemplo de alcance de variables en funciones

def subtract(x, y):
    return x - y


result = subtract(5, 3)
print(x)
# ERROR! "name 'x' is not defined"

# Ejercicio: Alcance de variables en funciones
def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

# don't touch above this line

# ¡Corregimos los nombres de las variables aquí!
max_health = get_max_health(my_modifier, my_level)

# don't touch below this line

print(f"max_health is: {max_health}")


*📊 Lo que imprimirá la pantalla de tu juego:

#Una vez corregido, la función recibirá el 5 y el 10, los multiplicará y la terminal mostrará el total de vida de tu personaje:
#• max_health is: 50
#¡Y con esto has conquistado el concepto del alcance de variables! ⚔️💎

# =========================================================
# Alcance Global
# Cuando definimos una variable o una función, ese nombre es accesible en cualquier otro lugar de nuestro programa, 
# incluso dentro de otras funciones.
# =========================================================

#ejemplo de alcance global

pi=3.14159
def get_area_of_circle(radius):
    return pi * radius * radius

# Dado que pi se declaró en el ámbito"blobal" principal, se puede utilizar dentro de la get_area_of_circle() función.

# Ejercicio: Alcance global, declararemos la variable player_level en la parte superior del ámbito global y se asignará el valor 4.

player_level = 4

# Don't touch below this line


def calculate_health(modifier):
    return player_level * modifier


def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level


print(f"Character has {calculate_health(10)} max health.")

print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")


# 📊 Lo que imprimirá la pantalla de tu juego (si usas el valor 1):

# Una vez que las funciones puedan leer el nivel global del jugador, la terminal calculará todo con éxito:
# • Character has 10 max health. (1 * 10)
# • Character has 12 primary stats. (3 + 8 + 1)
# ¡Y habrás desbloqueado otra valiosa lección sobre variables globales! ⚔️💎

# Conclusión del Alcance de Variables
# El alcance de una variable se refiere a dónde está disponible esa variable en el código.

pi = 3.14


def get_area_of_circle(radius):
    area = pi * radius * radius
    return area

#1. ¿Tiene la función get_area_of_circle acceso a la variable pi?
# Sí, sí tiene acceso. Como la variable pi está declarada en la parte más externa del código (el ámbito global), 
# cualquier función que esté abajo puede verla y usar su valor sin ningún problema.

#2. Sin devolverla, ¿se puede acceder a la variable area dentro de la función fuera de la misma?
# No, no se puede. La variable area es una variable local. Nace y muere estrictamente adentro de la caja de la función 
# get_area_of_circle. Si intentas escribir print(area) en el código global (afuera de la función), Python se romperá y 
# te dará un error porque no sabe qué es area en el mundo exterior. La única forma de sacar ese valor al exterior es 
# usando la palabra clave return.