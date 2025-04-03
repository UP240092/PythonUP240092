#Nivel 1, Ejercicio 1: Poner dos numeros y sumarlos 
print("Nivel 1, Ejercicio 1")
def adn():
    n1= 5
    n2= 9
    total= n1+n2
    return total
print("El resultado es: ", adn())

#Nivel 1, Ejercicio 2: Calcular el area de un circulo
print("Nivel 1, Ejercicio 2")
import math
def areac():
    radio= 7
    area= math.pi*radio**2
    return area
print("El area del circulo con un radio de 7 es de: ", areac())

#Nivel 1, Ejercicio 3: Comprobar la lista de argumentos
print("Nivel 1, Ejercicio 3")
def addan(*args):
    if all(isinstance(num, (int, float)) for num in args):
        return sum(args) 
    else:
        return "Error: Los argumentos deben ser numeros"
print(addan(1, 2, 3, 4, 5, 6))
print(addan("string", 1, 2, 3))

#Nivel 1, Ejercicio 4: Convertir temperatura de Celsius a Fahrenheit
print("Nivel 1, Ejercicio 4")
def cefa(celcius):
    fahrenheit= (celcius*9/5)+32
    return fahrenheit
print("La temperatura en Fahrenheit es: ", cefa(14))

#Nivel 1, Ejercicio 5: Saber la temporada del mes
print("Nivel 1, Ejercicio 5")
def se(mes):
    if mes in ["Enero", "Febrero", "Marzo"]:
        return "Invierno"
    elif mes in ["Abril", "Mayo", "Junio"]:
        return "Primavera"
    elif mes in ["Julio", "Agosto", "Septiembre"]:
        return "Verano"
    else:
        return "Otoño"
print("La temporada en Octubre es: ", se(mes= "Octubre"))

#Nivel 1, Ejercicio 6: Devolver la pendiente de una ecuacion lineal
print("Nivel 1, Ejercicio 6")
print("x1= 4")
print("x2= 2")
print("y1= 14")
print("y2= 6")
def li(x1, x2, y1, y2):
    n= (y2-y1)/(x2-x1)
    return n
print("La pendiente es: ", li(4, 2, 14, 6))

#Nivel 1, Ejercicio 7: Solucionar una ecuacion cuadratica
print("Nivel 1, Ejercicio 7")
print("a= 4")
print("b= 8")
print("c= 3")
def cua(a, b, c):
    d= b**2-4*a*c
    if d>0:
        x1= (-b+d**0.5)/(2*a)
        x2= (-b-d**0.5)/(2*a)
        return x1, x2
    elif d==0:
        x= -b/(2*a)
        return x
    else:
        return "No hay solucion"
print("La solucion de la ecuacion es: ", "x=", cua(4, 8, 3))

#Nivel 1, Ejercicio 8: Hacer una lista e imprimir todo
print("Nivel 1, Ejercicio 8")
def lista(lista):
    for elemento in lista:
        print(elemento)
comida= ["Ramen", "Pollo", "Dumpling", "Pizza", "Pasta"]
print("La lista es: ")
lista(comida)

#Nivel 1, Ejercicio 9: Hacer una matriz y devolver lo contrario
print("Nivel 1, Ejercicio 9")
per= ["Aaron", "Vanessa", "Janize","Sandra", "Omar", "Brandon"]
def ma(array):
    yarra= []
    for elemento in array:
        yarra.insert(0, elemento)
    return yarra
print("Lista invertida: ", ma(per))

#Nivel 1, Ejercicio 10: Hacer una lista y cambiarla a mayusculas
print("Nivel 1, Ejercicio 10")


#Nivel 1, Ejercicio 11:
print("Nivel 1, Ejercicio 11")

#Nivel 1, Ejercicio 12:
print("Nivel 1, Ejercicio 12")

#Nivel 1, Ejercicio 13:
print("Nivel 1, Ejercicio 13")

#Nivel 1, Ejercicio 14:
print("Nivel 1, Ejercicio 14")

#Nivel 1, Ejercicio 15:
print("Nivel 1, Ejercicio 15")

#Nivel 2, Ejercicio 1:
print("Nivel 2, Ejercicio 1")

#Nivel 2, Ejercicio 2:
print("Nivel 2, Ejercicio 2")

#Nivel 2, Ejercicio 3:
print("Nivel 2, Ejercicio 3")

#Nivel 2, Ejercicio 4:
print("Nivel 2, Ejercicio 4")

#Nivel 3, Ejercicio 1:
print("Nivel 3, Ejercicio 1")

#Nivel 3, Ejercicio 2:
print("Nivel 3, Ejercicio 2")

#Nivel 3, Ejercicio 3:
print("Nivel 3, Ejercicio 3")

#Nivel 3, Ejercicio 4:
print("Nivel 3, Ejercicio 4")

#Nivel 3, Ejercicio 5.1:
print("Nivel 3, Ejercicio 5.1")

#Nivel 3, Ejercicio 5.2:
print("Nivel 3, Ejercicio 5.2")
