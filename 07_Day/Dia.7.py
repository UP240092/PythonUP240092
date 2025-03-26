#Nivel 1, Ejercicio 1: Encontrar la longitud de it-companies
print("Nivel 1, Ejercicio 1")
it_companies= {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

#Nivel 1, Ejercicio 2: Agregar twitter en it_companies
print("Nivel 1, Ejercicio 2")
it_companies.add("Twitter")
print(it_companies)

#Nivel 1, Ejercicio 3: Insertar mas empresas en la lista
print("Nivel 1, Ejercicio 3")
it_companies.update(["Accenture", "IBM"])
print(it_companies)

#Nivel 1, Ejercicio 4: Eliminar una empresa de la lista
print("Nivel 1, Ejercicio 4")
it_companies.remove("Apple")
print(it_companies)

#Nivel 1, Ejercicio 5: Buscar la diferencia entre quitar y desechar
print("Nivel 1, Ejercicio 5")
print("Cual es la diferencia entre eliminar y descartar?")
print("Eliminar sirve para Se utiliza para eliminar una variable,")
print("un elemento de una lista, una clave de un diccionario, etc.")
print("Descartar sirve para Es un método específico de los conjuntos")
print("en Python. Se utiliza para eliminar un elemento de un conjunto")
print("si está presente. Si el elemento no está en el conjunto, no")
print("hace nada (no lanza una excepción).")

#Nivel 2, Ejercicio 1: Unir A y B
print("Nivel 2, Ejercicio 1")
A= {19, 22, 24, 20, 25, 26}
B= {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))

#Nivel 2, Ejercicio 2: Buscar una interseccion en B
print("Nivel 2, Ejercicio 2")
print(A.intersection(B))

#Nivel 2, Ejercicio 3: Subconjunto de B
print("Nivel 2, Ejercicio 3")
print(A.issubset(B))

#Nivel 2, Ejercicio 4: Son conjuntos disjuntos A y B?
print("Nivel 2, Ejercicio 4")
print(A.isdisjoint(B))

#Nivel 2, Ejercicio 5: Unir A con B y B con A
print("Nivel 2, Ejercicio 5")
print(A.union(B))
print(B.union(A))

#Nivel 2, Ejercicio 6: Diferencia simetrica entre A y B
print("Nivel 2, Ejercicio 6")
print(A.symmetric_difference(B))

#Nivel 2, Ejercicio 7: Eliminar los conjuntos por completo
print("Nivel 2, Ejercicio 7")
del A
del B

#Nivel 3, Ejercicio 1: Edades en un conjunto comparar longitud
print("Nivel 3, Ejercicio 1")
edades= [22, 19, 24, 25, 26, 24, 25, 24]
edadesco= set(edades)
print(edades)
print(len(edades))
print(len(edadesco))
ed= len(edades) == len(edadesco)
print("Las longitudes son iguales?: ", ed)

#Nivel 3, Ejercicio 2: Explicar la diferencia de los diferentes tipos de codigo
print("Nivel 3, Ejercicio 2")
print("Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto")
print("Las cadenas (str) son secuencias inmutables de caracteres usadas para texto; las listas (list)")
print("son colecciones ordenadas y mutables que permiten duplicados y cambios en sus elementos; las")
print("tuplas (tuple) son similares a las listas pero inmutables, también pueden tener duplicados; y")
print("los conjuntos (set) son colecciones desordenadas y mutables, pero no permiten elementos duplicados,")
print("siendo útiles para operaciones como la unión e intersección. Cada uno tiene su función dependiendo")
print("de la necesidad de mutabilidad, orden o exclusividad de elementos.")

#Nivel 3, Ejercicio 3: Cuantas palabras unicas se han utilizado en la oracion?
print("Nivel 3, Ejercicio 3")
fr= "Soy profesora y me encanta inspirar y enseñar a la gente"
pa= fr.split()
un= set(pa)
print(fr)
print("Las palabras unicas son: ", len(un), un)