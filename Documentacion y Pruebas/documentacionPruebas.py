# Documentacion y Pruebas
# Incluir comentarios en clases, metodos , modulos, etc


class Areas:
    
    """Esta clase cualcula las areas de diferentes figura geometricas"""

    def areaCuadrado(lado):

        """calculo el area de un cuadrado
        elevando al cuadrado el lado pasado por parametro"""

        return"el area del cuadrado es :" +str(lado*lado)


    def areaTriangulo(base, altura):

        """Calcula el area de un triangulo utilizando los parametros base y altura """

        return "el area del triangulo es: " +str((base*altura)/2)

#print(areaTriangulo(2,7))
#print(areaCuadrado.__doc__) # para ver la cocumentacion 
help(Areas.areaTriangulo)