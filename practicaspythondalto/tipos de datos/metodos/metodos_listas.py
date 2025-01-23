#creamos una lista con list()
lista = list(["hola", "david", 35])

#cuenta y nos dice la cantidad de elementos dentro
#de la lista

cantidad_de_elementos_lista = len(lista)

#agrega un elemento a la lista
#agregando_con_append

lista.append("jeje")

#agrega un elemento a la lista en un indice específico

lista.insert(2, "trx")


#agrega varios elementos a la lista, siempre en formato lista


lista.extend(["ghnana", 35,65,"reder"])

print(lista)

#eliminar un dato de la lista por su indice

lista.pop(0) #elimina el primer argumento de la lista
lista.pop(-1)#eliminamos el ultimo porque vuelve al final
lista.pop(-2)#eliminamos el ante ultimo porque es uno menos que el ultimo

#removiendo un elemento de la lista por su valor
lista.remove("gdrf") #si lo encuentra lo elimina de la lista, sino lanza una excepcion

#eliminando todos los elementos de la lista, pero no la lista
#lista.clear()

#ordena los parametros de la lista
# primero van los False, luego los True y despues los numeros
#todo de menoa a mayor
#pero si le ponemos (reverse=True) los ordena al reves

lista.sort()
lista.sort(reverse=True)

#invirtiendo el orden de la lista
#no las ordena de ningun modo, solo revierte el orden
lista.reverse() 

