# Python Tkinter Threading

from tkinter import *
import time
from random import randint
import threading

root = Tk()

root.title('Learn To Code at Python Pythin Tkinter Threading')
root.iconbitmap('Pythin Tkinter Threading/panda.ico')
root.geometry("500x400")

def five_seconds():
    time.sleep(5) # Espera de 5 segundos
    my_label.config(text="5 Secondsis Up!")
    
def rando():
    random_label.config(text=f"Random Number: {randint(1,1000)}") # Numero random
    
    
my_label = Label(root, text="Hello There!")
my_label.pack(pady=20)

my_button1 = Button(root, text="5 seconds", command=threading)
my_button1.pack(pady=20)

my_button2 =  Button(root, text="Pick Random Number", command=rando)
my_button2.pack(pady=20)

random_label = Label(root, text="")
random_label.pack(pady=20)

root.mainloop()
