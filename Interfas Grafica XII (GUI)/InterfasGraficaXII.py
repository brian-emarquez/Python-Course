# Interfas Grafica XII
# Ventanas Emergentes

from tkinter import *
from tkinter import messagebox

root=Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Brian", "Procesador de textos")

def avisoLicencia():
    messagebox.showwarning("Licencias", "Producto bajo licencia GNU")

def salirAplicacion():
    # valor=messagebox.askcancel - buleano
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")# yes or no

    if valor=="yes":
        root.destroy()

def cerrarDocumnto():
    valor=messagebox.askretrycancel("reintentar", "No es posible cerrar el documento")# yes or no
    
    if valor==FALSE:
        root.destroy()



barraMenu=Menu(root)
root.config(menu=barraMenu, width=600, height=400)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumnto)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoHerramientas=Menu(barraMenu)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoAyuda=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)


root.mainloop()