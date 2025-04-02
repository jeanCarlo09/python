###
# 04 - Entrada de usuario `input()` - Versión simplificada
# Permite obtener datos del usuario a través de la consola.
# El valor devuelto es siempre un string.
###

# print("Hola, cómo te llamas?")
# nombre = input()

# print(f"Hola {nombre}, bienvenido a Python")

nombre = input("Hola, cómo te llamas?\n")
print(f"Hola {nombre}, bienvenido a Python")


age = input("Cuántos años tienes?\n")
print(f"Dentro de 20 años tendras {int(age) + 20} años")

print("Obtener múltiples valores de entrada a la vez")
country, city = input("En qué país y ciudad vives?\n").split()
print(f"Vives en {country}, {city}")