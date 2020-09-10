# Python Tkinter Mouse On Hover Image Animation
# Animación de imagen con el mouse sobre el mouse

from tkinter import *

root = Tk()
root.iconbitmap('Python Tkinter Mouse On Hover Image Animation/pineapple.ico')
root.geometry("600x600") 
root.title('Python Tkinter Mouse On Hover Image Animation')

def change(e):
    my_pic = PhotoImage(file="Python Tkinter Mouse On Hover Image Animation/images/dreamtheater2.png")
    my_label.config(image=my_pic)
    my_label.image = my_pic

def change_back(e):
    my_pic = PhotoImage(file="Python Tkinter Mouse On Hover Image Animation/images/dreamtheater1.png")
    my_label.config(image=my_pic)
    my_label.image = my_pic

def do_sumething():
    label2 = Label(root, text="You clicked the button")
    label2.pack()


my_pic = PhotoImage(file="Python Tkinter Mouse On Hover Image Animation/images/dreamtheater1.png")
my_label = Button(root, image=my_pic, command=do_sumething)
my_label.pack(pady=20)

my_label.bind("<Enter>", change)
my_label.bind("<Leave>", change_back)

root.mainloop()