#Continue: Saltar a la siguiente interacion en el buble
#******************************************************
for i in "Python2":
    if (i=="h"):
        continue

    print(" La letras son : " + i)#Omite la H
#******************************************************
#pass: devuelve null

nombre = "brian marquez 3"
contador = 0

for i in nombre:
    if(i==" "):# si se encuntr en un espacio en blanco que ignore
        continue
    contador+=1

print(contador)

#else: simular a un condicion para decidir lo contrarios

