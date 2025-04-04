###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para realizar tareas específicas.
###

import os # Forma de importar módulos en Python
os.system('clear') # Se utiliza el comando 'clear' para limpiar la consola en sistemas Unix/Linux. En Windows se usa 'cls'.


print("\n Funciones")

""" Definición de una función

def nombre_funcion(parametro1, parametro2, ...):
    # docstring
    # Cuerpo de la función
    return valor_de_retorno # Opcional

"""

# Definición de una función
def greet():
    print("Hola!")

greet() # Llamada/invocar a la función


def greet_to(name: str):
    print(f"Hola {name}!")

greet_to("Jean") # Llamada/invocar a la función
greet_to("Juan") # Llamada/invocar a la función

# Parametro: lo que acepta la función
# Argumento: lo que se le pasa a la función
def add(a: int, b:int):
    return a + b

print("Suma:", add(2, 3)) # Llamada/invocar a la función
print("Suma:", add(5, 10)) # Llamada/invocar a la función

# Documentación de funciones con docstring

def multiply(a: int, b: int) -> int:
    """
    Multiplica dos números enteros y devuelve el resultado.
    
    :param a: Primer número entero.
    :param b: Segundo número entero.
    :return: El resultado de la multiplicación.
    """
    return a * b


print(multiply(2, 3)) # Llamada/invocar a la función


print(multiply.__doc__) # Imprime la documentación de la función
print(multiply.__annotations__) # Imprime la documentación de la función

help(multiply)