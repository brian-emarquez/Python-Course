
# Documentacion y Pruebas II
# Modulo doctest



def compruebaMail(mailUsuario):

    #TEST
    """
    la funcion compruebaMail evalue un mail 
    recibido en busca de la @ si tiene una @ es correcto, 
    si tiene mas de una @ es incorrecto si la @
    esta a final es incorrecto

    >>> compruebaMail('juan@cursos.es')
    True

    >>> compruebaMail('juan@cursos.es@')
    False

    >>> compruebaMail('juancursos.es')
    False

    >>> compruebaMail('juan@cursos@.es@')
    False

    """

    arroba=mailUsuario.count('@')
    if (arroba!=1 or mailUsuario.rfind('@') == (len(mailUsuario)-1) or mailUsuario.find('@')==0):
        return False
    else:
        return True


import doctest
doctest.testmod()