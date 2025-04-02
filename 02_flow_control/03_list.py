###
# 03 - Listas
# Secuencia mutable de elementos
# Pueden contener elementos de diferentes tipos
###
import os # Forma de importar módulos en Python
os.system('clear') # Se utiliza el comando 'clear' para limpiar la consola en sistemas Unix/Linux. En Windows se usa 'cls'.


print("Crear listas en Python")
list1 = [1, 2, 3, 4, 5]
list2 = ["uno", "dos", "tres"]
list3: list[int | str | float | bool] = [1, "uno", 2.5, True]

empty_list = []  # Lista vacía
maxtrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz de 3x3

print("list1:", list1)
print("list2:", list2)
print("list3:", list3)
print("empty_list:", empty_list)
print("maxtrix:", maxtrix)

print("\nAcceder a los elementos de una lista por índice")
print("Primer elemento de list1:", list1[0])
print("Último elemento de list1:", list1[-1])
print("Último elemento de list1:", list1[-2])
# print("Último elemento de list1:", list1[-5]) # No se puede acceder a un índice negativo mayor que la longitud de la lista

print("Matrix", maxtrix[1][1])

# Slicing (rebanado) de listas
list1 = [1, 2, 3, 4, 5]
print(list1[1:4])  # [2, 3, 4]
print(list1[:3])   # [1, 2, 3]
print(list1[3:])   # [4, 5]
print(list1[:])    # [1, 2, 3, 4, 5] -> Copia de la lista

# print(list1[desde:hasta:paso]) -> desde: índice inicial, hasta: índice final (sin incluirlo), paso: número de elementos a saltar
print(list1[::2])  # [1, 3, 5] -> Salto de 2, para devolver índexes pares
print(list1[::-1])  # [5, 4, 3, 2, 1] -> Reversa


# Modificar listas
list1 = [1, 2, 3, 4, 5]
list1[0] = 10
print("list1:", list1)  # [10, 2, 3, 4, 5]

# Añadir elementos a una lista
list1 = [1, 2, 3]

# Forma larga y menos eficiente
list1 = list1 + [4, 5]  # Concatenación de listas
print("list1:", list1)  # [1, 2, 3, 4, 5]

# Forma corta y más eficiente
list1 += [6, 7]  # Concatenación de listas
print("list1:", list1)  # [1, 2, 3, 4, 5, 6, 7]


# Recuperar la longitud de una lista
print(len(list1))

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]