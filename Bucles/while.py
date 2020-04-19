#count = 1
count = int(input("Ingrese un numeros: "))

if count >= 6:
        print("el numero es mayor que 5")
while count <=5: #miesntra que en contrador
    print(count)
    count = count +1 # va aumentando hasta 5 , para que no sea infinito

print("============================================================================")
#Raiz cuadrada de un numero
print("Raiz cuadrada con While")
import math
numero = int (input ("Ingrese un Numero: "))

while numero<0:
    print("Error -> Ingrese un numero positivo")
    numero = int (input ("Ingrese un Numero: "))

print(f"Su raiz cuadrada es: {(math.sqrt(numero)):.2f}")



print("============================================================================")
#Mostar Hola Mundo 10 veces
print("Hola Mundo 10 veces")
nombre= 0
while(nombre<=10):
    print("Hola Mundo")
    nombre = nombre+1
