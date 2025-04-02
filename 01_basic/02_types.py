###
# 02 - types
# int, float, str, bool, NoneType, list, tuple, dict,
# range, set, ...
###

# Doc string, se utiliza más para documentar, se puede utilizar '''
"""
  Así puedes hacer una cadena de texto multilínea,
  y si no l asignas a nada, se trata como un comentario.
"""

print("int:")
print(type(1))
print(type(-5))
print(type(11203913298030891238901298301890)) # En Python no ocurren los problemas como en JS que se desborda el número

print("float:")
print(type(1.0))
print(type(1e3)) # 1e3 = 1000.0 -> Float
print(1e3) 

print("complex:")
print(type(1 + 2j)) # Complejo
print(type(1j)) # Complejo
print(1 + 2j)

print("str:")
print(type("Hola Mundo"))
print(type('Hola Mundo'))
print(type(""))
print(type("123"))
print(type("""
  Multilinea
"""))
print(type('''
           Multilinea
           '''))

print("bool:")
print(type(True))
print(type(False))
print(type(1 == 1))

print("NoneType:")
print(type(None)) # NoneType
print(None) # False