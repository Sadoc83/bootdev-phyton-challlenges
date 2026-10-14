# =========================================================
# Día 6 - Construye un sistema de puntuación para máquinas recreativas
# =========================================================

# Completa estas tres funciones:

# * calculate_target_scoreDevuelve los puntos obtenidos al acertar a los objetivos.
# * add_combo_bonusDevuelve una puntuación después de añadir una bonificación por combo.
# * calculate_final_scoreutiliza las otras dos funciones, luego agrega una bonificación por logro y devuelve la puntuación final.
# Las tres funciones deben usar returnsentencias. No imprima los resultados.

# Por ejemplo, con 8objetivos que valen 25puntos cada uno, una 50bonificación de combo de puntos y una 100bonificación de logro de puntos:

# Target score: 200
# Score with combo: 250
# Final score: 350


def calculate_target_score(targets_hit, points_per_target):
    pass


def add_combo_bonus(target_score, combo_bonus):
    pass


def calculate_final_score(
    targets_hit, points_per_target, combo_bonus, achievement_bonus
):
    pass

# =========================================================
# Solución paso a paso

def calculate_target_score(targets_hit, points_per_target):
    return targets_hit * points_per_target

# Paso 1: Calcular la puntuación por objetivos (calculate_target_score)

# • El problema: Necesitamos saber cuántos puntos hicimos solo por golpear objetivos. 
#   Nos dan cuántos golpeamos (targets_hit) y cuánto vale cada uno (points_per_target).
# • Toma de decisiones: Si destruyes 8 objetivos y cada uno vale 25 puntos, la operación 
#   lógica es una multiplicación (*).
# • Resultado: Multiplicamos ambos valores y usamos return para enviar el resultado hacia afuera.

def add_combo_bonus(target_score, combo_bonus):
    return target_score + combo_bonus


# Paso 2: Añadir el combo (add_combo_bonus)

# • El problema: Tomar una puntuación que ya tenemos (target_score) y sumarle un extra por haber 
#   hecho una racha o combo (combo_bonus).
# • Toma de decisiones: Al ser una bonificación adicional directa sobre una puntuación existente, 
#   la operación correcta es una suma (+).
# • Resultado: Sumamos la puntuación base más el bono de combo y lo devolvemos.

def calculate_final_score(
    targets_hit, points_per_target, combo_bonus, achievement_bonus
):
    base_score = calculate_target_score(targets_hit, points_per_target)
    score_with_combo = add_combo_bonus (base_score, combo_bonus)
    return score_with_combo + achievement_bonus


# Paso 3: El "gran Gran FINale" ... el puntaje final (calculate_final_score)

# Este es el paso más interesante porque conecta todo lo anterior. El ejercicio pide explícitamente 
#   que se utilice las otras dos funciones.
# • Toma de decisiones:
#	1. En lugar de volver a escribir la multiplicación, llamamos a la primera función: 
#   calculate_target_score(targets_hit, points_per_target). Guardamos ese resultado en una variable 
#   llamada base_score.
#	2. Ahora que tenemos la base, usamos la segunda función para añadir el combo. Le pasamos 
#   nuestra base_score y el combo_bonus: add_combo_bonus(base_score, combo_bonus). 
#   Guardamos esto en score_with_combo.
#	3. Finalmente, las instrucciones dicen que a ese resultado con combo hay que sumarle el 
#   bono por logros (achievement_bonus). Hacemos la suma final y usamos return para entregar 
#   el gran total.


