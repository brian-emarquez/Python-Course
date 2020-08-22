# Python Tkinter Paned Windows
# ventanas con paneles de Python Tkinter

from tkinter import *

root = Tk()
root.title('Python Tkinter Paned Windows!')
root.iconbitmap('Python Tkinter Paned Windows/menu.ico')
root.geometry("400x400") 

# Panel
panel_1 = PanedWindow(bd=4, relief="raised", bg="red")
panel_1.pack(fill=BOTH, expand=1)

left_label = Label(panel_1, text="Left Panel")
panel_1.add(left_label)

# Second Panel
panel_2 = PanedWindow(panel_1, orient=VERTICAL, bd=4, relief="raised", bg="blue")
panel_1.add(panel_2)

top = Label(panel_2, text="Top Panel")
panel_2.add(top)

buton = Label(panel_2, text="Boton Panel")
panel_2.add(buton)

root.mainloop()