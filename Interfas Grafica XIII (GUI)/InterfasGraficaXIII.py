# Interfas Grafica XIII
# abrir ventanas - ficheros

from tkinter import *
from tkinter import filedialog

root=Tk()

def abreFichero(): 
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Fichero de Excel","*.xlsx"), ("Ficheros de texto", "*.txt")))
    print(fichero)
    
Button(root, text="Abrir fichero", command=abreFichero).pack()



root.mainloop()
