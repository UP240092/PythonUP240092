from functools import reduce

#Nivel 1, Ejercicio 1:Diferencia entre asignar, filtraar y reducir
print("Nivel 1, Ejercicio 1")
mapFunction = "Toma una función y un iterable como parámetros. Devuelve un iterable con los elementos transformados."
filterFunction = "Filtra los elementos de un iterable según una condición (devuelve True o False). Devuelve un iterable con los elementos que cumplen la condición"
reduceFunction = "Acumula o reduce los elementos de un iterable a un solo valor mediante una función. No devuelve otro iterable, sino un único valor"
print("map:" , mapFunction)
print("filter:" , filterFunction)
print("reduce:" , reduceFunction)

#Nivel 1, Ejercicio 2: Diferencia entre función de orden superior, cierre y decorador
print("Nivel 1, Ejercicio 2")
higherOrderFunction = "Puede tomar una o más funciones como parámetros, puede ser devuelta como resultado de otra función, se puede modificar, se puede asignar una función a una variable"
closureFunction = "Es una función que 'recuerda' las variables de su entorno externo incluso después de que la función externa termine su ejecución."
decoratorFunction = "Patrón de diseño que permite añadir nuevas funciones a un objeto existente sin modificar su estructura. Toma una función como argumento, le agrega funcionalidad y devuelve una nueva función."
print("higher order function:" , higherOrderFunction)
print("closure:" , closureFunction)
print("decorator:" , decoratorFunction)

#Nivel 1, Ejercicio 3: Definir una función de llamada antes de asignar, filtrar o reducir, consulte ejemplos.
print("Nivel 1, Ejercicio 3")
def double(x):
    return x * 2
numbers = [1, 2, 3, 4, 5]
print("Lista de números:" , numbers)
doubledNumbers = map(double, numbers)
print("Lista del doble de los números:" , list(doubledNumbers))

#Nivel 1, Ejercicio 4: Utilizar bucle para imprimir lista de paises
print("Nivel 1, Ejercicio 4")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print("Países en la lista:")
for country in countries:
    print(country)

#Nivel 1, Ejercicio 5: Imprimir lista de nombres
print("Nivel 1, Ejercicio 5")
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
print("Nombres en la lista:")
for name in names:
    print(name)

#Nivel 1, Ejercicio 6: Imprimir lista de numeros
print("Nivel 1, Ejercicio 6")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Números en la lista:")
for number in numbers:
    print(number)

#Nivel 2, Ejercicio 1: Cambiar a mayusculas en lista de paises
print("Nivel 2, Ejercicio 1")
paises = ['Estonia', 'Finlandia', 'Suecia', 'Dinamarca', 'Noruega', 'Islandia']
paises_mayusculas = list(map(str.upper, paises))
print(paises_mayusculas)

#Nivel 2, Ejercicio 2: Cambiar numeros al cuadrado
print("Nivel 2, Ejercicio 2")
numeros = [1, 2, 3, 4, 5]
numeros_cuadrados = list(map(lambda x: x**2, numeros))
print(numeros_cuadrados)

#Nivel 2, Ejercicio 3: Cambiar a mayusculas los nombres
print("Nivel 2, Ejercicio 3")
nombres = ['Asabeneh', 'David', 'Donald', 'Bill']
nombres_mayusculas = list(map(str.upper, nombres))
print(nombres_mayusculas)

#Nivel 2, Ejercicio 4: Filtrar paises con 'land'
print("Nivel 2, Ejercicio 4")
paises_con_land = list(filter(lambda pais: 'land' in pais.lower(), paises))
print(paises_con_land)

#Nivel 2, Ejercicio 5: Filtrar paises con 6 caracteres
print("Nivel 2, Ejercicio 5")
paises_seis_caracteres = list(filter(lambda pais: len(pais) == 6, paises))
print(paises_seis_caracteres)

#Nivel 2, Ejercicio 6: Filtrar paises con seis o mas letras
print("Nivel 2, Ejercicio 6")
paises_mas_seis_caracteres = list(filter(lambda pais: len(pais) >= 6, paises))
print(paises_mas_seis_caracteres)

