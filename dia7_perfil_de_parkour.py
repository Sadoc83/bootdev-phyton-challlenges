# =========================================================
# Día 7 - Perfil de parkour
# Clompletar estas dos funciones usando def y return. No imprima los resultados.
# =========================================================

# Cada función debe devolver un único resultado. No imprimas nada dentro de las funciones.

# Ejemplo
# calculate_jump_score(8, 5)
# 21

# calculate_sprint_score(6, 4)
# 22

def calculate_jump_score(leg_power, balance):
    pass


def calculate_sprint_score(speed, stamina):
    pass

# =========================================================
# Solución paso a paso

def calculate_jump_score(leg_power, balance):
    # El doble de la potencia de la pierna más el balance
    return (leg_power * 2) + balance

def calculate_sprint_score(speed, stamina):
    # Tres veces la velocidad más la resistencia
    return (speed * 3) + stamina


# 📊 Comprobando el resultado con el ejemplo:

# • Si ejecutamos calculate_jump_score(8, 5), Python calcula (8 * 2) + 5, 
# lo que da 21. ¡Coincide perfectamente!
# • Si ejecutamos calculate_sprint_score(6, 4), Python calcula (6 * 3) + 4, 
# lo que da 22. ¡Exacto!

# ---------------------------------
# Jump stats: leg power=8, balance=5
# Sprint stats: speed=6, stamina=4

# Expected jump score:   21
# Actual jump score:     21
# Expected sprint score: 22
# Actual sprint score:   22
# Pass
# ---------------------------------
# Jump stats: leg power=12, balance=3
# Sprint stats: speed=9, stamina=7

# Expected jump score:   27
# Actual jump score:     27
# Expected sprint score: 34
# Actual sprint score:   34
# Pass
# ============= PASS ==============
# 2 passed, 0 failed, 3 skipped
