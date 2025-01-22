#and: Este operador nos devuelve True si ambos resultados comparados son
#iguales, basta con que uno sea falso o los dos para que tire False

resultado  = True & True # devuelve True
resultado1 = False & True # devuelve False
resultado2 = True & False # devuelve False
resultado3 = True & True # devuelve True
resultado4 = False & False # devuelve False

#print(resultado)
#print(resultado1)
#print(resultado2)
#print(resultado3)
#print(resultado4)


#or, este operador solo nos devuelve False si ambas condiciones son
#falsas, con que sólo una ya sea True, nos devuelve siempre True

resultado5  = True | True #devuelve True
resultado6 = False | True #devuelve True
resultado7 = True | False #devuelve True
resultado8 = True | True #devuelve True
resultado9 = False | False #devuelve False



#not,cuando es verdad que (no es cierto algo) devuelve True
#y cuando no es verdad que (no es cierto algo) devuelve False

resultado10 = not 1 < 5 #devuelve False
resultado11 = not 6 < 5 #devuelve True 

print(resultado10)
print(resultado11)