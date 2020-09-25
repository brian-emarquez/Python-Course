# Python Tkinter Text Bold and Italics Text
# Texto de Python Tkinter Texto en negrita y en cursiva

from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Python Tkinter Text Bold and Italics Text')
root.iconbitmap('Python Tkinter Text Bold and Italics Text/icons/panda.ico')
root.geometry("600x600")

# Read Only r
# read and write r+ (beginning of file)
# Write Only w (over-Written)
# Write and Read w+ (over written)
# Append Only a (end of file)
# Append and Read a+ (end of file)

#----------------------------------------------------------------------------Function--------------------------------------------------------------------------#
def open_txt():
    text_file = filedialog.askopenfilename(initialdir="Python Tkinter Text Bold and Italics Text/", title ="Open Text File", filetypes=(("Text Files", "*.txt"),))
    text_file = open(text_file, "r")
    stuff = text_file.read()

    my_text.insert(END, stuff)
    text_file.close()

def save_txt():
    text_file = filedialog.askopenfilename(initialdir="Python Tkinter Text Bold and Italics Text/", title ="Open Text File", filetypes=(("Text Files", "*.txt"),))
    text_file = open(text_file, "w")
    text_file.write(my_text.get(1.0, END))

def add_image():
    # Add Image 
    global my_image
    my_image = PhotoImage(file="Python Tkinter Text Bold and Italics Text/images/softwares.png")
    position = my_text.index(INSERT)
    my_text.image_create(position, image=my_image)

    my_label.config(text=position)

def select_text():
    selected = my_text.selection_get()
    my_label.config(text=selected)

def bolder():
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    my_text.tag_configure("bold", font=bold_font)

    current_tags = my_text.tag_names("sel.first")
    
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")


def italics_it():
    
    italic_font = font.Font(my_text, my_text.cget("font"))
    italic_font.configure(slant="italic")

    my_text.tag_configure("italic", font=italic_font)

    current_tags = my_text.tag_names("sel.first")
    
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")


#-------------------------------------------------Frame-------------------------------------------------------#
my_frame = Frame(root)
my_frame.pack(pady=10)

# Create Scrolbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=40, height=10, font=("Helvetica", 16), selectbackground="green", selectforeground="black", yscrollcommand=text_scroll)
my_text.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview)


open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=20)

save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(pady=20)

image_button = Button(root, text="Add Image", command=add_image)
image_button.pack(pady=5)

select_button = Button(root, text="Select Text", command=select_text)
select_button.pack(pady=5)

bold_button = Button(root, text="Bold", command=bolder)
bold_button.pack(pady=5)

italics_button = Button(root, text="italics", command=italics_it)
italics_button.pack(pady=5)

my_label = Label(root, text="")
my_label.pack(pady=5)

root.mainloop()
