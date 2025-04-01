#Nivel 1, Ejercicio 1: Crear una tupla vacia
print("Nivel 1, Ejercicio 1")
tupla= tuple()
print(tupla)

#Nivel 1, Ejercicio 2: Tupla con los nombres de mis hermanos
print("Nivel 1, Ejercicio 2")
sis= ("Karina", "Julieta")
bro= ("Andres", "Luisda")
print(sis, bro)

#Nivel 1, Ejercicio 3: Juntar las dos tuplas
print("Nivel 1, Ejercicio 3")
seb= sis+bro
print(seb)

#Nivel 1, Ejercicio 4: Sacar la longitud de la tupla
print("Nivel 1, Ejercicio 4")
print(len(seb))

#Nivel 1, Ejercicio 5: Agrgar los nombres de mis papás
print("Nivel 1, Ejercicio 5")
par= ("Ana", "Julio")
fam= seb+par
print(fam)

#Nivel 2, Ejercicio 1: Desempacar todos los de la tupla
print("Nivel 2, Ejercicio 1")
family=list(fam)
sib= family[:4]
pare= family[4:]
print(sib)
print(pare)

#Nivel 2, Ejercicio 2: Crear una tupla con frutas, verduras y productos de origen animal
print("Nivel 2, Ejercicio 2")
frutas= ("Durazno", "Manzana", "Platano", "Guayaba")
verduras= ("Coliflor", "Brocoli", "Zanahoria", "Calabaza")
animal= ("Queso", "Leche", "Carne", "Huevos")
foodstuff= frutas+verduras+animal
print(foodstuff)

#Nivel 2, Ejercicio 3: Hacer la tupla una lista
print("Nivel 2, Ejercicio 3")
foodstuff1= list(foodstuff)
print(foodstuff1)

#Nivel 2, Ejercicio 4: Cortar los elementos de en medio de la lista
print("Nivel 2, Ejercicio 4")
print(foodstuff1[5:7])

#Nivel 2, Ejercicio 5: Cortar los primeros 3 elementos y los ultimos 3
print("Nivel 2, Ejercicio 5")
print(foodstuff1[3:9])

#Nivel 2, Ejercicio 6: Eliminar la tupla
print("Nivel 2, Ejercicio 6")
del foodstuff1

#Nivel 2, Ejercicio 7.0: Comprobar si existe algun elemento de tupla
print("Nivel 2, Ejercicio 7.0")
paisesnor= ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(paisesnor)

#Nivel 2, Ejercicio 7.1: Comprobar si existe 'Estonia'
print("Nivel 2, Ejercicio 7.1")
print("Estonia" in paisesnor)

#Nivel 2, Ejercicio 7.2: Comprobar si existe 'Iceland'
print("Nivel 2, Ejercicio 7.2")
print("Iceland" in paisesnor)

print("Revisado")