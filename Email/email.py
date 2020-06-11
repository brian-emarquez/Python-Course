#Ingreso por Email, validando
correo = input("Ingrese su correo Electronico: ")
contador = 0

for i in correo:
    if (i=="@" or i=="."):
        contador=contador+1

if contador==1:
    print("El correo el valido")
else:
    print("El correo el Invalido")


