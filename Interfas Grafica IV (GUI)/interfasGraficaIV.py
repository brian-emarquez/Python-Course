# Interfas Grafica IV
# Entry - Entrada de datos
# Grid
#padx,y

from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")


cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

#Label
nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nonmbrePass=Label(miFrame, text="Password:")
nonmbrePass.grid(row=1, column=0, sticky="e", padx=10, pady=10)

nonmbreApellido=Label(miFrame, text="Apellido:")
nonmbreApellido.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionDireccion=Label(miFrame, text="Direccion de la casa:")
direccionDireccion.grid(row=3, column=0, sticky="e", padx=10, pady=10)

raiz.mainloop()