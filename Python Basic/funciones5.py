# Funciones con diferente tipos de envio de datos
# kwargs

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Juan', 'Karla', 'Guillermo']
desplegarNombres(nombres)
desplegarNombres('Carlos')
"""desplegarNombres((8, 9))
desplegarNombres([10, 11])"""