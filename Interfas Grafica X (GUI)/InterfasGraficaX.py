# Check Button

from tkinter import *

root=Tk()

playa=IntVar()
montana=IntVar()
turismo=IntVar()

def opcionesViaje():
    opcionEscogida=""
    if(playa.get()==1):
        opcionEscogida+=" playa"

    if(montana.get()==1):
        opcionEscogida+=" montana"

    if (turismo.get()==1):
        opcionEscogida+=" turismo"

    textoFinal.config(text=opcionEscogida)

root.title("Destino de Viaje")

foto=PhotoImage(file="Interfas Grafica X (GUI)/car.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo", variable=turismo, onvalue=1, offvalue=0, command=opcionesViaje).pack()


textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()