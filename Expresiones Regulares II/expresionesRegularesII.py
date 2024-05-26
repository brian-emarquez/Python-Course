# Expresiones Regulares II
# Metacaracteres (caracter Comodin)

import re

lista_nombres=['Ana Gomez',
                'Maria Martin',
                'Sandra Lopez',
                'Santiago Martin',
                'Sandra Fernandez']

for elemento in lista_nombres:
    #if re.findall('^Sandra', elemento):# ^ ve cual de lo caracteres empiesa con sandra
    if re.findall('Martin$', elemento):
        print(elemento)

#########################################################################################
print("----------------Segunda parte-------------------")

lista_nombres1=['http://brianmarquez.org',
                'ftp://brianmarquez.org',
                'http://brianmarquez.coñ',
                'http://brianmarquez.com',
                'ftp://brianmarquez.com'
]

for elemento1 in lista_nombres1:
    if re.findall('[ñ]', elemento1):
        print(elemento1)
