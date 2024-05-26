#Colas
#Colas de banco
print("Primera Instancia")
cola = ["Luis", "Brian", "Jose", "David"]
print(cola)

print("======================================================================================")
#AGRAMOS UN ELEMTO A LA COLA
print("Agregando un elemento a la cola")
cola.append("Yuliza")
print(cola)

print("======================================================================================")
#SACANDO ELEMTO POR EL PRINCIPIO
print("Sacando elemntos por el principio")
n=cola.pop(0)
print(f"Estan atendiendo {n} en el banco")
n=cola.pop(0)
print(f"Estan atendiendo {n} en el banco")
print(cola)
print("======================================================================================")


