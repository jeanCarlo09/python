###
# 03 - casting de tipos
# Transformar un tipo de un valor a otro
# int(), float(), str(), bool()
###

print("int:")
print(type(int("1")))
print(type(int("-100")))

# print("100" + 1) Error, no hace conversiones automaticas

print("100" + str(2))
print(2 + int("100"))

#print(int("1.14444")) # Error, no se puede convertir un float a int desde un string
print(int(3.1444))
print(int(3.99)) # Pierde precisión


print(bool(3))
print(bool(0))
print(bool(-1))

print(bool(""))
print(bool(" "))
print(bool("False"))

# Python redondea al par más cercano, por lo que 2.5 con round es 2
# y 3.5 es 4