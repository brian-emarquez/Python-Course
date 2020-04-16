#sets, Conjutos
#Lista desordenada sin indices
#no se puede tener otro tipo de colecciones: lista, tuplas, etc
#no puede haber valores duplicados

conjuntos = set()
conjuntos = {1,2,3,"brian", 4.6}
print(conjuntos)

("==================================================================================")
conjuntos.add(5)
print (conjuntos) # es agregado sin un orden

("==================================================================================")






print("=============================================================================")
colors = {"red", "black", "write"}

#print(type(colors))  # tipo de dato set
print("red" in colors)

#agregar un color al Sets
colors.add("violete")
print(colors)

#remoer elemento a sets
colors.remove("red")
print(colors)

# borra contenido al sets
colors.clear()
print(colors)
