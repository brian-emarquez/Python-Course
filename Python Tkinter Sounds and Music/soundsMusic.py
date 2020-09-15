# Python Tkinter Sounds and Music
# Sonidos y música de Python Tkinter

# pip install pygame


from tkinter import *
import pygame
root = Tk()
root.title('Python Tkinter Sounds and Music')
root.iconbitmap('Python Tkinter Sounds and Music/sound.ico')
root.geometry("500x400") 

pygame.mixer.init()

def play():
    pygame.mixer.music.load("Python Tkinter Sounds and Music/sound/rock-808.mp3")
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    

my_button = Button(root, text="Play Song", font=("Helvetica", 32), command=play)
my_button.pack(pady=20)

stop_button = Button(root, text="Stop", command=stop)
stop_button.pack(pady=20)


root.mainloop()