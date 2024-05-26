# FUNCIONES LAMBDA
# funciones anonima
# funciones on the go, on demand, online

'''def area_triangulo(base, altura):
    return(base*altura)/2

triangulo=area_triangulo(5,7)'''

# USANDO LAMBDA (no puede tener condicionales y bucles)
area_triangulo=lambda base, altura:(base*altura)/2

print(area_triangulo(7,5))



