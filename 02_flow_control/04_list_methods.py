###
# 04 - Métodos de listas
# Los métodos más importantes de listas son:
###

import os # Forma de importar módulos en Python
os.system('clear') # Se utiliza el comando 'clear' para limpiar la consola en sistemas Unix/Linux. En Windows se usa 'cls'.

list1 = [1, 2, 3, 4, 5]

# Añadir o insertar elementos a una lista
list1.append(6)  # Añadir un elemento al final de la lista
print("list1:", list1)  # [1, 2, 3, 4, 5, 6]

list1.insert(2, 20) # Insertar un elemento en una posición/indice específica
print("list1:", list1) 

list1.extend([7, 8, 9]) # Añadir varios elementos al final de la lista
print("list1:", list1)

# Eliminar elementos de una lista
list1.append(1)
list1.remove(1) # Eliminar el primer elemento que coincida con el valor especificado
print("list1:", list1)

list1.pop() # Eliminar el último elemento de la lista (por default su argumento es -1)
print("list1:", list1)

first_item = list1.pop(0) # Eliminar el primer elemento de la lista
print("list1:", list1, "Deleted item:", first_item)

# Eliminar forzosamente un elemento de la lista (pero puede ser útil para eliminar un rango de elementos)
del list1[0] # Eliminar el primer elemento de la lista
print("list1:", list1)

animals = ["🐶", "🐈", "🐠", "🦥"]
del animals[1:3] # Eliminar un rango de elementos de la lista
print("animals:", animals)

# Eliminar todos los elementos de la lista
list1.clear() # Eliminar todos los elementos de la lista
print("list1:", list1) # []

# Ordenar una lista
list1 = [5, 2, 4, 1, 3]
list1.sort() # Ordenar la lista de menor a mayor
print("list1:", list1) # [1, 2, 3, 4, 5]

# Crear copia de la lista ordenada
list1 = [5, 2, 4, 1, 3]
sorted_numbers = sorted(list1)
print(sorted_numbers, list1)

# Ordenar cadenas de texto
list1 = ["perro", "gato", "elefante", "ratón", "Perro", "Elefante"]
animals_sorted = sorted(list1) # Ordena primero por mayúsculas y luego por minúsculas por comparación lexicográfica, las mayúsculas y minusculas tienen peso diferente
print(animals_sorted) # ['Elefante', 'Perro', 'elefante', 'gato', 'perro', 'ratón']
# Para ignorar el case sensitive, se puede usar el argumento key
animals_sorted.sort(key=str.lower) # Ordena la lista ignorando el case sensitive
print(animals_sorted)

# Otros detalles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la lista
print(animals.count('🐶')) # Cuantas veces aparece el elemento
print('🐼' in animals) # Comprueba si hay algún elemento en la lista
print('🐹' not in animals) # Comprueba si no hay ningún elemento en la lista


###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.