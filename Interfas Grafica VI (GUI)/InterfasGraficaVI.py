# Interfas Grafica VI
# Interfas Calculadora
from tkinter import *

raiz = Tk()

miFrame=Frame(raiz)
miFrame.pack()

#Entry
#------------------------------Pantalla---------------------------------
pantalla=Entry(miFrame)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black",fg="#136F02", justify="right")

#-------------------------------1 Fila-----------------------------------

buton7=Button(miFrame, text="7", width=3)
buton7.grid(row=2, column=1)

buton8=Button(miFrame, text="8", width=3)
buton8.grid(row=2, column=2)

buton9=Button(miFrame, text="9", width=3)
buton9.grid(row=2, column=3)

botonDiv=Button(miFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)

#-------------------------------2 Fila-----------------------------------

buton4=Button(miFrame, text="4", width=3)
buton4.grid(row=3, column=1)

buton5=Button(miFrame, text="5", width=3)
buton5.grid(row=3, column=2)

buton6=Button(miFrame, text="6", width=3)
buton6.grid(row=3, column=3)

botonMul=Button(miFrame, text="*", width=3)
botonMul.grid(row=3, column=4)

#-------------------------------3 Fila-----------------------------------

buton1=Button(miFrame, text="1", width=3)
buton1.grid(row=4, column=1)

buton2=Button(miFrame, text="2", width=3)
buton2.grid(row=4, column=2)

buton3=Button(miFrame, text="3", width=3)
buton3.grid(row=4, column=3)

botonRes=Button(miFrame, text="-", width=3)
botonRes.grid(row=4, column=4)


#-------------------------------4 Fila-----------------------------------

buton0=Button(miFrame, text="0", width=3)
buton0.grid(row=5, column=1)

butonComa=Button(miFrame, text=".", width=3)
butonComa.grid(row=5, column=2)

butonIgual=Button(miFrame, text="=", width=3)
butonIgual.grid(row=5, column=3)

botonSuma=Button(miFrame, text="+", width=3)
botonSuma.grid(row=5, column=4)

raiz.mainloop()
