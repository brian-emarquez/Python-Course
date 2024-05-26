# Validacion de Correo Electronico en Python

contador = 0
email = input("Ingrese su correo electronico: ")

for i in email:
    if ("@" or "."):
        contador = contador+1

if contador == 2:
    print("Correo Valido")
else:
    print("Correo Invalido")
