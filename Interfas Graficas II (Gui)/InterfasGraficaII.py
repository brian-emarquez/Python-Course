from tkinter import *

raiz=Tk()

raiz.title("Ventana de Prueba")
#raiz.resizable(0,0) #ancho y alto 
raiz.iconbitmap("Iconos\system.ico")
raiz.geometry("750x550")#Tamaño de la venta
raiz.config(bg="white")

#Frame
miFrame = Frame()
miFrame.pack()
miFrame.config(bg="red")

raiz.mainloop() #Bucle Infinito