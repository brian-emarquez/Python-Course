#Archivos Externos II - 2

from io import open
# creamos un txt, APERTURA
archivo_texto = open("archivo.txt","r") #r : modo lectura

#
archivo_texto.seek(len(archivo_texto.readline()))
print(archivo_texto.read())