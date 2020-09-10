# Python Tkinter Text to Speech
# Texto a voz de Python Tkinter

# pip install pyttsx3
# pip install pywin32

from tkinter import *
import pyttsx3 

root = Tk()
root.iconbitmap('Python Tkinter Text to Speech/pineapple.ico')
root.geometry("600x600") 
root.title('Python Tkinter Text to Speech')

engine = pyttsx3.init()
engine.say("Bienvenidos a Python Tkinter mmmmmmmmmmmmmmmmmmmmmmmmmmm")


engine.runAndWait()




root.mainloop()