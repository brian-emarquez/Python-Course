# Listas

nombres = ['Juan','Karla','Ricardo', 'María']
# imprimir la lista nombres
print(nombres)
# acceder a los elementos de un a lista
print(nombres[0])
print(nombres[1])
# acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
#Imprimir un rago
print(nombres[0:2]) # sin incluir el índice 2
#Ir del inicio de la lista al índice (sin incluirlo)
print(nombres[:3])
#Desde el índice indicado hasta el final
print(nombres[1:])


#Cambiar un valor
nombres[3] = 'Ivone'
print(nombres)

#iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen más nombres en la lista')
# preguntar el largo de una lista


print(len(nombres))
# agregar un elemento
nombres.append('Lorenzo')
print(nombres)
# insertar un elemento en un índice en específico
nombres.insert(1, 'Octavio')
print(nombres)
# remover un elemento
nombres.remove('Octavio')
print(nombres)
# remover el último valor agregado
nombres.pop()
print(nombres)
# eliminar un indice
del nombres[0]
print(nombres)
# limpiar la lista
nombres.clear()
print(nombres)
# borrar la lista por completo
del nombres
print(nombres)