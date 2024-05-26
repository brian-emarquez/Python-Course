#Ejercicio 5

saldo = 1000

print("\t.:MENU:.") # recorrer espacio

print("1.  Ingresar dinero en la cuenta")
print("2.  Retirar Dinero de la Cuenta")
print("3.  Monstar Dinero")
print("4.  Salir")
print()
opcion = int(input("Elija una Opcion: "))
print()

if opcion==1:
	extra = float(input("Ingrese el valor de deposito: "))
	saldo = saldo + extra # saldo =+extra
	print(f"Su saldo actual es: {saldo}")

elif opcion==2:
	retiro = float(input("Ingrese el valor de retiro: "))
	if retiro > saldo:
		print ("No puede retirar el dinero")
	else:
		saldo = saldo - retiro # saldo =+extra
		print(f"Su saldo actual es: {saldo}")

elif opcion==3:
	print(f"el saldo actual es: {saldo}")

elif opcion==4:
	print("Gracias por utilizar el cajero automatico")

else:
	print("Error, se equivoco de opcion de menu")













