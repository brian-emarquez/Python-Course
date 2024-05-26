# Documentacion y Pruebas III

import math

def raizCuadrada(listaNumeros):

    """
    La funcion devuelve una lista con la
    raiz cuadrada de los elemento numericos 
    pasados por parametos en otra lista

    >>> lista=[]
    >>> for i in [4, 9, 16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]
    


    """

    return [math.sqrt(n) for n in listaNumeros]

#print(raizCuadrada([9, 16, 25, 36])) 


import doctest
doctest.testmod()

