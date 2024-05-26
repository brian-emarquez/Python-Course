# Pyhton Tkinter Image Buttons and Rounded Buttons
# Botones de imagen de Pyhton Tkinter y botones redondeados


from tkinter import *

root = Tk()
root.title('Python Tkinter Image Buttons and Rounded Buttons')
root.iconbitmap('Python Tkinter Image Buttons and Rounded Buttons/api.ico')
root.geometry("400x400")

def thing():
    my_label.config(text="You clicked the button...")

login_btn = PhotoImage(file="Python Tkinter Image Buttons and Rounded Buttons/images/login.png")

img_label = Label(image=login_btn)
#img_label.pack(pady=20)

my_button = Button(root, image=login_btn, command=thing, borderwidth=0)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()


