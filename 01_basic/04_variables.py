###
# 04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte
###


age = 32
print(age)

age = 39
print(age)

# Tipado dinámico: el tipo de dato se determina en tiempo de ejecución, y
# no es necesario declararlo explícitamente, tipo Java o TS (tipado estático).

name = "Jean"
print(type(name))

name = 23
print(type(name))


# Tipado fuerte: no se permite la conversión automática entre tipos de datos.
# JS es de tipado débil, y permite hacer conversiones automáticas entre tipos de datos.

#print(10 + "2") # Error, no se puede sumar un número a un string

# f-string (literal de cadena de formato)
name = "Jean"
age = 32
print(f"Hola soy {name} y tengo {age} años")

# No recomendada forma de asignar variables
name, age, city = "Jean", 32, "Madrid"

# Convenciones de nombres de variables
# - snake_case: nombre_de_variable

first_name = "Jean"
last_name = "Vargas"

# En Python no existen constantes, valores no reasignables

MY_CONSTANT = 3.14 # Por convención se escriben en mayúsculas las constantes, más que todo para identificar

# nombres no válidos de variables
# - No pueden empezar con un número
# - No pueden contener espacios
# - No pueden contener caracteres especiales (excepto _)
# - No pueden ser palabras reservadas (if, else, for, while, etc.)

# Types anotation -> Son como anotaciones, para dar un tipado al dato
# Pero en tiempo de ejecución no se verifica, solo es para información

is_user_logged_in: bool = True
print(is_user_logged_in)

# Funciona XD, si en las configs del IDE se tiene el `Type checking mode` en off
# Pero se sigue ejecutando, solamente es visual
is_user_logged_in = 42 
print(is_user_logged_in)

# Con el type anotation se puede pasar de tipado denámico a tipado estático