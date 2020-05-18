#Pilas con funcione de Listas
#no existen directamente en python

pila = [1,2,3]
print(pila)
print("======================================================================================")
print("Agregando Elementos de Una Pila")
#AGRENDO ELEMENTO A UNA PILA
pila.append(4) 
pila.append(5)
pila.append(6)
pila.append(7)
print(pila)

print("======================================================================================")
#BORRAR ELEMENTOS DE UNA PILA (POR EL FINAL)
print("Borrando un Elemento de Una Pila")
n= pila.pop()
print(pila)
print(f"eh sacado: {n} de la pila")


