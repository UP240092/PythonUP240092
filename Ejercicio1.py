#Ejercicio 1: Edad
edad= 18
print(type(edad))

#Ejercicio 2: Altura
altura= 1.73
print(type(altura))

#Ejercicio 3: Número complejo
nc= 4+10j
print(type(nc))

#Ejercicio 4: Area de un triangulo
altura= float(input("Coloca la altura del triangulo: "))
base= float(input("Coloca la base del triangulo: "))
area= base*altura/2
print("El area de tu triangulo es: ", area)

#Ejercicio 5: Perimetro de un triangulo
ladoa= float(input("Inserta lado A: "))
ladob= float(input("Inserta lado B: "))
ladoc= float(input("Inserta lado C: "))
perimetro= ladoa+ladob+ladoc
print("El perimetro de tu triangulo es: ", perimetro)

#Ejercicio 6: Area y perimetro de un rectangulo
alturar= float(input("Coloca la altura del rectangulo: "))
baser= float(input("Coloca la base del rectangulo: "))
arear= baser*alturar
perimetror= 2*(baser+alturar)
print("El area de tu rectangulo es: ", arear)
print("El perimetro de tu rectangulo es: ", perimetror)

#Ejercicio 7: Area y Circunferencia de un circulo
radio= float(input("Coloca el radio del circulo: "))
pi= 3.14
areac= pi*radio*radio
circunferencia= 2*pi*radio
print("El area de tu circulo es: ", areac)
print("La circunferencia de tu circulo es: ", circunferencia)

#Ejercicio 8: Pendiente 1
x= 0
y= 0
interx= (y+2)/2
intery= 2*x-2
m= intery/-interx
print("La pendiente de la recta es: ", m)
print("La intersección en el eje x es: ", interx)
print("La intersección en el eje y es: ", intery)

#Ejercicio 9: Pendiente 2
import math 
x1= 2
y1= 2
x2= 6
y2= 10
pendiente= (y2-y1)/(x2-x1)
diseu= math.sqrt((x2-x1)**2+(y2-y1)**2)
print("La pendiente de la recta es: ", pendiente)
print("La distancia euclidiana es: ", diseu)

#Ejercicio 10: Comparación de pendientes
m1= m
m2= pendiente
print("La pendiente de la recta y= 2x-2 es: ", m1)
print("La pendiente entre los puntos (2,2) y (6,10) es: ", m2)
if m1==m2:
    resultado= "Las pendientes son iguales"
else: 
    resultado= "Las pendientes son diferentes"
print(resultado)

#Ejercicio 11: Calcular x
xc= float(input("Coloca un valor de x: "))
yc= xc**2 +6*xc + 9
print("El valor de y es: ", yc)
if yc== 0:
    print("y equivale a 0 cuando x es: ", xc)
else:
    print("y no equivale a 0 cuando x es: ", xc)

#Ejercicio 12: Medir python y jerga
pylen= len("Python")
dralen= len("Dragon")
falsacom= pylen < dralen
print("La longitud de 'Python' es: ", pylen)
print("La longitud de 'Dragon' es: ", dralen)
print("La longitud de 'Dragon' es mayor a la de 'Python'?", falsacom)

#Ejercicio 13: 'on' en python y dragon
python= 'on' in 'python'
dragon= 'on' in 'dragon'
if python and dragon:
    resultado= "La silaba 'on' se encuentra en ambas palabras"
else:
    resultado= "La silaba 'on' no se encuentra en ambas palabras"
print(resultado)

#Ejercicio 14: Jargon en la frase
frase= "I hope this course is not full of jargon"
if "jargon" in frase:
    resultado= "La palabara 'jargon' esta en la frase"
else:
    resultado: "La palabra 'jargon' no esta en la frase"
print(resultado)

#Ejercicio 15: No 'on' en python y dragon
pythonno= 'on' not in 'python'
dragonno= 'on' not in 'dragon'
if pythonno and dragonno:
    resultado= ("La silaba 'on' no se encuentra en ninguna palabra")
else:
    resultado= ("La silaba 'on' se encuentra en alguna palabra")
    print(resultado)

#Ejercicio 16: Longitud de python
pylon= len("python")
pylonflo= float(pylon)
pylonst= str(pylonflo)
print("La longitud de la palabra 'Python' es: ", pylon)
print("La longitud como flotante es: ", pylonflo)
print("La longitud como strigt es: ", pylonst)

#Ejercicio 17: Numeros divisibles entre dos
def esPar(numero):
    if numero%2 == 0:
        return True
    else:
        return False
numero= float(input("Ingresa un numero: "))
if esPar(numero):
    print("El numero", numero, "es par")
else:
    print("El numero", numero, "es impar")

#Ejercicio 18:

#Ejercicio 19:

#Ejercicio 20:

#Ejercicio 21:

#Ejercicio 22:

#Ejercicio 23: