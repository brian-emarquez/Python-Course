# Expresiones Regulares I
# las expresiones reguales son una secuencia de caracteres que forman un patron de busqueda

# Sirven para el trabajo de procesamiento de texto

import re

cadena = "Vamos a aprender expresiones regulares en python. python es un lenguaje de sintaxis sencilla"

#buscarmos las palabre aprender
#print(re.search("aprender", cadena))

textoBuscar="aprender"
textoBuscar1="python"


if re.search(textoBuscar, cadena) is not None:
    print("He encontrado el texto")

else:
    print("No Encontre el texto")

###########################################################
textoEncontrado=re.search(textoBuscar,cadena)
print(textoEncontrado.start())# buscar el nuevo de caracteres hasta llegar a la palabra deficinida (aprender)
print(textoEncontrado.end())# carancte donde finaliza
print(textoEncontrado.span())# hace los 2 primeros metodos


###########################################################
print(re.findall(textoBuscar1, cadena))
print(len(re.findall(textoBuscar1, cadena))) #longitud
