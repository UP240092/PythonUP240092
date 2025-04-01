#Ejercicio 1: Crea un diccionario vacio llamado perro
print("Ejercicio 1")
perro= {}
print(len(perro))

#Ejercicio 2: Agregar todas las caracteristicas al diccionario
print("Ejercicio 2")
perro= {
    "Nombre": "Beily",
    "Color": "Cafe",
    "Raza": "Sharpei",
    "Patas": 4,
    "Edad": 4
}
print(perro)

#Ejercicio 3: Crea un diccionario para un estudiante
print("Ejercicio 3")
estudiante= {
    "Nombre": "Ana Sofia",
    "Apellido": "Velasco Lopez",
    "Sexo": "Femenino",
    "Edad": 18,
    "Estado civil": "Soltera",
    "Habilidades": ["Python"],
    "Pais": "Mexico",
    "Ciudad": "Aguascalientes",
    "Direccion": "Camino Real #230-A"
}
print(estudiante)

#Ejercicio 4: Longitud del diccionario del estudiante
print("Ejercicio 4")
print(len(estudiante))

#Ejercicio 5: Valor de habilidades y que tipo de datos son
print("Ejercicio 5")
ha= estudiante["Habilidades"]
print(ha)
print(type(ha))

#Ejercicio 6: Modificar las habilidades
print("Ejercicio 6")
estudiante["Habilidades"].append("CSS")
estudiante["Habilidades"].append("Java")
print(estudiante)

#Ejercicio 7: Claves del diciionario
print("Ejercicio 7")
claves= estudiante.keys()
print("Claves: ", claves)

#Ejercicio 8: Obtener los valores del diccionario
print("Ejercicio 8")
valores= estudiante.values()
print("Valores: ", valores)

#Ejercicio 9: Cambiar el diciionario a tupla
print("Ejercicio 9")
tupla= estudiante.items()
print("Tupla: ", tupla)

#Ejercicio 10: Eliminar una de los elementos del diccionario
print("Ejercicio 10")
estudiante.popitem()
print(estudiante)

#Ejercicio 11: Eliminar una de los diciionarios
print("Ejercicio 11")
del perro
print("Se ha eliminado el diccionario")