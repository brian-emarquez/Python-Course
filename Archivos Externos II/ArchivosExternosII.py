#Archivos Externos II
#Metodo seek(): realiza la ubicacion del puntero.

from io import open
# creamos un txt, APERTURA
archivo_texto = open("archivo.txt","r") #r : modo lectura

print(archivo_texto.read()) # hace lectura
archivo_texto.seek(0) # posiciona el puntero a inicio - 0
print(archivo_texto.read(11)) # Hace Lectura hasta el espacio 11
