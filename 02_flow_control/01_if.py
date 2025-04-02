###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código dependiendo del cumplimiento de condiciones. Bifurcaciones (variantes).
###

import os # Forma de importar módulos en Python
os.system('clear') # Se utiliza el comando 'clear' para limpiar la consola en sistemas Unix/Linux. En Windows se usa 'cls'.

age = 18

print("Sentencia condicional if")
if age >= 18:
    print("Eres mayor de edad")

print("\n Sentencia condicional if con else")
if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\n Sentencia condicional if con elif")
if age >= 18:
    print("Eres mayor de edad")
elif age >= 13:
    print("Eres un adolescente")
else:
    print("Eres un niño")

print("\n Operadores lógicos. Condiciones multiples")

age = 18
has_license = True

if age >= 18 and has_license:
    print("Puedes conducir")
else:
    print("No puedes conducir")


print("\n Operadores lógicos. Condiciones con or")
if age >= 18 or has_license:
    print("Puedes conducir")
else:
    print("No puedes conducir")


print("\n Operadores lógicos. Condiciones con not")
is_weekend = True
if not is_weekend:
    print("Es un día laboral")
else:
    print("Es fin de semana")

print("\n Operadores lógicos. If anidados... Es una mala práctica")
if age >= 18:
    if has_license:
        print("Puedes conducir")
    else:
        print("Saca la licencia!!!")
else:
    print("No puedes conducir")



# Condicional ternario, forma abreviada de if-else
print("\n Condicional ternario")
age = 18
# [código si cumple la condición] if [condición] else [código si no cumple la condición]
can_drive = "Puedes conducir" if age >= 18 else "No puedes conducir"
print(can_drive)


###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)