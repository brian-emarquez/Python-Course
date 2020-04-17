#Conjustos 3
#Subconjustos

a = {1,2,3}
b = {3,4,5}

c = {1,2,3,4,5}
#los conjusto a de a estan en c
print(a.issubset(c))
print(a.issuperset(c))
print(a.isdisjoint(b)) # si no conparten un elemento en comun

print("==============================================================================================")
#volverlo Inmutable
print("Volverlo Inmutable")

a = frozenset({1,2,3})
#a = add(3)

