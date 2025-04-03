###
# 01 - Bucles (for)
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