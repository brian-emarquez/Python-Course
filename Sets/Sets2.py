#Comjuntos

a = {1,2,3}
b = {3,4,5}

resultado = a==b
print(len(a))
print(resultado)

print("=========================================================================================")
#Unir 2 cojuntos
print("Union de 2 Conjustos")
c = a | b
print(c)

print("=========================================================================================")
# Interseccion
print("Interseccion de 2 Conjustos")
c = a & b
print(c)

print("=========================================================================================")
#Diferencia
print("Interseccion de 2 Conjustos")
c = a - b
print(c)

print("=========================================================================================")
#Diferencia Simetrica
print("Diferencia Simetrica")
c = a ^ b
print(c)


