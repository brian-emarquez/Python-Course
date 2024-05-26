##########################################################################
#  Python Tkinter How To Dynamically Resize Button Text
# Python Tkinter Cómo cambiar el tamaño del texto del botón de forma dinámica
##########################################################################

from tkinter import *

root = Tk()
root.title('Python Tkinter How To Dynamically Resize Button Text!')
root.iconbitmap('Python Tkinter How To Dynamically Resize Button Text/icons/back.ico')
root.geometry("500x500") 


Grid.columnconfigure(root, index=0, weight=1)
Grid.rowconfigure(root, 0, weight=1)
button_1 = Button(root, text="Button 1!")
button_1.grid(row=0, column=0, sticky="nsew")

def resize(e):
    #print(e)
    # Grab THE APP WIDHT AND DIVIDE BY 10
    size = e.width / 10
    # Change our button text size
    button_1.config(font=("Helvetica", int(size)))

    # Mess with height
    height_size =  e.height / 10
    if e.height <= 300:
        button_1.config(font=("Helvetica", int(height_size)))


#Bind the app
root.bind('<Configure>', resize)

root.mainloop()