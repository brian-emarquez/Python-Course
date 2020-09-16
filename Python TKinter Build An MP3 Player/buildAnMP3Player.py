# Python TKinter Build An MP3 Player
# Python TKinter construye un reproductor MP3 

# pip install pygame

from tkinter import *
import pygame

root = Tk()
root.title('Python TKinter Build An MP3 Player')
root.iconbitmap('Python TKinter Build An MP3 Player/icons/music.ico')
root.geometry("500x300") 

# Initializa Pygame Mixer
pygame.mixer.init()

#create PLayñist Box
song_box = Listbox(root, bg="black", fg="green", width=60)
song_box.pack(pady=20)

# Define Button Images For Controls
back_btn_img = PhotoImage(file='Python TKinter Build An MP3 Player/images/back50.png')
forward_btn_img = PhotoImage(file='Python TKinter Build An MP3 Player/images/forward50.png')
play_btn_img = PhotoImage(file='Python TKinter Build An MP3 Player/images/play50.png')
pause_btn_img = PhotoImage(file='Python TKinter Build An MP3 Player/images/pause50.png')
stop_btn_img = PhotoImage(file='Python TKinter Build An MP3 Player/images/stop50.png')

# Create Button Frame
control_frame = Frame(root)
# control_frame.grid(row=1, column=0, pady=20)
control_frame.pack(pady=20)


# Create Play/Stop etc Buttons
back_button = Button(control_frame, image=back_btn_img, borderwidth=0)
forward_button = Button(control_frame, image=forward_btn_img, borderwidth=0)
play_button = Button(control_frame, image=play_btn_img, borderwidth=0)
pause_button = Button(control_frame, image=pause_btn_img, borderwidth=0)
stop_button = Button(control_frame, image=stop_btn_img, borderwidth=0)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

root.mainloop() 