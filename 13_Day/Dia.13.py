#Ejercicio 1: Filtrar numero negativo y cero
print("Ejercicio 1")
numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
numeros_filtrados = [num for num in numeros if num <= 0]
print(numeros_filtrados)

#Ejercicio 2: Aplanar lista
print("Ejercicio 2")
lista_de_listas = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_filtrada = [item for sublista in lista_de_listas for item in sublista[0]]
print(lista_filtrada)

#Ejercicio 3: Crear lista de tuplas
print("Ejercicio 3")
numeros_potencias = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(0, 11)]
print(numeros_potencias) 

#Ejercicio 4: Aplanar lista
print("Ejercicio 4")
paises = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]
paises_filtrados = [[pais.upper(), pais[:3].upper(), capital.upper()] for [(pais, capital)] in paises]
print(paises_filtrados)

#Ejercicio 5: cambiar de lista a diccionario
print("Ejercicio 5")
paises = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]
lista_diccionarios = [{'pais': item[0][0].upper(), 'ciudad': item[0][1].upper()} for item in paises]
print(lista_diccionarios)

#Ejercicio 6: Cambiar de lista a cadenas cortas
print("Ejercicio 6")
nombres = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
lista_nombres = [item[0][0] + " " + item[0][1] for item in nombres]
print(lista_nombres)

#Ejercicio 7: Resolver pendiente o interseccion
print("Ejercicio 7")
pendiente = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)
interseccion_y = lambda m, x1, y1: y1 - m * x1
x1, y1, x2, y2 = 1, 2, 3, 6
m = pendiente(x1, x2, y1, y2)
print('La pendiente es:', m)
b = interseccion_y(m, x1, y1)
print('La interseccion es:', b)
