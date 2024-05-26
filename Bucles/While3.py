# While 3
#Hacer un programa que saque la raiz cuadrada con 2 intentos

import math

intentos = 0
numero = int(input("Ingrese un Numero para sacar la raiz cuadrada: "))

while numero <0:
    print("¡Error: Numero negatico!")
    numero = int(input("Ingrese un Numero para sacar la raiz cuadrada: "))
    if(numero<0):
        intentos = intentos+1

    if intentos ==2:
        print("Llgo al limite de intentos")
        break

if intentos < 2:
    resultado = math.sqrt(numero)
    print(f"El resuldo es: {resultado}")
    



