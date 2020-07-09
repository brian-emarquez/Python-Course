# Interfas Grafica VII
# Interfas Calculadora
# Llamadas a funciones 
# Funciones lambda o anonimas


from tkinter import *

raiz = Tk()

miFrame=Frame(raiz)
miFrame.pack()

#Entry
#------------------------------Pantalla---------------------------------

numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #Espaciador
pantalla.config(background="black",fg="#2EF907", justify="right", width=30)

#--------------------------Pulsaciones teclado---------------------------


def numeroPulsado(num):
    numeroPantalla.set(numeroPantalla.get() + num)



#-------------------------------1 Fila-----------------------------------

buton7=Button(miFrame, text="7", width=7, height=3, command=lambda:numeroPulsado("7")) 
buton7.grid(row=2, column=1)

buton8=Button(miFrame, text="8", width=7, height=3, command=lambda:numeroPulsado("8"))
buton8.grid(row=2, column=2)

buton9=Button(miFrame, text="9", width=7, height=3, command=lambda:numeroPulsado("9"))
buton9.grid(row=2, column=3)

botonDiv=Button(miFrame, text="/", width=7, height=3)
botonDiv.grid(row=2, column=4)

#-------------------------------2 Fila-----------------------------------

buton4=Button(miFrame, text="4", width=7, height=3, command=lambda:numeroPulsado("4"))
buton4.grid(row=3, column=1)

buton5=Button(miFrame, text="5", width=7, height=3, command=lambda:numeroPulsado("5"))
buton5.grid(row=3, column=2)

buton6=Button(miFrame, text="6", width=7, height=3, command=lambda:numeroPulsado("6"))
buton6.grid(row=3, column=3)

botonMul=Button(miFrame, text="*", width=7, height=3, command=lambda:numeroPulsado("7"))
botonMul.grid(row=3, column=4)

#-------------------------------3 Fila-----------------------------------

buton1=Button(miFrame, text="1", width=7, height=3, command=lambda:numeroPulsado("1")) 
buton1.grid(row=4, column=1)

buton2=Button(miFrame, text="2", width=7, height=3, command=lambda:numeroPulsado("2"))
buton2.grid(row=4, column=2)

buton3=Button(miFrame, text="3", width=7, height=3 , command=lambda:numeroPulsado("3"))
buton3.grid(row=4, column=3)

botonRes=Button(miFrame, text="-",width=7, height=3, command=lambda:numeroPulsado("-"))
botonRes.grid(row=4, column=4)


#-------------------------------4 Fila-----------------------------------

buton0=Button(miFrame, text="0", width=7, height=3, command=lambda:numeroPulsado("0"))
buton0.grid(row=5, column=1)

butonComa=Button(miFrame, text=".", width=7, height=3, command=lambda:numeroPulsado(","))
butonComa.grid(row=5, column=2)

butonIgual=Button(miFrame, text="=", width=7, height=3, command=lambda:numeroPulsado("="))
butonIgual.grid(row=5, column=3)

botonSuma=Button(miFrame, text="+", width=7, height=3 , command=lambda:numeroPulsado("+"))
botonSuma.grid(row=5, column=4)

raiz.mainloop()
