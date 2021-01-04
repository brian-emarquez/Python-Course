#####################################################
#Funciones Lambda
#####################################################

# Se Utiliza para abreviar, ahorar tiempo

'''def area_triangulo(base, altura):

    return(base*altura)/2

triangulo1 = area_triangulo(5, 7)
triangulo2 = area_triangulo(9, 6)

print(triangulo1)
print(triangulo2)
'''

# Simplifica la funciones
area_triangulo=lambda base, altura: (base*altura)/2
print(area_triangulo(5, 7))