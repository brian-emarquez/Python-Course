###############################################################################
# Python Tkinter How To Read A PDF File
# Python Tkinter Cómo leer un archivo PDF

# pip install PyPDF2
###############################################################################



from tkinter import *
import PyPDF2 
from tkinter import filedialog

root = Tk()
root.title("Python Tkinter How To Read A PDF File")
root.iconbitmap("Python Tkinter How To Read A PDF File/icons/adobe.ico")
root.geometry('500x500')

# Create a Textbox
my_text = Text(root, height=30, width=60)
my_text.pack(pady=10)

# Open PDF
def open_pdf():
    #grab the filename of the file
    open_file = filedialog.askopenfilename(
        initialdir="Python Tkinter How To Read A PDF File/documents", 
        title="Open PDF File",
        filetypes=(
            ("PDF FILES", "*.pdf"),
            ("All Files", "*.*")))

    #cheack to see if the is a file
    if open_pdf:
        #Open the PDF file
        pdf_file = PyPDF2.PdfFileReader(open_file)
        # set the page to read
        page = pdf_file.getPage(0)
        #extract the net from th pdf file
        page_stuff = page.extractText()

        #add text to textbox
        my_text.insert(1.0, page_stuff)





# clear the textbox
def clear_text_box():
    my_text.delete(1.0, END)

#Create A menu
my_menu = Menu(root)
root.config(menu=my_menu)

#add some dropdown menus
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_command(label="Clear", command=clear_text_box)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)



root.mainloop()