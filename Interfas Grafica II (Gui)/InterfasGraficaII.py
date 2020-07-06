from tkinter import *
#Raiz
raiz=Tk()

raiz.title("Ventana de Prueba")
raiz.iconbitmap("Iconos\system.ico")

raiz.config(bg="blue")

#Frame
miFrame = Frame()
miFrame.pack()
#miFrame.pack(fill="y", expand="True")
#mFrame.pack(side="right", anchor="n") #left, top, botton, right
miFrame.config(bg="red")
miFrame.config(width="650", height="350")
miFrame.config(relief="groove")
miFrame.config(bd=35)
miFrame.config(cursor= "hand2")


raiz.mainloop() #Bucle Infinito