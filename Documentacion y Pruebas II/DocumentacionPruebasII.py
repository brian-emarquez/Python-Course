# Documentacion y Pruebas II
# Modulo doctest

import doctest

def areaTriangulo(base , altura):

    #Test 
    """
    Calcula el area de un triangulo dado
    >>> areaTriangulo(3, 6)
    'El area del triangulo es 9.0'

    >>> areaTriangulo(4, 5)
    'El area del triangulo es 10.0'

    >>> areaTriangulo(9, 3)
    'El area del triangulo es 13.5'

    """
    return "El area del triangulo es " +str((base*altura)/2)

doctest.testmod()