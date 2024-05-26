#Listas
demo_list = [1,"hola", 1.45, True]
colors = ['red', "blue", "red"]

#constructor - utilisando list
nombres_list = list({1,2,3,4}) # se utilizo una tupla {}
print (nombres_list)
#print (type(nombres_list))

#Rango===============================================================
rango = list(range(1,100))
print (rango) # miestras lo numero del 1 al 100

#Para tener informacion de las listas
print(len(colors)) # 3
print(colors[2]) # color red
print('red' in colors) # true
print('reds' in colors) # false

#====================================================================
print (colors)
colors[0] = "Black" # se cambio el red por el black
print (colors)


#====================================================================
colors.append("yelow") # se agrego al arreglo
#colors.extend(["yelow","yelow") # se agreso al arreglo
print(colors)

print("==============================================================")

colores = ["verde","azul","morado","amarillo"]
print(colores[0:3])