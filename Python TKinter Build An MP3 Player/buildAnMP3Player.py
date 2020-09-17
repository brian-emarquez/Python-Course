# Python TKinter Build An MP3 Player

from tkinter import *
from tkinter import filedialog
import pygame
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

# pip install pygame

from tkinter import *
import pygame

root = Tk()
root.title('Python TKinter Build An MP3 Player')
root.iconbitmap('Python TKinter Build An MP3 Player/icons/music.ico')
root.geometry("500x300") 

# Initializa Pygame Mixer
pygame.mixer.init()

def play_time():
	# Check to see if song is stopped
	if stopped:
		return

	# Grab Current Song Time
	current_time = pygame.mixer.music.get_pos() / 1000
	# Convert Song Time To Time Format
	converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))


	# Reconstruct song with directory structure stuff
	song = playlist_box.get(ACTIVE)
	song = f'Python TKinter Build An MP3 Player/sounds/{song}.mp3'

	# Find Current Song Length
	song_mut = MP3(song)
	global song_length
	song_length = song_mut.info.length
	# Convert to time format
	converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))
	
	# Check to see if song is over
	if int(song_slider.get()) == int(song_length):
		stop()

	elif paused:
		# Check to see if paused, if so - pass
		pass
	
	else: 
		# Move slider along 1 second at a time
		next_time = int(song_slider.get()) + 1
		# Output new time value to slider, and to length of song
		song_slider.config(to=song_length, value=next_time)

		# Convert Slider poition to time format
		converted_current_time = time.strftime('%M:%S', time.gmtime(int(song_slider.get())))

		# Output slider
		status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}  ')


	# Add Current Time To Status Bar
	if current_time > 0:
		status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}  ')
	
	# Create Loop To Check the time every second
	status_bar.after(1000, play_time)

# Create Function To Add One Song To Playlist
def add_song():
	song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3" ), ))
	# Strip out directory structure and .mp3 from song title
	song = song.replace("Python TKinter Build An MP3 Player/sounds/", "")
	song = song.replace(".mp3", "")
	# Add To End of Playlist
	playlist_box.insert(END, song)

# Create Function To Add Many Songs to Playlist
def add_many_songs():
	songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3" ), ))
	
	# Loop thru song list and replace directory structure and mp3 from song name
	for song in songs:
		# Strip out directory structure and .mp3 from song title
		song = song.replace("Python TKinter Build An MP3 Player/sounds/", "")
		song = song.replace(".mp3", "")
		# Add To End of Playlist
		playlist_box.insert(END, song)

# Create Function To Delete One Song From Playlist
def delete_song():
	# Delete Highlighted Song From Playlist
	playlist_box.delete(ANCHOR)

# Create Function To Delete All Songs From Playlist
def delete_all_songs():
	# Delete ALL songs 
	playlist_box.delete(0, END)

# Create Play Function
def play():
	# Set Stopped to False since a song is now playing
	global stopped
	stopped = False

	# Reconstruct song with directory structure stuff
	song = playlist_box.get(ACTIVE)
	song = f'Python TKinter Build An MP3 Player/sounds/{song}.mp3'
	
	#Load song with pygame mixer
	pygame.mixer.music.load(song)
	#Play song with pygame mixer
	pygame.mixer.music.play(loops=0)

	# Get Song Time
	play_time()

# Create Stopped Variable
global stopped
stopped = False 
def stop():
	# Stop the song
	pygame.mixer.music.stop()
	# Clear Playlist Bar
	playlist_box.selection_clear(ACTIVE)

	status_bar.config(text='')

	# Set our slider to zero
	song_slider.config(value=0)

	# Set Stop Variable To True
	global stopped
	stopped = True


	
