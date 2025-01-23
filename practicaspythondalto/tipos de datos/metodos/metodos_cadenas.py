cadena1 = "Hola, soy David"
cadena2 = "Biemvenido"

resultado = "Que hacemoo!!" + cadena1.upper() + " " + cadena2.upper()

print(resultado)

#funcion que nos permite saber que operador podemos usar con la variable
#o dato pero si no le damos la funcion print, no muestra nada en pantalla

dir(cadena1) #no se muestra en pantalla
print(dir(cadena1)) # se muestra en pantalla la lista de operadores



#Operadores Dato.()
#convierte a minusculas

minusc = cadena1.lower()

#convierte a mayúsculas

mayusc = cadena1.upper()

#pone la primera letra en mayúsculas

primera_en_mayuscula = cadena1.capitalize()

#busca una cadena en otra cadena, si no hay coincidencias
#devuelve -1

busqueda_find = cadena1.find("f")

#buscamos una cadena en otra cadena, si no hay coincidencias
#lanza una excepcion (se corta el programa)

busqueda_index = cadena1.index("f")

#Este operador si es un dato numerico devuelve True, sino False

es_numerico = cadena1.isnumeric()

#si es alfanumerico devuelve True, sino False

es_alfanumerico = cadena1.isalpha()

#buscamos coincidencias de una cadena dentro de otra cadena, devuelve cantidad de
#coincidencias

contar_coincidencias = cadena1.count("f")

#contamos cuantos caracteres tiene una cadena
#no es un operador, es una funcion por eso se escribe distinto

contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con una cadena dada
#si es así, devuelve True

empieza_con = cadena1.startswith("f")

#verificamos si una cadena termina con una cadena dada
#si es así, devuelve True

termina_con = cadena1.endswith("f")

#reemplaza un valor o pedazo de la cadena por otro dado
#Si el valor que escribimos como a reemplazar, se encuentra en la
#cadena efectivamente, se reemplaza por el segundo valor que le damos
#si no coincide aunque sea una letra, no hace nada

cadena_nueva = cadena1.replace("Hola" , "Lu")

#separar cadenas con la cadena que le demos
#y crea una lista [] con la cadena separandola segun la cadena que 
#le damos (en este caso cada vez que encuentre "ftft" separaria
# los items de la cadena)

cadena_separada = cadena1.split("ftft")

