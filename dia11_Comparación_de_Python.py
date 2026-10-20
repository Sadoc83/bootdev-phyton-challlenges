# =========================================================
# Día 11 - Comparación de Python
# =========================================================

# Comparación de Python, ¡qué sorpresa!
# Considere este código Python:

# x = 5

# if x == 1 or 2:
#    print("Condition is True")
# else:
#    print("Condition is False")

# Algunas personas esperan que esto signifique "si x es 1 o 2", pero eso no es lo que hace Python.

# Estos documentos podrían resultarle útiles:

https://docs.python.org/3/reference/expressions.html#boolean-operations
https://docs.python.org/3/reference/expressions.html#comparisons
https://docs.python.org/3/reference/expressions.html#truth-value-testing


# Ideas clave que quizás quieras considerar:

# Cómo "or" combina dos expresiones
# Cómo se tratan los valores no booleanos (números) como " True o False" en las declaraciones "if".
# Cómo escribir comparaciones de forma clara cuando se quiere comprobar varios valores posibles.

#=========================================================
# Respuesta paso a paso

# En Python, la condición if x == 1 or 2: no funciona como el lenguaje humano y casi siempre es un error. 
# (Así que más vale no forzar una interpretación literal de la frase "x es 1 o 2"). 
# En cambio, Python evalúa la condición de manera diferente a lo que uno podría esperar. Esto se debe a 
# las siguientes razones técnicas:

# 1. Cómo evalúa Python la condición realmente

# El operador or divide la línea en dos expresiones completamente independientes a cada lado:
# • Expresión izquierda: x == 1 (Compara si la variable es igual a 1, devolviendo True o False).
# • Expresión derecha: 2 (Un número entero literal aislado).

# Debido a la precedencia de operadores, Python evalúa primero la comparación de la izquierda. 
# Si x no es 1, ese lado se vuelve False. Luego, el operador or pasa a evaluar la expresión de la derecha por sí 
# sola.

# 2. Cómo se evalúa el lado derecho por sí solo (if 2:)

# Si escribiéramos la expresión derecha por separado como if 2:, el código dentro del bloque SÍ se ejecutaría.
# Esto ocurre por la regla de Prueba de Valor de Verdad (Truthiness) de Python: todos los tipos de datos tienen 
# un valor booleano implícito. En el caso de los números enteros, el único número que se evalúa como False es el 
# cero (0). Como el número 2 es distinto de cero, Python lo trata inherentemente como True.

# 💥 Conclusión del fallo

# Como if 2: equivale a if True:, la condición original se reduce a if (False o True) o True:. Al haber un True 
# definitivo en el lado derecho, el operador or hace que toda la condicional sea siempre verdadera, ignorando por 
# completo el valor real de x.

# 🛠️ La forma clara y correcta de expresarlo

# Para solucionar este comportamiento y evaluar correctamente si "x es 1 o 2", se deben usar cualquiera de estas 
# dos alternativas profesionales:

# 1. Comparación explícita: if x == 1 or x == 2: (Evalúa ambas relaciones por separado).
# 2. Operador de pertenencia (Recomendada): if x in (1, 2): (Comprueba de forma limpia si el valor de x está 
# dentro del grupo).

#=========================================================
# Comentario final de Boots - Boot.dev

# ¡Excelente trabajo! Has cubierto ambas partes de la pregunta con claridad.

# Cómo se evalúa: Explicaste que el operador ordivide la condición en dos expresiones independientes, 
# x == 1y 2, y que la comparación de la izquierda se evalúa primero por la precedencia de operadores. 
# 
# Luego señalaste que, según las reglas de veracidad de Python, el único entero que se evalúa como Falsees 0, 
# por lo que 2 siempre es verdadero. Así, la condición completa resulta siempre verdadera, sin importar el valor 
# real de x.

# La forma correcta: O freciste dos alternativas claras:

if x == 1 or x == 2:
    print("Condition is True")

if x in (1, 2):
    print("Condition is True")

# La primera limpia comparamente xcon cada valor, y 
# la segunda usa el operador de pertenencia inpara comprobar si xestá dentro del grupo.

# =========================================================
# Recordatorio: EL IDIOMA DE PYTHON (TRUTHINESS Y OPERADORES)
# =========================================================

    x = 5

# ❌ ERROR COMÚN: Esto siempre da True porque '2' no es cero.
# if x == 1 or 2: 
#     print("Esto siempre se ejecuta")

#  FORMA CORRECTA 1: Comparación explícita
    if x == 1 or x == 2:
        print("x es 1 o 2")

#  FORMA CORRECTA 2 (La más pro): Uso de pertenencia
    if x in (1, 2):
        print("x está en el grupo")