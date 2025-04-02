#Nivel 1, Ejercicio 1: Itere del 0 al 10 con diferentes bucles
print("Nivel 1, Ejercicio 1")
cu= 0
while cu<=10:
    print(cu)
    cu= cu+1
n= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    
for nu in n:
    print(nu)

#Nivel 1, Ejercicio 2: Iterar del 10 al 0 con diferentes bucles
print("Nivel 1, Ejercicio 2")
cu2= 10
while cu2>=1:
    print(cu2)
    cu2= cu2-1
n2= [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
for nu2 in n2:
    print(nu2)

#Nivel 1, Ejercicio 3: Hacer un triangulo con #
print("Nivel 1, Ejercicio 3")
for i in range(8):
    print("#"*i)

#Nivel 1, Ejercicio 4: Hacer un cuadro con #
print("Nivel 1, Ejercicio 4")
m= 8
n= 8
for j in range(m):
  for i in range(n):
     print("#", end=" ")
  print()

#Nivel 1, Ejercicio 5: imprimir un patron 
print("Nivel 1, Ejercicio 5")
for i in range(11):
    print(i, "x", i, "=", i*i)

#Nivel 1, Ejercicio 6: Iterar una lista e imprimir los elementos
print("Nivel 1, Ejercicio 6")
le= ['Python', 'Numpy','Pandas','Django', 'Flask']
for lenf in le:
    print(lenf)

#Nivel 1, Ejercicio 7: Iterar del 0 al 100 y solo imprimir numeros pares
print("Nivel 1, Ejercicio 7")
for i in range(0, 101, 2):
    print(i)

#Nivel 1, Ejercicio 8: Iterar del 0 al 100 y solo imprimir numeros impares
print("Nivel 1, Ejercicio 8")
for i in range(1, 100, 2):
 print(i)

#Nivel 2, Ejercicio 1: Usar el bucle for para sumar todos los numeros
print("Nivel 2, Ejercicio 1")
suma= 0
for n in range(101):
   suma=suma+n
print("El total de las suma es de: ", suma)

#Nivel 2, Ejercicio 2: Iterar del 0 al 100 e imprimir la suma de todos los pares y las probabilidades
print("Nivel 2, Ejercicio 2")
supa= 0
suim= 0
for n in range(101):
    if n%2==0:
      supa=supa+n
    else:
      suim= suim+n
print("La suma de todos los pares es de: ", supa)
print("La suma de todos los impares es de: ", suim)

#Nivel 3, Ejercicio 1: Extraer ciertos paises de la lista de paises
print("Nivel 3, Ejercicio 1")
from Paises import paises
print("Paises que contienen la palabra 'Land'")
for pais in paises:
   if "land" in pais:
      print(pais)

#Nivel 3, Ejercicio 2: Invertir el orden de una lista con un bucle
print("Nivel 3, Ejercicio 2")
fru= ['plátano', 'naranja', 'mango', 'limón']
print("La lista invertida de frutas es: ")
for fru in reversed(fru):
   print(fru)

#Nivel 3, Ejercicio 3.1: Cuantos lenguajes hay en la lista de paises
print("Nivel 3, Ejercicio 3.1")
import Paises_data as pada
data= pada.countries
counle= []
for pais in data:
   for language in pais["languages"]:
      counle.append(language)
idiomas = set(counle)
nulen = len(idiomas)
print("Las cantidades de lenguajes en Paises_data es: ", nulen)

#Nivel 3, Ejercicio 3.2: Encontrar los 10 idiomas mas hablados 
print("Nivel 3, Ejercicio 3.2")
paset= set(counle)
id= {}
for language in paset:
   id[language]= 0
for language in id:
   for pais in data:
      if language in pais["languages"]:
         id[language]= pais["population"]+id[language]
svlp= sorted(id.values(), reverse= True)
sklp= sorted(id, key= id.get, reverse= True)
print("Los 10 idiomas mas hablados en el mundo son: ")
for i in range(10):
   print("Idioma: ", sklp[i], "Cantidad de personas hablantes: ", svlp[i])

#Nivel 3, Ejercicio 3.3: Encontrar los 10 paises mas poblados
print("Nivel 3, Ejercicio 3.3")
copu= []
setp= set(copu)
dicp= {}
for pais in data:
   dicp[pais["name"]]= pais["population"]
sorc= sorted(dicp.items(), key= lambda x: x[1], reverse= True)
print("Los 10 paises mas poblados son: ")
for i in range(min(10, len(sorc))):
   country, population= sorc[i]
   print(f"{country}: {population}")
