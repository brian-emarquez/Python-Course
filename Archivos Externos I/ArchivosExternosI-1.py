# Archivos EXternos

# Ojeticos : Persistencia de datos
# Mejos de Archivos externos
# Trabajo de BBDD

from io import open
# creamos un txt, APERTURA
archivo_texto = open("archivo.txt","w") #W : para abir el modo escritura
frase = "Estupendo dia  estudiar python \n El dia de hoy"

# MANUPULACION
archivo_texto.write(frase)

# CIERRE

archivo_texto.close()

