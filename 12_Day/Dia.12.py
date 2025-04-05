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
def listOfHexaColors (num):
    hexaColor = []
    for j in range(num):
        randomColor = '#' + ''.join(random.choices('0123456789ABCDEF' , k = 6))
        hexaColor.append(randomColor)
    return hexaColor
print("Números de colores hexadecimales: ")
print(listOfHexaColors(5))

#Nivel 2, Ejercicio 2: Devolver colores en una matriz
print("Nivel 2, Ejercicio 2")
def listOfRgbColors (num):
    rgb = [] 
    for c in range(num):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        rgb.append(('rgb', red, green, blue))
    return rgb
print("Número de colores RGB en una matriz:" , listOfRgbColors(5))

#Nivel 2, Ejercicio 3: Generar numeros de colores
print("Nivel 2, Ejercicio 3")
def generateColors (type, num):
    colors = []
    if type == 'hexa':
        for j in range(num):
            randomColor = '#' + ''.join(random.choices('0123456789ABCDEF', k = 6))
            colors.append(randomColor)
        return colors
    else:
        for j in range(num):
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)
            colors.append(('rgb', red, green, blue))
        return colors
print('Colores hexadecimales:', generateColors('hexa', 3))
print('Colores RGB:', generateColors('rgb', 2))

#Nivel 3, Ejercicio 1: Hacer una lista mesclada
print("Nivel 3, Ejercicio 1")

#Nivel 3, Ejercicio 2: Hacer una matriz de numeros
print("Nivel 3, Ejercicio 2")
