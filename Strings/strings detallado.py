mystr = "Hello World"

#dir()
#print(dir(mystr))
print (mystr.upper())  # lo cambia a mayuscula usando el meto Upper
print (mystr.lower())  # lo cambia a minuscula
print (mystr.capitalize())  # latra capital 
print (mystr.swapcase())  # mayuscula y minuscula seguidos

#cambio de palabra y volverlo mayuscula
print (mystr.replace("Hello", "Hola").upper())

#Contar los caracteres
print (mystr.count("l")) # tienes 2 veces las 3

#quiero saber si empiesa con la palabra Hola

print(mystr.startswith("H"))# si comienza con H
print(mystr.endswith("World"))

#dividir el texto
print (mystr.split("o"))#separa apartir de la o

#buscar la posicion en el elemento en el texto
#dir()
print (mystr.find("o"))
print (mystr.find(" ")) # espacop en blanco
print (len(mystr)) #longitud de la palabra 
print (mystr.index("e")) #incide de la palabra e 

#muesta la letra segun la posicion
print (mystr[4])