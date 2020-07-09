# Interfas Grafica V
# Scroll
# Botones

from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar()

#Frame
cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

#Caja de texto
cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)

scrollVert = Scrollbar(miFrame, command=textoComentario.yview) # scroll
scrollVert.grid(row=4, column=2, sticky= "nsew") #Scroll
textoComentario.config(yscrollcommand=scrollVert.set)# Scrol Dinamico



#Label
nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nonmbrePass=Label(miFrame, text="Password:")
nonmbrePass.grid(row=1, column=0, sticky="e", padx=10, pady=10)

nonmbreApellido=Label(miFrame, text="Apellido:")
nonmbreApellido.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionDireccion=Label(miFrame, text="Direccion:")
direccionDireccion.grid(row=3, column=0, sticky="e", padx=10, pady=10)

comentarioLabel=Label(miFrame, text="Comentarios:")
comentarioLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

#Botones

def codigoBoton():

    minombre.set("brian")

botonEnvio=Button(raiz, text="Enviar", command= codigoBoton)
botonEnvio.pack()




raiz.mainloop()