# Create Function To Play The Next Song
def next_song():
	# Reset Slider position and status bar
	status_bar.config(text='')
	song_slider.config(value=0)

	#Get current song number
	next_one = playlist_box.curselection()
	# Add One To The Current Song Number Tuple/list
	next_one = next_one[0] + 1

	# Grab the song title from the playlist
	song = playlist_box.get(next_one)
	# Add directory structure stuff to the song title
	song = f'Python TKinter Build An MP3 Player/sounds//{song}.mp3'
	#Load song with pygame mixer
	pygame.mixer.music.load(song)
	#Play song with pygame mixer
	pygame.mixer.music.play(loops=0)

	# Clear Active Bar in Playlist
	playlist_box.selection_clear(0, END)

	# Move active bar to next song
	playlist_box.activate(next_one)

	# Set Active Bar To next song
	playlist_box.selection_set(next_one, last=None)

# Create function to play previous song
def previous_song():
	# Reset Slider position and status bar
	status_bar.config(text='')
	song_slider.config(value=0)

	#Get current song number
	next_one = playlist_box.curselection()
	# Add One To The Current Song Number Tuple/list
	next_one = next_one[0] - 1

	# Grab the song title from the playlist
	song = playlist_box.get(next_one)
	# Add directory structure stuff to the song title
	song = f'Python TKinter Build An MP3 Player/sounds/{song}.mp3'
	#Load song with pygame mixer
	pygame.mixer.music.load(song)
	#Play song with pygame mixer
	pygame.mixer.music.play(loops=0)

	# Clear Active Bar in Playlist
	playlist_box.selection_clear(0, END)

	# Move active bar to next song
	playlist_box.activate(next_one)

	# Set Active Bar To next song
	playlist_box.selection_set(next_one, last=None)


# Create Paused Variable
global paused 
paused = False

# Create Pause Function
def pause(is_paused):
	global paused
	paused = is_paused

	if paused:
		#Unpause
		pygame.mixer.music.unpause()
		paused = False
	else:
		#Pause
		pygame.mixer.music.pause()
		paused = True

#Create Volume Function
def volume(x):
	pygame.mixer.music.set_volume(volume_slider.get())

# Create a Slide Function For Song Positioning
def slide(x):
	# Reconstruct song with directory structure stuff
	song = playlist_box.get(ACTIVE)
	song = f'Python TKinter Build An MP3 Player/sounds/{song}.mp3'
	
	#Load song with pygame mixer
	pygame.mixer.music.load(song)
	#Play song with pygame mixer
	pygame.mixer.music.play(loops=0, start=song_slider.get())


# Create main Frame
main_frame = Frame(root)
main_frame.pack(pady=20)

# Create Playlist Box
playlist_box = Listbox(main_frame, bg="black", fg="green", width=60, selectbackground="green", selectforeground='black')
playlist_box.grid(row=0, column=0)

# Create volume slider frame
volume_frame = LabelFrame(main_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=20)

# Create Volume Slider
volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, length=125, value=1, command=volume)
volume_slider.pack(pady=10)

# Create Song Slider
song_slider = ttk.Scale(main_frame, from_=0, to=100, orient=HORIZONTAL, length=360, value=0, command=slide)
song_slider.grid(row=2, column=0, pady=20)

# Define Button Images For Controls
back_btn_img = PhotoImage(file='Python TKinter Build An MP3 Player/images/back50.png')
forward_btn_img = PhotoImage(file='Python TKinter Build An MP3 Player/images/forward50.png')
play_btn_img = PhotoImage(file='Python TKinter Build An MP3 Player/images/play50.png')
pause_btn_img = PhotoImage(file='Python TKinter Build An MP3 Player/images/pause50.png')
stop_btn_img = PhotoImage(file='Python TKinter Build An MP3 Player/images/stop50.png')


# Create Button Frame
control_frame = Frame(main_frame)
control_frame.grid(row=1, column=0, pady=20)

# Create Play/Stop etc Buttons
back_button = Button(control_frame, image=back_btn_img, borderwidth=0, command=previous_song)
forward_button = Button(control_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(control_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(control_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(control_frame, image=stop_btn_img, borderwidth=0, command=stop)

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
# Add Many Songs to Playlist
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

# Create Delete Song Menu Dropdowns
remove_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist", command=delete_all_songs)

# Create Status Bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)


# Temporary Label
my_label = Label(root, text='')
my_label.pack(pady=20)


root.mainloop()
