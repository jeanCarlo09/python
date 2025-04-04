###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable
###

import os # Forma de importar módulos en Python
os.system('clear') # Se utiliza el comando 'clear' para limpiar la consola en sistemas Unix/Linux. En Windows se usa 'cls'.


print("\n Bucles (for)")

animals = ["🐶", "🐈", "🐠", "🦥"]

for animal in animals:
    print("Animal:", animal)

print("\n Iterando sobre un string")

name = "Jean"
for character in name:
    print("Letter:", character)

# enumerate() permite iterar sobre un iterable y obtener el índice de cada elemento
print("\n Iterando con index")
animals = ["🐶", "🐈", "🐠", "🦥"]
for index, animal in enumerate(animals):
    print("Index:", index, "Animal:", animal)


# Bucles anidados
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\n Bucles anidados")
for index, row in enumerate(matrix):
    for element in row:
        print("Element:", element)
    print(f"Fin de la fila {index}")


# Break
animals = ["🐶", "🐈", "🐠", "🦥"]
print("\n Bucle for con break")
for index, animal in enumerate(animals):
    print("Animal:", animal)
    if animal == "🐠":
        print("Se encontró el pez en el index", index)
        break
   

# Continue
print("\n Bucle for con continue")
for index, animal in enumerate(animals):
    if animal == "🐠" or animal == "🐶":
        continue
    print("Animal:", animal)

# Comprensión de listas (list comprehension)
animals = ["pez", "perro", "gato", "pájaro"]

capitalized_animals = [animal.upper() for animal in animals]

print("\n Comprensión de listas")
print("Lista original:", animals)
print("Lista capitalizada:", capitalized_animals)

# Comprensión de listas con condicionales
odd_numbers = [number for number in [1, 2, 3, 4, 5, 6, 7, 8, 9] if number % 2 == 0]

print("\n Comprensión de listas con condicionales")
print("Lista de números impares:", odd_numbers)

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")