###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición.
###

import os # Forma de importar módulos en Python
os.system('clear') # Se utiliza el comando 'clear' para limpiar la consola en sistemas Unix/Linux. En Windows se usa 'cls'.


print("\n Bucles (while)")

counter = 0

while counter <= 5:
    print("Counter:", counter)
    counter += 1

    
print("Fin del bucle while")


print("\nBucle while con break")
counter = 0

while True:
    print("Counter:", counter)
    counter += 1
    if counter > 5:
        break


print("\nBucle while con continue")
counter = 0
while counter < 10:
    counter += 1
    
    if not counter % 2 == 0: # Si el número no es par
        continue

    print("Counter:", counter)

print("\nBucle while con else")
counter = 0

while counter < 5:
    print("Counter:", counter)
    counter += 1
else:
    print("Fin del bucle while")
    print("Counter:", counter)

print("\nBucle while con else y break")
counter = 0
while counter < 5:
    print("Counter:", counter)
    counter += 1
    break
else: # Se ejecuta solamente hasta que la condición del while no se cumple, si se rompe el bucle no se ejecuta
    print("Fin del bucle while")
    print("Counter:", counter)


# Ejemplo: Pedir al usuario que tiene que ser positivo, caso contrario solicitar otro

# number = -1

# while number <= 0:
#     number = int(input("Introduce un número positivo: "))

# print(f"\nEl número introducido:{number}")

number = -1

while number <= 0:
    try:
        number = int(input("Introduce un número positivo: "))
    except:
        print("Por favor, introduce un número válido.")
        continue

print(f"\nEl número introducido:{number}")



###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")