####################################################################
# Python TKinter Using Entry Boxes On Canvas
# Python TKinter usando cuadros de entrada en lienzo
####################################################################

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Python TKinter Using Entry Boxes On Canvas')
root.iconbitmap('Python TKinter Using Entry Boxes On Canvas/icons/canvas.ico')
root.geometry("323x576") 
#make sure app
root.resizable(width=False, height=False)

# Define background Image
bg = ImageTk.PhotoImage(file="Python TKinter Using Entry Boxes On Canvas/images/background.jpg")

# Define canvas
my_canvas = Canvas(root, width=323, height=576, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# Put the image on the canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")

# Define Entry Boxes
un_entry = Entry(root,font=("Helvetica", 24), width=14, fg="#336d92", bd=0)
pw_entry = Entry(root,font=("Helvetica", 24), width=14, fg="#336d92", bd=0)


un_entry.insert(0, "username") 
pw_entry.insert(0, "password") 

# Add the entry boxes to the canvas
un_window = my_canvas.create_window(34, 290, anchor="nw", window=un_entry)
pw_window = my_canvas.create_window(34, 370, anchor="nw", window=pw_entry)

#Define function Welcome
def welcome():
    un_entry.destroy()
    pw_entry.destroy()
    login_btn.destroy()

    # Add a welcome message
    my_canvas.create_text(160, 450, text="welcome", font=("Helvetica", 40), fill="white" )


# Define Button
login_btn = Button(root, text="Login", font=("Helvetica", 20), width=15, fg="#336d92", command=welcome)
login_btn_window = my_canvas.create_window(36, 470, anchor="nw", window=login_btn)


# Define entry_Clear function
def entry_clear(e):
    if un_entry.get() == 'username' or pw_entry.get() == 'password':
        un_entry.delete(0,END)
        pw_entry.delete(0,END)
        # change text t o starts
        pw_entry.config(show="*")


# Bind the entry boxes
un_entry.bind("<Button-1>", entry_clear)
un_entry.bind("<Button-1>", entry_clear)




root.mainloop()