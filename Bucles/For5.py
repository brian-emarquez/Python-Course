#FOR
#REPASOS
print("0. ======================================================================")


for i in ["Primavera", "verano", "invierno"]:
    print("i")

#comprobacion de un correo electronico
print("1. ======================================================================")

email = False
miemail = input("Ingrese su correo: ")

for i in miemail:
    if(i=="@"):
        email=True

if email==True:
    print("Correo Valido")
else:
    print("Correo invalido")

print("2. ======================================================================")

contador = 0
miemail = input("Ingrese su correo: ")

for i in miemail:
    if(i=="@" or i=="."):
        contador=contador+1

if email==True:
    print("Correo Valido")
else:
    print("Correo invalido")

print("3. ======================================================================")


#RANGE