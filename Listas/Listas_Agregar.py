colors = ['red', "blue", "red"]

#insertar un color en una posicion dada

colors.insert(0, "White")
print (colors)

#insertar al final de la cadena
colors.insert(len(colors), "violete")
print (colors)

#Eliminar un elemento de la lista
colors.pop()
print (colors)

print("==============================================================")

lista = [1,2,3]
lista.extend([4,5,6])
print(lista)
