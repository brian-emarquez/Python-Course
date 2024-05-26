from io import open
# creamos un txt, APERTURA
archivo_texto = open("archivo.txt","r") #r : modo lectura

#Lectura
texto = archivo_texto.read()
archivo_texto.close()
print(texto)



print("=================================================")

#r : modo lectura
archivo_texto1 = open("archivo.txt","r") 
lineas_texto1=archivo_texto1.readlines()
archivo_texto1.close()
print(lineas_texto1[0])# Imprime una lista


print("=================================================")

# Agregar
archivo_texto2 = open("archivo.txt","a") 
archivo_texto2.write("\n Siempre es una buena ocacion para estudiar python")
archivo_texto2.close()
