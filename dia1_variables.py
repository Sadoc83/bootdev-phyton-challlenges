# =========================================================
# Variables, almacenan datos mientras se ejecuta nuestro programa.
# =========================================================
player_health= 1000
print(player_health)


# =========================================================
# Las Variables, pueden contener cualquier valor y ese valor puede cambiar
# =========================================================

player_health = 1000

player_health = 900

print(player_health)

player_health = 800
print(player_health)

player_health = 700
print(player_health)

player_health = 600

print(player_health)

# =========================================================
# Matematicas: my_sum = a + b | my_difference = x - y | my_product = c * d | my_quotient = a / b
# =========================================================

player_health = 1000
armor_multiplier = 2
armored_health = 1000 * 2
print(armored_health)


# =========================================================
# Numeros Negativos
# =========================================================

player_health = 100
poison_damage = -10

player_poison_health = player_health + poison_damage

print(player_poison_health)


# =========================================================
# Tipos basicos de variable
# =========================================================

player_health = 100

player_has_magic = True

print("player_health is a/an", type(player_health).__name__)
print("player_has_magic is a/an", type(player_has_magic).__name__)


# =========================================================
# Cadenas F en Python, Ejercicio 1
# =========================================================

name = "Yarl"
age = 37
race = "dwarf"

print(f"{name} is a {race} who is {age} years old.")


# =========================================================
# Variables de tipo None
# =========================================================

enemy = None

print(enemy is None)


# =========================================================
# Matematicas con cadenas de caracteres
# =========================================================

sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# Don't edit above this line

print(sentence_start + player1_health + sentence_end)
print(sentence_start + player2_health + sentence_end)


# =========================================================
# Concatenacion de cadenas con operador +, Ejercicio 2
# =========================================================

player_name = "Charles"
greeting = "Well met,"
quest_start = "The local mine has been taken over by orcs!"
quest_end = "We need your help taking it back."
space = " "

# don't touch above this line

complete_greeting = greeting + space + (player_name)
print(complete_greeting)
print(quest_start)
print(quest_end)


# =========================================================
# Concatenacion de cadenas con operador + y calculo del promedio /, Ejercicio 3
# =========================================================

game_one_score = 97
game_two_score = 92
game_three_score = 106
game_four_score = 105

# Don't touch above this line

average_score = (game_one_score + game_two_score + game_three_score + game_four_score) / 4

# Don't touch below this line

print(round(average_score))


# =========================================================
# Informe de personaje con distintas sintaxis de los atributos, Ejercicio 4
# =========================================================

name = "Lopen"
level = 25
character_class = "Windrunner"
magic_resistance = 10.5
account_active = True

# Don't edit below this line

print("Character Report")
print(f"{name} is a level {level} {character_class}.")
print(f"They have {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

print("=========================")
print("Character Report Complete")
print("Data types:")
print(
    f"name: {type(name).__name__}, level: {type(level).__name__}, character_class: {type(character_class).__name__}"
)
print(f"magic_resistance: {type(magic_resistance).__name__}")
print(f"account_active: {type(account_active).__name__}")
