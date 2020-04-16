# Hacer un programa que pida 1 numeros y se de cuenta cual 
#de ellos es par , o si ambon son par
print("Ingrese 2 numeros eneteros")

a = int(input('ingrese un numero: '))
b = int(input('ingrese otro numero: '))

if(a%2==0 and b%2==0):
	print("Ambos numeros son pares")
elif (a%2==0 and b%2!=0):
	print(f"{a} es Par")
elif (a%2!=0 and b%2==0):
	print(f"{b} es par")
elif (a%2!=0 and b%2!=0):
	print("Ninguno es par")


