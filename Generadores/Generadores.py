#GENERADORES
# Estrucutra que entraen valor de unas funcion y almacenan en objetos iterables
#yield : contruye un objeto ietarble con el primer valor de la lista

#SIN GENERADOR
def generador_pares(Limite):
    num=1
    lista=[]

    while num<Limite:
        lista.append(num*2)
        num+=1

    return lista

print(generador_pares(10))

#CON GENERADOR

def generador_pares_1(Limite):
    num=1
   
    while num<Limite:
        yield num*2
        num+=1

print(generador_pares_1(10))

#HACEMOS UN RECORRIDO

def generador_pares_2(Limite):
    num=1
   
    while num<Limite:
        yield num*2
        num+=1

devuelvepares=generador_pares_2(10)

for i in devuelvepares:
    print(i)


# TRES PRIMEROS OBJETOS

def generador_pares_3(Limite):
    num=1
   
    while num<Limite:
        yield num*2
        num+=1

devuelvepares=generador_pares_2(10)
print("\n")
print(next(devuelvepares))
print("Aqui podria irel codigo")
print(next(devuelvepares))
print("Aqui podria irel codigo")
print(next(devuelvepares))
print("Aqui podria irel codigo")