#Nivel 2, Ejercicio 7: Filtrar paises con la letra 'E'
print("Nivel 2, Ejercicio 7")
paises_comienzan_e = list(filter(lambda pais: pais.startswith('E'), paises))
print(paises_comienzan_e)

#Nivel 2, Ejercicio 8: Encadenar dos iteradores
print("Nivel 2, Ejercicio 8")
resultado_encadenado = list(map(str.upper, filter(lambda pais: 'land' in pais.lower(), paises)))
print(resultado_encadenado)

#Nivel 2, Ejercicio 9: Hacer una lista y hacerla de cadena
print("Nivel 2, Ejercicio 9")
def obtener_lista_strings(lista):
    return list(filter(lambda x: isinstance(x, str), lista))
ejemplo_lista = [1, 'hola', 3.5, 'mundo', True]
print(obtener_lista_strings(ejemplo_lista))

#Nivel 2, Ejercicio 10: Sumar todos los numeros de la lista
print("Nivel 2, Ejercicio 10")
suma_numeros = reduce(lambda x, y: x + y, numeros)
print(suma_numeros)

#Nivel 2, Ejercicio 11: Hacer una oracion con los paises
print("Nivel 2, Ejercicio 11")
oracion_paises = reduce(lambda x, y: x + ', ' + y, paises[:-1]) + ' y ' + paises[-1] + ' son países del norte de Europa.'
print(oracion_paises)

#Nivel 2, Ejercicio 12: Hacer lista de paises ordenanda
print("Nivel 2, Ejercicio 12")
def categorizar_paises(paises, patron):
    return list(filter(lambda pais: patron in pais.lower(), paises))
print(categorizar_paises(paises, 'land'))

#Nivel 2, Ejercicio 13: Hacer un diccionario
print("Nivel 2, Ejercicio 13")
def contar_paises_por_letra(paises):
    diccionario = {}
    for pais in paises:
        inicial = pais[0]
        diccionario[inicial] = diccionario.get(inicial, 0) + 1
    return diccionario
print(contar_paises_por_letra(paises))

#Nivel 2, Ejercicio 14: Primeros diez paises de la lista
print("Nivel 2, Ejercicio 14")
def obtener_primeros_diez(paises):
    return paises[:10]
print(obtener_primeros_diez(paises))

#Nivel 2, Ejercicio 15: Ultimos diez paises de la lista
print("Nivel 2, Ejercicio 15")
def obtener_ultimos_diez(paises):
    return paises[-10:]
print(obtener_ultimos_diez(paises))

#Nivel 3, Ejercicio 1.0: Ordenar los paises
print("Nivel 3, Ejercicio 1.0")
import Paises_data as datac
data = datac.countries
print("Por nombre:")
sortedByName = sorted(data, key = lambda x: x["name"])
for country in sortedByName:
    print(country["name"])
print("Por capital:")
sortedByCapital = sorted(data, key = lambda x: x["capital"])
for country in sortedByCapital:
    print(country["capital"])
print("Por población")
sortedByPopulation = sorted(data, key = lambda x: x["population"])
for country in sortedByPopulation:
    print(country['name'] , "Población:" , country['population'])

#Nivel 3, Ejercicio 1.1: Ordenar los idiomas mas hablados
print("Nivel 3, Ejercicio 1.1")
sortedLanguages = sorted(data, key=lambda x: x["population"], reverse = True)
print("Los 10 idiomas más hablados por ubicación:")
top10Spoken = sortedLanguages[:10]
for language in top10Spoken:
    print(language['languages'] , ({language['name']}) , "lo hablan:" ,  language['population'] , "habitantes")

#Nivel 3, Ejercicio 1.2: Ordenar los paises mas poblados
print("Nivel 3, Ejercicio 1.2")
sortedCountries = sorted(data, key=lambda x: x["population"], reverse=True)
top10Populated = sortedCountries[:10]
print("Los 10 países más poblados son:")
for country in top10Populated:
    print(country["name"]) , country["population"]
