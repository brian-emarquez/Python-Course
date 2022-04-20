# funcionesCantidaArgimento
# args

def listarNombres(*args): # cantidad de nombres desconocida
    for nombre in args:
        print(nombre)

listarNombres('Juan', 'Karla', 'María', 'Ernesto')
#listarNombres('Laura', 'Carlos')