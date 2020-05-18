#TUPLAS
# Las tuplas son inmutables , no se pueden cambiar (no se añade no se modifica)
#lent = cuenta los elementos 
#count = cuentos el mismo caracter o numero 

x = ("", "y", "z")
y = (1, 2, 3, 4, 5)
tupla= (10, 20, 30, 40)

print(type(x))#tuple
print(type(y))#tuple
#print(dir(x))

#para acceder a un eleneto de la tupla
print(y[0]) #1
print(y[1]) #2
print(y[2]) #3
print(y[3]) #4
print(y[4]) #5

#buscar por indice
print(tupla[2])

#buscar por nombre
print (30 in tupla)

print("===================================================")

#convertir tupla a lista
lista = list(tupla)
print(lista)
print(type(lista))



