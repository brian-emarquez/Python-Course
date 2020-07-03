#Cambio , remplazo de cadena de Letras
print("=================================================================")

archivo_texto = open("archivo.txt","r+") # Archivo de Lectura y escritura

lista_texto=archivo_texto.readlines()
lista_texto[1]= " Estas linea ha sido incluioda desde el exterior 2 \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()