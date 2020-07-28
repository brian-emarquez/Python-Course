# Expresiones Regulares IV
# Match y search

import re

nombre1="Jara Lopez"

nombre2= "Antonio Gomez"

nombre3="Lara Lopez"

if re.match(".ara", nombre1, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No Hemos encontrado el nombre")



