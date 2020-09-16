# Python TKinter Build An MP3 Player
# Python TKinter construye un reproductor MP3 

# pip install pygame

from tkinter import *
import pygame
from tkinter import filedialog
import time
#from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title('Python TKinter Build An MP3 Player')
root.iconbitmap('Python TKinter Build An MP3 Player/icons/music.ico')
root.geometry("500x350") 

# Initialize Pygame
pygame.mixer.init()

# Create Function To Add One Song To Playlist
def add_song():
	song = filedialog.askopenfilename(initialdir='Python TKinter Build An MP3 Player/audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3" ), ))
	# Strip out directory structure and .mp3 from song title
	song = song.replace("Python TKinter Build An MP3 Player/audio/", "")
	song = song.replace(".mp3", "")
	# Add To End of Playlist
	song_box.insert(END, song)


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

# Create Main Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Add Song Menu Dropdows
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
# Add One Song To Playlist
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)


root.mainloop() 