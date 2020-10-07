# Python Tkinter Custom Message Box Popups
# Ventanas emergentes del cuadro de mensaje personalizado de Python Tkinter

from tkinter import *

root = Tk()
root.title('Python Tkinter Custom Message Box Popups')
root.iconbitmap('Python Tkinter Custom Message Box Popups/Icons/like.ico')
root.geometry("300x300") 

def choice(option):
    pop.destroy()

    if option=="yes":
        my_label.configure(text="You Clicked Yes!")
    else:
        my_label.configure(text="You Clicked NO!!")


def cliker():
    global pop
    pop = Toplevel(root)
    pop.title("my Popup")
    root.geometry("300x250") 
    pop.configure(bg="green")

    global me
    me = PhotoImage(file="Python Tkinter Custom Message Box Popups/images/will.png")

    pop_label = Label(pop, text="Would you Like To Procedeed?", bg="green", fg="white", font=("helvetica", 12))
    pop_label.pack(pady=10)

    my_frame = Frame(pop, bg="green")
    my_frame.pack(pady=5)

    me_pic = Label(my_frame, image=me, borderwidth=0)
    me_pic.grid(row=0, column=0, padx=10)

    yes = Button(my_frame, text="YES", command=lambda: choice("yes"), bg='orange')
    yes.grid(row=0, column=1, padx=10)

    no = Button(my_frame, text="NO", command=lambda: choice("no"), bg='yellow')
    no.grid(row=0, column=2, padx=10)

my_button = Button(root, text="Click Me!", command=cliker)
my_button.pack(pady=50)

my_label= Label(root, text="")
my_label.pack(pady=20)

root.mainloop()