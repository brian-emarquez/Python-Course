
#Generadores 2
#Yield from  : simplificar el codigo de los generadores en el caso de utilizar bucles anidados

def devuelve_ciudades(*cuidades ): #el * sifnifica que va a resivir un numero indetermiad de elementos en forma de tupla
    for elementos in cuidades:
        for subelementos in elementos:
            yield subelementos

cuidades_devuelta= devuelve_ciudades("Lima", "arequipa", "Ica")
print(next(cuidades_devuelta))
print(next(cuidades_devuelta))

print("\n")

#Yield from
def devuelve_ciudades_1(*cuidades ): #el * sifnifica que va a resivir un numero indetermiad de elementos en forma de tupla
    for elementos in cuidades:
        yield from elementos

cuidades_devuelta= devuelve_ciudades_1("Lima", "arequipa", "Ica")
print(next(cuidades_devuelta))
print(next(cuidades_devuelta))


