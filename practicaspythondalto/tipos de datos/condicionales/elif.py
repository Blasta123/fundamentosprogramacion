ingreso_mensual= 12000
gasto_mensual = 1100

#if anidados y else-if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual >3000:
        print("Bien, estas muy bien así")
    else:
        print("Estás gastando mucho, no te va a alcanzar")
    print("Vivis muy bien en cualquier parte del mundo")


#podemos poner todos los elif que querramos hasta que cubra todas
#las condiciones que necesitemos

elif ingreso_mensual > 1000:
    print("Vivis muy bien en latinoamerica")
    
else:
    print("Sos pobre")