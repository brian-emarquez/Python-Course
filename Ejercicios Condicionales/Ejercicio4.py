#Ejercicio 4

#S, s = SUMA
#R, r.= RESTA
#M, m = Multiplicaion
#D, d  = Division

num1 = float(input("Ingrese un Numero: "))
num2 = float(input("Ingrese otro Numero: "))

operacion = input("Ingrese Un Letra: S, R, M, D\n").upper()

if operacion =="S":
	suma = num1 + num2
	print(f"el resultado de la suma es {suma}")

elif operacion == "R":
	resta = num1 - num2
	print(f"el resultado de la resta es {resta}")

elif operacion == "M":
	resta = num1 * num2
	print(f"el resultado de la multiplicacion es {resta}")

elif operacion == "D":
	resta = num1 / num2
	print(f"el resultado de la resta es {resta}")
else:
	print("se equiboco de operacion")





