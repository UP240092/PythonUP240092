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
for len in le:
    print(len)

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
su= 0
n = 0
for n in range(101):
   su= su+n
   n= n+1
   print("La suma de todos los numeros es de ", su)

#Nivel 2, Ejercicio 2:
print("Nivel 2, Ejercicio 2")

#Nivel 3, Ejercicio 1:
print("Nivel 3, Ejercicio 1")

#Nivel 3, Ejercicio 2:
print("Nivel 3, Ejercicio 2")

#Nivel 3, Ejercicio 3.0:
print("Nivel 3, Ejercicio 3.0")

#Nivel 3, Ejercicio 3.1:
print("Nivel 3, Ejercicio 3.1")

#Nivel 3, Ejercicio 3.2:
print("Nivel 3, Ejercicio 3.2")

#Nivel 3, Ejercicio 3.3:
print("Nivel 3, Ejercicio 3.3")
