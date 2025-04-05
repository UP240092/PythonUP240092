import random
import string

#Nivel 1, Ejercicio 1: Generar un id random
print("Nivel 1, Ejercicio 1")
def rid():
    per= string.ascii_letters+string.digits
    id= "".join((random.choice(per))for j in range(4))
    return id
print("Usuario: ", rid())

#Nivel 1, Ejercicio 2: Modificar el usuario
print("Nivel 1, Ejercicio 2")
def uib():
    pers= string.ascii_letters+string.digits
    num= int(input("Ingrese el numero de caracteres que quiere que tenga el usuario: "))
    id= int(input("Ingrese el numero de IDs que quiera: "))
    def gru():
        return "".join((random.choice(pers))for p in range(num))
    print("Su usuario es: ")
    for i in range(id):
        print(gru())
uib()

#Nivel 1, Ejercicio 3: Genera colores random
print("Nivel 1, Ejercicio 3")
def cg():
    morado= random.randint(0,255)
    negro= random.randint(0,255)
    rojo= random.randint(0,255)
    return (morado, negro, rojo)
print("Colores RGB: ", cg())

#Nivel 2, Ejercicio 1: Colores a matrices
print("Nivel 2, Ejercicio 1")

#Nivel 2, Ejercicio 2: Devolver colores en una matriz
print("Nivel 2, Ejercicio 2")

#Nivel 2, Ejercicio 3: Generar numeros de colores
print("Nivel 2, Ejercicio 3")

#Nivel 3, Ejercicio 1: Hacer una lista mesclada
print("Nivel 3, Ejercicio 1")

#Nivel 3, Ejercicio 2: Hacer una matriz de numeros
print("Nivel 3, Ejercicio 2")
