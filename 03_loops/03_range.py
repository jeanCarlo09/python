###
# 03 - Range
# Permite crear una secuencia o rango de números de números. Puede ser útil para for, pero no solo para ese caso
###

import os # Forma de importar módulos en Python
os.system('clear') # Se utiliza el comando 'clear' para limpiar la consola en sistemas Unix/Linux. En Windows se usa 'cls'.


print("\n Range")
#numbers = range(0, 10) # Crea un rango de números del 0 al 9. No crea listas
numbers = range(10) # Crea un rango de números del 0 al 9. No crea listas
print("numbers:", numbers)
print(type(numbers)) # <class 'range'>

numbers = range(0, 10, 2)
print("numbers:", numbers)

# No crea una lista, crea un rango que se va generando a medida que se itera, bajo demanda

for number in numbers:
    print("Number:", number) # Hasta que no se itere no se genera el número

for number in range (-5, 0):
    print("Number:", number) # Hasta que no se itere no se genera el número

for number in range(10, 0, -1):
    print("Number:", number) # Hasta que no se itere no se genera el número

print("\n Crear una lista a partir de un rango") # No es recomendable, evitar de usar si es posible
numbers = list(range(10))
print("numbers:", numbers) # Crea una lista a partir de un rango
print(type(numbers)) # <class 'list'>

# Para ejecutar un bucle N cantidad de veces, dónde N es un número entero y conocido

counter = 0
while counter < 5:
    print("Iteración")
    counter += 1

# O usando un bucle for con range, más limpio y legible
print("\n Bucle for con range")
for _ in range(5):
    print("Iteración")

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")