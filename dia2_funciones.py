# =========================================================
# Funciones nos permiten reutilizar y organizar el código. 
# =========================================================

def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


sword_length = 1.0
spear_length = 2.0

# don't touch above this line

sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

# don't touch below this line

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")


# =========================================================
# Múltiples parámetros
# Las funciones pueden tener múltiples parámetros ("parámetro" es una forma elegante de decir "entrada"). Por ejemplo, esta subtractfunción acepta 2 parámetros: ay b.
# =========================================================

def subtract(a, b):
    result = a - b
    return result

def triple_attack(damage_one, damage_two, damage_three):
    total_damage = damage_one + damage_two + damage_three
    return total_damage


# Don't touch below this line

# This is the first triple attack
attack_one = 2
attack_two = 4
attack_three = 3
first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)

print("Getting damage for", attack_one, attack_two, "and", attack_three, "...")
print(first_triple_attack_damage, "points of damage dealt!")
print("=====================================")

# This is the second triple attack
attack_four = -1
attack_five = 10
attack_six = 5
second_triple_attack_damage = triple_attack(attack_four, attack_five, attack_six)

print("Getting damage for", attack_four, attack_five, "and", attack_six, "...")
print(second_triple_attack_damage, "points of damage dealt!")
print("=====================================")


# =========================================================
# Impresión vs. Devolución
# Algunos desarrolladores novatos se quedan atascados en la diferencia entre print() y return.
# =========================================================

def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return(title)


# Don't touch below this line


def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")


# =========================================================
# Dónde declarar funciones
# Las funciones pueden declararse en cualquier lugar de un archivo de Python, pero deben declararse
# =========================================================

def main():
    print("Fantasy Quest is booting up...")
    print("Game is running!")

    main()


# =========================================================
# Orden de las funciones
# Todas las funciones deben definirse antes de ser utilizadas.
# =========================================================

def main():
    health = 10
    armor = 5
    add_armor(health, armor)


def add_armor(h, a):
    new_health = h + a
    print_health(new_health)


def print_health(new_health):
    print(f"The player now has {new_health} health")


# call entrypoint at the end
main()

def to_celsius(f):
    return 5/9 * (f - 32)


## Don't touch below this line

# Esta formula funciona para calcular la temperatura en grados Celsius a partir de la temperatura en grados Fahrenheit. La fórmula es: C = 5/9 * (F - 32)

def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")


test(100)
test(88)
test(104)
test(112)


# =========================================================
# ¿Cuántas veces se calculate_damagellama a la función y dónde se almacenan los resultados? R=3
# calculate_damage(...): ¿qué nombre de variable recibe el valor devuelto en cada una de esas tres llamadas? R=stab_damage, slash_damage, fireball_damage
# =========================================================

def calculate_damage(opening_attack, core_damage, finishing_move):
    total = opening_attack + core_damage + finishing_move
    return total


stab_damage = calculate_damage(10, 20, 30)
slash_damage = calculate_damage(5, 10, 15)
fireball_damage = calculate_damage(50, 60, 70)
print(stab_damage)
print(slash_damage)
print(fireball_damage)


# =========================================================
# Convertir horas a segundos
# =========================================================

def hours_to_seconds(hours):
    return hours * 3600


# Don't touch below this line


def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(25)
test(100)
test(33)


# =========================================================
# Ningún retorno
# Cuando no se especifica ningún valor de retorno en una función, esta devolverá automáticamente None.
# =========================================================

def my_func():
    print("I do nothing")
    return None

def my_func():
    print("I do nothing")
    return

def my_func():
    print("I do nothing")

# Si imprimimos el valor devuelto, vemos que es None.

result = my_func()
# I do nothing

print(result)
# None

# =========================================================
# Múltiples valores de retorno
# Una función puede devolver más de un valor separándolos con comas.
# =========================================================

def become_warrior(full_name, power):
    title = f"{full_name} the warrior"
    new_power = power + 1
    return title, new_power


# Don't edit below this line


def main():
    test("Frodo Baggins", 5)
    test("Bilbo Baggins", 10)
    test("Gandalf The Grey", 9000)


def test(input1, input2):
    result1, result2 = become_warrior(input1, input2)
    print(result1, "has a power level of:", result2)


main()


# =========================================================
# Parámetros frente a argumentos
# Los parámetros son los nombres que se utilizan para las entradas al definir una función. 
# Los argumentos son los valores de las entradas que se proporcionan cuando se llama a una función.
# =========================================================

# a and b are parameters
def add(a, b):
    return a + b


# 5 and 6 are arguments
sum = add(5, 6)

# =========================================================
# Valores predeterminados de los parámetros
# Puedes especificar un valor predeterminado para un parámetro de función, 
# lo cual es útil cuando una función tiene parámetros "opcionales". 
# Estos se crean utilizando el =operador de asignación ( ) dentro de la firma de la función.
# =========================================================

# ejemplo de función con un parámetro opcional:
def get_greeting(email, name="there"):
    print(f"Hello {name}, welcome! You've registered your email: {email}")

#Ejercicio: crea una función que calcule el daño de un ataque, con un parámetro opcional para la armadura del jugador.
def get_punched(health, armor=0):
    damage= 50 - armor
    return health - damage 


def get_slashed(health, armor=0):
    damage= 100 - armor
    return health - damage 


# Don't touch below this line


def test(health, armor):
    print(f"Running tests for health {health} and armor {armor}")
    print("========================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("----------------------------------------\n")


test(400, 5)
test(300, 3)
test(200, 1)


def curse(weapon_damage):
    # 1. Calculamos la maldición menor (50% del daño original)
    lesser_cursed = weapon_damage * 0.5
    
    # 2. Calculamos la maldición mayor (25% del daño original)
    greater_cursed = weapon_damage * 0.25
    
    # 3. Devolvemos ambos resultados en el orden exacto
    return lesser_cursed, greater_cursed

# Don't modify below this line

# Ejemplo de uso de la función curse, extra.
# El lesser_curseddaño: reducir la entrada weapon_damageal 50% de su valor original (una reducción del 50%).
# El greater_curseddaño: reducir la entrada weapon_damageal 25% de su valor original (una reducción del 75%).

def test(weapon_damage):
    print("Weapon's base damage:", float(weapon_damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    print("=====================================")


def main():
    test(100)
    test(500)
    test(1000)


main()


#  Enchant and Attack, ejemplo de uso de la función curse, extra +1.

def enchant_and_attack(target_health, damage, weapon):
    # 1. Calculamos el daño encantado (+10 de poder)
    enchanted_damage = damage + 10
    
    # 2. Calculamos la salud restante del enemigo
    new_health = target_health - enchanted_damage
    
    # 3. Creamos el nombre del arma encantada usando f-strings
    enchanted_weapon = f"enchanted {weapon}"
    
    # 4. Devolvemos el nombre del arma y la nueva vida en ese orden
    return enchanted_weapon, new_health


# Don't modify below this line


def test(target_health, damage, weapon):
    print(f"The target has {target_health} health.")
    print(f"{weapon} base damage: {damage}... Enchanting and attacking.")
    enchanted_weapon, new_health = enchant_and_attack(target_health, damage, weapon)
    print(f"The target has been attacked with the {enchanted_weapon}.")
    print(f"The target has {new_health} health remaining.")
    print("=====================================")


def main():
    test(100, 50, "sword")
    test(500, 100, "axe")
    test(1000, 250, "bow")


main()