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
paises=["Corea", "Japon", "Italia", "Venecia"]
print("Lista: ", paises)
def capli(lista):
    return [cosa.upper() for cosa in lista]
print("Lista en mayusculas: ", capli(paises))

#Nivel 1, Ejercicio 11: Agregarle elementos a una lista
print("Nivel 1, Ejercicio 11")
def agr(lista, cosa):
    lista.append(cosa)
    return lista
print("Lista nueva: ", agr(per, "Isai"))

#Nivel 1, Ejercicio 12: Eliminar un elemento de una lista
print("Nivel 1, Ejercicio 12")
def qui(lista, cosa):
    lista.remove(cosa)
    return lista
print("Lista nueva: ", qui(comida, "Pizza"))

#Nivel 1, Ejercicio 13: Sumar todos los numeros 
print("Nivel 1, Ejercicio 13")
def suma(numero):
    s= 0
    for i in range(1, numero+1):
        s=s+i
    return s
print("La suma es de: ", suma(14))

#Nivel 1, Ejercicio 14: Sumar todos los numeros impares
print("Nivel 1, Ejercicio 14")
def im(numero):
    n= 0
    for i in range(numero+1):
        if i%2==1:
            n+=i
    return n
print("La suma de los impares es: ", im(10))

#Nivel 1, Ejercicio 15: Sumar los numeros pares 
print("Nivel 1, Ejercicio 15")
def pa(numero):
    n2= 0
    for i in range(numero+1):
        if i%2==0:
            n2+=i
    return n2
print("La suma de los pares es: ", pa(6))

#Nivel 2, Ejercicio 1: Contar cuantos pares e impares hay en un numero
print("Nivel 2, Ejercicio 1")
def impa(numero):
    n3= 0
    n4= 0
    for i in range(numero+1):
        if i%2==1:
            n3=n3+1
        else:
            n4= n4+1
    return n3, n4
print("La cantidad de numeros pares e impares es de: ", impa(1313))

#Nivel 2, Ejercicio 2: Devolver el factorial de un numero entero
print("Nivel 2, Ejercicio 2")
def fac(numero):
    f= 1
    if (numero<0):
        return "El factorial no es posible con numeros negativos"
    else:
        for i in range(1, numero+1):
            f= f*i
            return f
print("El factorial del numero es: ", fac(9))        

#Nivel 2, Ejercicio 3: Comprobar si el parametro esta vacio o no
print("Nivel 2, Ejercicio 3")
lista= ["JK", "Jin"]
def va(parametro):
    if len(parametro)==0:
        return "Esta vacio"
    else:
        return "No esta vacio"
print("El parametro ", va(lista))

#Nivel 2, Ejercicio 4: Escribir diferentes funciones 
print("Nivel 2, Ejercicio 4")
nota= [6, 8, 9, 7, 9, 8, 10, 8]
print("Calificaciones:" , nota)
from collections import Counter

def cm(lista):
    su= 0
    for i in lista:
        su= su+i
    mean= su/len(lista)
    return mean
print("Media: ", round(cm(nota), 2))

def cme(lista):
    lista.sort()
    mediana= lista[int(len(lista)/2+1)]
    return mediana
print("Mediana: ", cme(nota))

def cmo(lista):
    co= Counter(lista)
    mode= co.most_common(1)
    mode= mode[0]
    mode= mode[0]
    return mode
print("Moda:", cmo(nota))

def cr(lista):
    lista.sort()
    range = lista[-1]-lista[0]
    return range
print("Rango: ", cr(nota))

def cv(lista):
    sum= 0
    for i in lista:
        sum= sum+i
    mean= sum/len(lista)
    n= []
    for i in lista:
        n.append((i-mean)**2)
    sumN= 0
    for i in n:
        sumN= sumN+i
    return sumN/len(lista)
print("Varianza: ", round(cv(nota), 2))

def cs(lista):
    sum= 0
    for i in lista:
        sum= sum+i
    mean= sum/len(lista)
    n= []
    for i in lista:
        n.append((i-mean)**2)
    sumN= 0
    for i in n:
        sumN= sumN+i
    variance= round(sumN/len(lista), 2)
    return variance*0.5
print("Desviación estándar: ", cs(nota))

#Nivel 3, Ejercicio 1: Comprobar si un numero es primo
print("Nivel 3, Ejercicio 1")
def pri(num):
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True
print("El numero 53 es primo?", pri(53))

#Nivel 3, Ejercicio 2: Comprobar si todos los elementos son unicos
print("Nivel 3, Ejercicio 2")
bts= ["RM", "Jin", "Suga", "Hobi", "Jimin", "V", "JK"]
print("Lista: ", bts)
def iu(bts):
    for i in bts:
        if bts.count(i)>1:
            return False
    return True
print("Todos los elementos de la lista son unicos?", iu(bts))

#Nivel 3, Ejercicio 3: Comprobar si una lista son los mismos datos
print("Nivel 3, Ejercicio 3")
n= [1, 2, 3, 4, 5]
print("Lista: ", n)
def sdt(n):
    types = []
    for i in n:
        types.append(type(i))
    if len(set(types)) == 1:
        return True
    return False
print("¿Todos los elementos de la lista son del mismo tipo?", sdt(n))

#Nivel 3, Ejercicio 4: Ver si es una variable de python
print("Nivel 3, Ejercicio 4")
def ipv(variable):
    t= type(variable)
    ti= [str, complex, int, float, bool, list, tuple, set, dict]
    if t in ti:
        return True
    return False
print("La variable es una variable de Python?", ipv(4))

#Nivel 3, Ejercicio 5.1: Los idiomas mas hablados del mundo
print("Nivel 3, Ejercicio 5.1")
import Paises_data as paises
data= paises.countries
from collections import Counter
def msl(lista):
    todos= [idioma for pais in lista for idioma in pais["languages"]]
    c= Counter(todos)
    top= c.most_common(10)
    return top
print("Los 10 idiomas mas hablados son: ", msl(data))

#Nivel 3, Ejercicio 5.2: Los paises mas poblados
print("Nivel 3, Ejercicio 5.2")
def mpc(lista):
    mas= []
    top= sorted(lista, key=lambda x: x["population"], reverse=True)[:10]
    print("Los 10 paises mas poblados son: ")
    for pais in top:
        mas.append(f"{pais["name"]}-{pais["population"]}")
    return mas
print(mpc(data))
