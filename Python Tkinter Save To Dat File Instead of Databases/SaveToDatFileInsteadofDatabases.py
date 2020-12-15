##########################################################
# Python Tkinter Save To Dat File Instead of Databases
# Guardar en archivo Dat en lugar de bases de datos
##########################################################

from tkinter import *
import pickle

root = Tk()
root.title('Python Tkinter Save To Dat File Instead of Databases')
root.iconbitmap('Python Tkinter Save To Dat File Instead of Databases/icons/arrow.ico')
root.geometry("500x400")

# Creatinf a list of sizes
sizes = [
    "Small",
    "Medium",
    "Large"
]

#my_text = Text(root, width=20, height=10)
#my_text.pack(pady=20)
my_list = Listbox(root)
my_list.pack(pady=20)

for item in sizes:
    my_list.insert(END, item)



def save_file():
    #Grab the studdd from our text box
    stuff = my_list.get(0, END)

    # Define a filename
    filename = "Python Tkinter Save To Dat File Instead of Databases/data/dat_stuff"

    # Opem the file
    output_file = open(filename, 'wb')
    
    # Actually add the data to the file
    pickle.dump(stuff, output_file)


def Open_file():
    # Define a filename
    filename = "Python Tkinter Save To Dat File Instead of Databases/data/dat_stuff"

    # Open the file
    input_file = open(filename, 'rb')

    #Load the data
    stuff = pickle.load(input_file)

    # output to text box
    for item in sizes:
        my_list.insert(END, item)

    print(stuff)

# delete from list box

def delete_items():
    my_list.delete(0, END)

my_button1 = Button(root, text="Save File", command=save_file)
my_button2 = Button(root, text="Open File", command=Open_file)
my_button3 = Button(root, text="Delete Items", command=delete_items)


my_button1.pack(pady=20)
my_button2.pack(pady=20)
my_button3.pack(pady=20)



root.mainloop()