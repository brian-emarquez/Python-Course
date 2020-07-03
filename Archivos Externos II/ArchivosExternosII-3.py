# Archos Externo II - 3

from io import open
# creamos un txt, APERTURA
archivo_texto = open("archivo.txt","r+") # Archivo de Lectura y escritura

archivo_texto.write("Comiendo de texto ")

print(archivo_texto.readlines())

