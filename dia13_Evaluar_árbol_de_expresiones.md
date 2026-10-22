# Evaluar el árbol de expresiones
Completa la función evaluate.

Se te proporciona un pequeño "lenguaje de calculadora" representado como un árbol de objetos Python. Este árbol es de tipo suma : una expresión ( Expr) puede ser un o Number un .BinaryOp

Utilizarás la instrucción de coincidencia de patrones match de Python para recorrer el árbol y calcular el resultado.

*ref*: https://www.boot.dev/challenges/2e92c949-ccba-4ab5-a217-6110d545d338#:~:text=de%20coincidencia%20de%20patronesmatch

El código de inicio define estos tipos por usted:

            from dataclasses import dataclass
            from enum import Enum, auto
            from typing import Union


            class Op(Enum):
                ADD = auto()
                SUB = auto()
                MUL = auto()


            @dataclass
            class Number:
                value: int


            @dataclass
            class BinaryOp:
                op: Op
                left: "Expr"
                right: "Expr"


            Expr = Union[Number, BinaryOp]

Un Expr es:

* Un Number(value)
* o un BinaryOp(op, left, right)donde
op es uno de Op.ADD, Op.SUB, oOp.MUL
lefty right son valores Expr en sí mismos (por lo que las expresiones pueden anidarse).

## 🗒 Tarea
Implementar:

        def evaluate(expr: Expr) -> int:
            ...

Utilizaremos la coincidencia de patrones y la recursión para calcular el resultado entero del árbol de expresiones.

## Normas
1. Si la expresión es una Number, devuelve su value.
2. Si la expresión es una BinaryOp:
Primero, evalúe recursivamente las expresiones lefty .right
Luego, combine los resultados en función de op:
    * Op.ADD: suma los dos valores
    * Op.SUB: restar derecha de izquierda
    * Op.MUL: multiplicar los valores
3. Todos los valores son enteros (no hay números decimales). Se puede asumir que el árbol es válido y que solo utiliza las tres operaciones definidas.

## Debes usar match/case para ramificar en el tipo de expresión .

### 💡 La coincidencia de patrones permite hacer coincidir directamente la forma de los datos. Por ejemplo:

    match expr:
        case Number(value=v):
            ...
        case BinaryOp(op=Op.ADD, left=l, right=r):
            ...

## Ejemplos
### Número simple
expr = Number(7)
print(evaluate(expr))
# 7

### Suma simple
expr = BinaryOp(Op.ADD, Number(2), Number(3))
print(evaluate(expr))
# 5

### Expresión anidada
Esto construye la expresión:(2 + 3) * (4 - 1)

left = BinaryOp(Op.ADD, Number(2), Number(3))      # (2 + 3)
right = BinaryOp(Op.SUB, Number(4), Number(1))     # (4 - 1)
expr = BinaryOp(Op.MUL, left, right)               # (2 + 3) * (4 - 1)

print(evaluate(expr))
# 15

La función evaluate debería producir estos resultados cuando las pruebas construyan árboles similares.

# 👨🏽‍🏫 Un Árbol de Expresiones (Expression Tree) 
Es simplemente una estructura donde los números están en las puntas (hojas) y las operaciones matemáticas unen esas puntas.

### Entremos en materia y lo haremos detalladamente:

El Concepto: ¿Qué estamos evaluando?
Imaginemos la operación (2 + 3) * (4 - 1). En programación, en lugar de leer texto, lo representamos como un árbol de objetos interconectados: 
    text
          [ * ] (BinaryOp)
         /     \
     [ + ]     [ - ] (BinaryOp)
     /   \     /   \
   [2]   [3] [4]   [1] (Number)
    
    
### Paso 1: La Entrada de la Función


def evaluate(expr: Expr) -> int:

* Qué hace: Esta línea define nuestra función llamada evaluate. Recibe un objeto llamado expr (que puede ser un número o una operación) y promete regresar un número entero (int).
* Por qué lo hace: Necesitamos un punto de entrada que reciba cualquier fragmento del árbol matemático (ya sea el árbol completo o una rama pequeñita) y se encargue de procesarlo.

### Paso 2: El Tablero de Decisiones (match)

    match expr:


* Qué hace: Python toma el objeto expr y abre un bloque de comparación (como un inspector analizando una caja cerrada).
* Por qué lo hace: Como expr puede ser un simple número o una operación compleja, el match nos permite revisar la "forma" o el tipo de dato del objeto para decidir qué camino tomar, sin usar condicionales if tradicionales que se vuelven difíciles de leer en estructuras de árboles.

### Paso 3: El Caso Base (Las Hojas del Árbol)

        case Number(v):
            return v


* Qué hace: El inspector (match) pregunta: "¿Esta caja es un objeto de tipo Number?". Si la respuesta es sí, extrae el número entero que tiene guardado adentro, se lo asigna a la variable temporal v y lo regresa inmediatamente con return v.
* Por qué lo hace: Este es el caso base de nuestra recursión. Los números no tienen operaciones dentro de ellos; son el destino final. Si no tuviéramos esta línea, la función seguiría buscando ramas eternamente y el programa fallaría (un ciclo infinito).

### Paso 4: Las Operaciones y la Magia de la Recursión

Aquí entran las tres líneas de las operaciones, que funcionan bajo la misma lógica. Veamos el ejemplo de la suma:

        case BinaryOp(Op.ADD, l, r):
            return evaluate(l) + evaluate(r)

* Qué hace:
	1. El match detecta que el objeto es una operación binaria (BinaryOp).
	2. Gracias al orden de los datos (forma posicional), Python extrae tres cosas de golpe: confirma que el operador es una suma (Op.ADD), guarda la rama izquierda en la variable l y la rama derecha en la variable r.
	3. Ejecuta evaluate(l) y evaluate(r). Es decir, la función se vuelve a llamar a sí misma para resolver primero los subárboles izquierdo y derecho.
	4. Cuando ambas ramas terminan de resolverse y regresan números reales, la función finalmente los suma (+) y entrega el resultado final.
* Por qué lo hace: En un árbol matemático no puedes sumar un "objeto" con otro "objeto". Tienes que obligar a la computadora a bajar por las ramas (l y r) hasta que encuentre los números (Number). La recursión es perfecta para esto porque va pausando las operaciones de arriba hasta que las ramas de abajo estén resueltas.
Lo mismo ocurre para la resta (-) y la multiplicación (*) en sus respectivas líneas:

        case BinaryOp(Op.SUB, l, r):
            return evaluate(l) - evaluate(r)
        
        case BinaryOp(Op.MUL, l, r):
            return evaluate(l) * evaluate(r)


### Resumen del comportamiento en la mente de Python:

Cuando le pasas una operación como (2 + 3) * (4 - 1):
1. Python entra al match y ve que la raíz principal es un BinaryOp de multiplicación (Op.MUL).
2. Dice: "No puedo multiplicar todavía. Primero voy a ejecutar evaluate en la izquierda (2 + 3) y luego en la derecha (4 - 1)".
3. Al resolver la izquierda, entra a la suma (Op.ADD), baja a las hojas, encuentra el 2 y el 3 (porque caen en el case Number(v)), los suma y obtiene 5.
4. Al resolver la derecha, hace lo mismo con la resta y obtiene 3.
5. Finalmente, regresa al punto de partida (la raíz) con los dos resultados listos y hace 5 * 3, devolviendo 15.

*¡Esa es la razón por la cual este código es tan potente! Con muy pocas líneas 🐍, es capaz de resolver árboles matemáticos gigantescos y superanidados.*