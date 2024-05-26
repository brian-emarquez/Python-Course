# Interfas Grafica IX 
# Raddio Button


from tkinter import *

root=Tk()
varOpcion=IntVar()


def imprimir():
    #print(varOpcion.get())
    if varOpcion.get()==1:
        etiqueta.config(text="Has elegido masculino")

    else: 
        etiqueta.config(text="Has elegido femenino")

Label(root, text="Genero:").pack()

Radiobutton(root, text="Masculino", variable= varOpcion, value=1, comman=imprimir).pack()
Radiobutton(root, text="Femenino", variable= varOpcion, value=2, comman=imprimir).pack()

etiqueta=Label(root)#linea de texto
etiqueta.pack()

root.mainloop()