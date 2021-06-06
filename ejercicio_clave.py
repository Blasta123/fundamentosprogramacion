#Creo clave alfanumérica de 8 dígitos

clave = "Clave123"
contrasenia = " "
contador = 3

#Creo un ciclo finito para darle al usuario 3 oportunidades de ingresar
#la clave correcta

for clave in range(3):
    contrasenia = input("Ingrese contraseña: ")
    if contrasenia == "Clave123":
        print("Acceso correcto")
        break
    elif contrasenia != clave:
        print("Contraseña incorrecta, intente nuevamente")
    contador = contador -1
    
    if contador == 0:
        print("Usuario bloqueado")