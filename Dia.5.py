#Ejercicio 1: Hacer una lista vacia
print("Ejercicio 1")
lista= ()
print(lista)

#Ejercicio 2:Hacer una lista con mas de 5 elementos
print("Ejercicio 2")
lista2= ("a, b, c, d, e, f, g")
print(lista2)

#Ejercicio 3: Encuentra la longitud de la lista
print("Ejercicio 3")
print(len(lista2))

#Ejercicio 4: Imprimir el primer, el de enmedio y el ultimo termino de la lista
print("Ejercicio 4")
print(lista2[0], lista2[9], lista2[18])

#Ejercicio 5: Hacer una variable con tus datos
print("Ejercicio 5")
mixed_data_types= ["Sofia", 18, 1.73, "Soltera", "Camino Real"]
print("Se hiso una variable con mis datos personales")

#Ejercicio 6: Hacer una variable con lista de compañias
print("Ejercicio 6")
it_companies= ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("Se hiso una variable con una lista de distintas compañias")

#Ejercicio 7: Imprimir la lista anterior
print("Ejercicio 7")
print(it_companies)

#Ejercicio 8: Imprimir cuantas empresas hay en la lista
print("Ejercicio 8")
print(len(it_companies))

#Ejercicio 9: Imprimir la primera, la intermedia y la ultima empresa
print("Ejercicio 9")
print(it_companies[0], it_companies[3], it_companies[6])

#Ejercicio 10: Modificar una empresa e imprimir la nueva lista
print("Ejercicio 10")
print(it_companies)
it_companies[3]= 'Samsung'
print(it_companies)

#Ejercicio 11: Agregar una empresa de TI en la lista
print("Ejercicio 11")
it_companies.append("Dell")
print(it_companies)

#Ejercicio 12: Agregar una empresa de TI en medio de la lista
print("Ejercicio 12")
it_companies.insert(4, "Accenture")
print(it_companies)

#Ejercicio 13: Cambiar el nombre de una empresa a mayusculas
print("Ejercicio 13")
it_companies[3]= it_companies[3].upper()
print(it_companies)

#Ejercicio 14: Hacer una cadena de las empresas
print("Ejercicio 14")
cadena= "#; ".join(it_companies)
print(cadena)

#Ejercicio 15: Revisar si existe una empresa en la lista
print("Ejercicio 15")
exis= "Tesla" in it_companies
print(exis)

#Ejercicio 16: Organisar la lista en orden alfabetico
print("Ejercicio 16")
it_companies.sort()
print(it_companies)

#Ejercicio 17: Organizar la lista de manera alfabetica al reves
print("Ejercicio 17")
it_companies.sort(reverse= True)
print(it_companies)

#Ejercicio 18: Eliminar las 3 primeras empresas de la lista
print("Ejercicio 18")
pri3= it_companies[3:9]
print(pri3)

#Ejercicio 19: Eliminar las 3 ultimas empresas de la lista
print("Ejercicio 19")
ult3= it_companies[3:6]
print(ult3)

#Ejercicio 20: Eliminar la empresa de en medio de la lista
print("Ejercicio 20")
it_companies.remove("Google")
print(it_companies)

#Ejercicio 21: Eliminar la primera empresa de la lista
print("Ejercicio 21")
it_companies.remove("SAMSUNG")
print(it_companies)

#Ejercicio 22: Eliminar las empresas intermedias de la lista
print("Ejercicio 22")
it_companies.remove("Facebook")
print(it_companies)

#Ejercicio 23: Eliminar la ultima empresa de la lista
print("Ejercicio 23")
it_companies.remove("Accenture")
print(it_companies)

#Ejercicio 24: Eliminar todas las empresas de la lista
print("Ejercicio 24")
it_companies.clear()
print(it_companies)

#Ejercicio 25: Eliminar la lista completa
print("Ejercicio 25")
del it_companies

#Ejercicio 26: Unirse a las listas
print("Ejercicio 26")
front_end= ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end= ['Node','Express', 'MongoDB']
listas= front_end+back_end
print(listas)

#Ejercicio 27: Asignar variables en la lista 
print("Ejercicio 27")
fullStack= listas.copy()
fullStack.insert(5, "Python")
fullStack.insert(6, "SQL")
print(fullStack)

#Ejercicio 1.0 nivel 2: Lista de edades
print("Ejercicio 1 nivel 2")
edades= [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(edades)

#Ejercicio 1.1 nivel 2: Ordenar la lista y encontrar el mayor y el menor
print("Ejercicio 1.1 nivel 2")
edades.sort()
print(edades)
menor= edades[0]
print(menor)
mayor= edades[-1]
print(mayor)

#Ejercicio 1.2 nivel 2:
print("Ejercicio 1.2 nivel 2")
edades.append(menor)
edades.append(mayor)
print(edades)

#Ejercicio 1.3 nivel 2: Encontrar la media
print("Ejercicio 1.3 nivel 2")
media= ((edades[5]+edades[6])/2)
print(media)

#Ejercicio 1.4 nivel 2: Sacar el promedio de todas las edades
print("Ejercicio 1.4 nivel 2")
sued= sum(edades)
promedio= sued/len(edades)
print("El promedio es de: ", promedio)

#Ejercicio 1.5 nivel 2:
print("Ejercicio 1.5 nivel 2")

