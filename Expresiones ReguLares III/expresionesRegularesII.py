# Expresiones Regulares II
# Metacaracteres (caracter Comodin)

import re

lista_nombres=['Ana',
                'Pedro',
                'Maria',
                'Rosa',
                'Sandra',
                'Celia']

for elemento in lista_nombres:
    if re.findall('^[O-T]', elemento):
        print(elemento)

