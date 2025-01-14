#Creo una lista para demostrar que son los datos compuestos

lista = ["David Meynet","Soy David", True, 1.85]

#Creo ahora una Tupla, otra manera de organizar datos para ver las
# diferencias en el manejo de los mismos, en la tupla los datos no pueden
#ser modificados, esa es la diferencia

tupla = ("David Meynet","Soy David", True, 1.85)

# Imprimo en pantalla un elemento de esa lista teniendo en cuenta
# que los elementos de la lista empiezan con índice 0, se cuentan 
# del 0 al 9, siendo índice 0 el primer elemento de la lista

print(lista[0])

# Hago un cambio en los datos de la lista (que sí pueden ser
# modificados)

lista[1] = "Jorge"

#creo un conjunto de datos (set)
#El orden de los datos no es fijo pero no se pueden cambiar, sí se puede
#redefinir el conjunto (como declarar nuevamente una variable)
#pero no cambiar uno de los datos del "conjunto"

#Además no se accede a datos por índice y no se accede a elementos 
#duplicados

conjunto = {"David Meynet","Soy David", True, 1.85}

#creo un dicionario (dict)
diccionario = {
    "Nombre" : "David",
    "Edad": 35,
    "Trabajo": "Freelancer"
}

print(diccionario["Nombre"])

#imprimo el indice 1 de la lista para corroborar el cambio
print(lista[1])
