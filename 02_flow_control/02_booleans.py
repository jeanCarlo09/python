###
# 02 - Booleans
# Valores lógicos: True o False
# Fundamentales para el control de flujo y la lógica en programación.
###

import os # Forma de importar módulos en Python
os.system('clear') # Se utiliza el comando 'clear' para limpiar la consola en sistemas Unix/Linux. En Windows se usa 'cls'.

# Operadores de comparación en Python
# ==  Igualdad
# !=  Desigualdad
# >   Mayor que
# <   Menor que
# >=  Mayor o igual que
# <=  Menor o igual que


# Las comparaciones de cadenas de texto en Python son lexicográficas.
# Se comparan carácter por carácter y es case sensitive, siguiendo el orden alfabético.

print("manzana" < "pera") # True, verifica una a una hasta encontrar una diferencia
print("manzana" == "pera") # True
print("Hola" == "hola") # True

# Tablas de verdad
# AND (Y)
# True and True = True
# True and False = False
# False and True = False
# False and False = False

# OR (O)
# True or True = True
# True or False = True
# False or True = True
# False or False = False

# NOT (NO)
# not True = False
# not False = True

# Tablas de verdad (para referencia):
print("\nTablas de verdad:")
print("\nand:")
print("A     B     A and B")
print("True  True ", True and True)
print("True  False", True and False)
print("False True ", False and True)
print("False False", False and False)

print("\nor:")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)

print("\nnot:") 
print("A     not A")
print("True ", not True)
print("False", not False)