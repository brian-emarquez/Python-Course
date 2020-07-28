# Expresiones Regulares IV
# Match y search

import re

cadena1="Jara Lopez"

cadena2= "456435646"

cadena3="a2342343"

if re.match("\d", cadena2): # numero
    print("Hemos encontrado el numero")
else:
    print("No Hemos encontrado el nombre")



