#Interfas Grafica III
#Label

from tkinter import *
root=Tk()

miFrame = Frame(root, width=500, height=400)
miFrame.pack()
miImagen=PhotoImage(file="Interfas Grafica III (GUI)/giphy.gif")

#Label
miLabel=Label(miFrame, text="Hola Mundo", fg="red", font=("Comic Sans MS", 18))
miLabel.place(x=190, y=10)

Label(miFrame, image=miImagen).place(x=50, y=50)

root.mainloop() #Bucle Infinito