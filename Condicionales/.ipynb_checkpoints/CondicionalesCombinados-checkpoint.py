#Condicionales Combinados
#Condicional Anidado

edad = int(input("Ingrese su Edad: "))
if edad>0:
	print("edad Aceptada")
	if edad>=18:
		print("Es mayor que edad")
	else:
		print("No Es mayor que edad")
else:
	print("Ingrese un numero valido")

print("______________________________________________")

edad1 = int(input("Ingrese su Edad: "))

if 0<edad1<100:
	if edad1>=18:
		print("Es mayor que edad")
	else:
		print("No Es mayor que edad")
else:
	print("Ingrese un numero valido")