# Expresiones Regulares III
# Metacaracteres (caracter Comodin)

import re

lista_nombres=['Ma1',
                'Se1',
                'Ma2',
                'Ba1',
                'Ma3',
                'Va1',
                'va2',
                'Ma4',
                'MaA',
                'Ma5',
                'MaB',
                'MaC']

for elemento in lista_nombres:
    if re.findall('Ma[0-3A-B]', elemento): # muestra Ma1, Ma2, Ma3
        print(elemento)

