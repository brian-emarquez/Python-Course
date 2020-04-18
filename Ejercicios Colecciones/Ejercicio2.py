#Ejercicio 2

print("Ejercicio 2")

list1 = [1,2,3,4,5,7,7,0]
list2 = [5,6,7,8,9,10,10]

a = set(list1)
b = set(list2)

union = list(a | b)
solaA = list(a - b)
soloB = list(b - a)
inters = list(a & b)

print (f" es resultado de la lista de palabras que aparecen en las dos lista es: {union}")
print (f" es resultado de la lista de lapabras en la primera lista, pero no en la segunfa es: {solaA}")
print (f" es resultado de la lista de palabras que aparecen en la la segunda lista, pero no en la primera: {soloB}")
print (f" es resultado de la lista de palabras en ambas listas: {inters}")





