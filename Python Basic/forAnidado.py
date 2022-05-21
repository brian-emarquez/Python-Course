# FOR ANIDADOS

 # ITERADORES
def iterador():
    lista = [5, 6, 3, 2]
    it = iter(lista)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))


# FOR ANIDADOS
def for_anidado():
    numeros = [1, 2, 3]
    letras = ['a', 'b', 'c']

    for n in numeros:
        print(n)
        for l in letras:
            print(l)

# FOR MULtIICACION
def for_multiplicacion():
    for a in range(1, 11):
        for b in range(1,11):
            print(a, "*", b, "=", a*b)

def listas():
    lista = [["Brian", "Nico", "Luis"], [10, 11, 12, 13], [5.3, 2.2, 11.1]]
    
    for n in lista:
        for m in n:
            print(m)
        print("-------")
    print("-------")

def arreglo():     
     
     arreglo = []
     arreglo = [5,8,9,4]
     
     for i in range(len(arreglo)):
        for j in range((i+1), len(arreglo)):  
            print(arreglo[j])
     
     
if __name__ == '__main__':
    # iterador()
    # for_anidado()
    # for_multiplicacion()
    # listas()
    arreglo()