contador = 0
miemail = input("Ingrese su correo: ")

for i in miemail:
    if(i=="@" or i=="."):
        contador=contador+1

if email==True:
    print("Correo Valido")
else:
    print("Correo invalido")