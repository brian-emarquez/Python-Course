#EJERCICIO 1
#escriba un prgrama donde tenga una lista y que, a continuacion elimine los elementos repetidos, por ultimo mostrar la lista

print("Ejercicio 1 - Primera Forma")
lista = [1,2,3,4,5,1,1,1,1,10,"brian"]

conjunto = set(lista)
lista = list(conjunto) # cambio a lista
print(lista)

print("========================================================================================")
#sengunda Forma con 1 sola linea de codigo
print("Ejercicio 1 - Segunda Forma")

list = list(set (lista))
print(lista)
