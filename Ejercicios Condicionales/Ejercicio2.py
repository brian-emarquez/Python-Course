# Hacer un prgrama que pide 3 numeros y 
# determine cual es el mayor

print("Ingrese 3 Numero Enteros")
num1 = int(input("Ingrese el NUmero 1: "))
num2 = int(input("Ingrese el NUmero 2: "))
num3 = int(input("Ingrese el NUmero 3: "))

if num1 > num2  and num1 > num3:
	print(f"el numero mayor es {num1}")
elif num2 > num3  and num2 > num1:
	print(f"el numero mayor es {num2}")
elif num3 > num2  and num3 > num1:
	print(f"el numero mayor es {num3}")



