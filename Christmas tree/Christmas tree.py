###############################################################
# Christmas tree
###############################################################

import numpy as np

class ArbolNavidad:

    def __init__(self, size):
        self.size = size
    
    def obtener_num_capas(self):
        if(self.size == 'medium'):
            num_capas = 9
        elif(self.size == 'large'):
            num_capas = 15
        else:
            raise ValueError('El tamaño del arbolito debe ser: medium o large, no {}'.format(self.size))
        
        return num_capas
    
    def crear_ramas(self):
        hoja1 = '.'
        hoja2 = '.'
        espacios = ' '
        num_capas = self.obtener_num_capas()
        COLORS = ['\x1b[5;37;40m', '\x1b[9;37;40m']
        CEND = '\033[0m'
        for i in range(1, num_capas+1):
            capa = hoja1 + hoja2
            print("{0}{1}{2}{3}".format(espacios*(num_capas-i+5), np.random.choice(COLORS), capa*i, CEND))
    
    def crear_tronco(self):
        tronco = ".."
        espacios = ' '
        COLORS = ['\033[91m', '\x1b[2;100;100m']
        CEND = '\033[0m'
        num_capas = self.obtener_num_capas()
        for i in range(1, 4):
            print("{0}{1}{2}{3}".format(espacios*(num_capas+4), COLORS[1], tronco, CEND ))

    def mostrar_mensaje(self):
        print('***Feliz Navidad a Todos y \nPróspero Año Nuevo***\n\n')
if __name__ == "__main__":
    arbolito_obj = ArbolNavidad('medium')
    arbolito_obj.crear_ramas()
    arbolito_obj.crear_tronco()
    arbolito_obj.mostrar_mensaje()
