#Nivel 1, Ejercicio 1: Ingresar la edad y saber si puedes manejar 
print("Nivel 1, Ejercicio 1")
ed1= int(input("Ingresa tu edad: "))
ed2= int(18-ed1)
if ed1>=18:
    print("Tiene la edad suficiente para conducir")
else:
    print("Necesitas esperar {} años para poder manejar".format(ed2))

#Nivel 1, Ejercicio 2: Comparar edades
print("Nivel 1, Ejercicio 2")
mied=int(18)
tued= int(input("Ingresa tu edad: "))
a1= int(tued-18)
a2= int(tued-18)
a3= int(mied-tued)
if mied == tued:
    print("Somos de la misma edad")
elif tued == 19:
    print("Eres mayor que yo por {} años".format(a1))
elif tued > 19:
    print("Eres mayor que yo por {} años".format(a2))
else:
    print("Eres menor que yo por {} años".format(a3))

#Nivel 1, Ejercicio 3: Comparar dos numeros
print("Nivel 1, Ejercicio 3")
n1= float(input("Ingrese un numero: "))
n2= float(input("Ingrese otro numero: "))
if n1>n2:
    print(n1, "es mayor que ", n2)
elif n1<n2:
    print(n1, "es menor que ", n2)
else:
    print(n1, "es igual a ", n2)

#Nivel 2, Ejercicio 1: Codigo que califique 
print("Nivel 2, Ejercicio 1")
cal= float(input("Ingresa tu calificacion: "))
if cal>=80:
    print("Tienes una A")
elif cal>=70 and cal<=79:
    print("Tienes una B")
elif cal>=60 and cal<=69:
    print("Tienes una C")
elif cal>=50 and cal<=59:
    print("Tienes una D")
else:
    print("Tienes una F") 

#Nivel 2, Ejercicio 2: Comprobar la temporada del año depende el mes
print("Nivel 2, Ejercicio 2")
mes=(input("Ingresa un mes: "))
if mes in ["septiembre", "octubre", "noviembre"]:
    print("Otoño")
elif mes in ["diciembre", "enero", "febrero"]:
    print("Invierno")
elif mes in ["marzo", "abril", "mayo"]:
    print("Primavera")
else:
    print("Verano")

#Nivel 2, Ejercicio 3: Modificar la lista para que agregue frutas
print("Nivel 2, Ejercicio 3")
frs= ["platano", "naranja", "mango", "limon"]
fr= str(input("Ingresa una fruta: "))
if fr in frs:
    print("Esa fruta ya esta en la lista")
else:
    frs.append(fr)
    print(frs)

#Nivel 3, Ejercicio 1.1: Checar si el diccionario tiene habilidades e imprimir las de enmedio
print("Nivel 3, Ejercicio 1.1")
person={
    'Primer_nombre': 'Asabeneh',
    'Ultimo_nombre': 'Yetayeh',
    'Edad': 250,
    'Pais': 'Finlandia',
    'Esta_Comprometido': True,
    'Habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'Direccion': {
        'Calle': 'Space street',
        'Codigo_postal': '02210'
    }
    }
if "Habilidades" in person:
    print(person["Habilidades"] [len(person["Habilidades"])//2])

#Nivel 3, Ejercicio 1.2: Checar si en habilidades tiene python
print("Nivel 3, Ejercicio 1.2")
if "Python" in person["Habilidades"]:
    print(person["Habilidades"])

#Nivel 3, Ejercicio 1.3: Ponerle un titulo a la persona depende sus habilidades
print("Nivel 3, Ejercicio 1.3")
if "Habilidades" in person:
    ha= person["Habilidades"]
if "JavaScript" in ha and "React" in ha:
    print("He is a front end developer")
elif "Node" in ha and "Python" in ha and "MongoDB" in ha:
    print("He is a backend developer")
elif "Node" in ha and "React" in ha and "MongoDB" in ha:
    print("He is a fullstack developer")
else:
    print("unknown title")

#Nivel 3, Ejercicio 1.4: Imprimir la informacion del diccionario en forma de enunciado
print("Nivel 3, Ejercicio 1.4")
if person["Esta_Comprometido"]==True and "Finlandia" in person["Pais"]:
    print("Asabeneth Yeteyeh vive en Finlandia, el esta casado")