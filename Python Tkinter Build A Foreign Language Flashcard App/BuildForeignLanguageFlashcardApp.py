#############################################################################################
#  Build A Foreign Language Flashcard App                                         ###########
#############################################################################################

from tkinter import *
from random import randint


root = Tk()
root.title('Python Tkinter Build A Foreign Language Flashcard App')
root.iconbitmap('Python Tkinter Build A Foreign Language Flashcard App/icons/iconfinde.ico')
root.geometry("550x410")

words  = [
    (("Hola"), ("Hello")),
    (("Adios"), ("GoodBye")),
    (("por favor"), ("Please")),
    (("gracias"), ("Thank you")),
    (("Lo siento"), ("Sorry")),
    (("Salud"), ("Bless You")),
    (("Si"), ("Yes")),
    (("No"), ("No")),
    (("¿Quien?"), ("Who")),
    (("¿Que?"), ("What")),
    (("¿por que?"), ("Why")),
    (("¿Donde?"), ("Where"))
]
# Get a count  of our word list
count = len(words)
#print(count)

def next():
    global hinter, hint_count
    # clear the scrren
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    hinter = ""
    hint_count = 0
    # cretae randon selection
    global random_word
    random_word = randint(0, count-1)
    # update label with spanish word
    spanish_word.config(text = words[random_word][0])

def answer():
    if my_entry.get().capitalize() == words[random_word][1]:
        answer_label.config(text=f"Correcto! {words[random_word][0]} es {words[random_word][1]} ")
    else:
        answer_label.config(text=f"Incorrecto! {words[random_word][0]} no es { my_entry.get().capitalize()} ")

# keep track of the hints
hinter = ""
hint_count = 0
def hint():
    global hint_count
    global hinter

    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1][hint_count]
        hint_label.config(text=hinter)
        hint_count +=1


spanish_word = Label(root, text = "", font=("Helvetica", 36))
spanish_word.pack(pady=50)

answer_label = Label (root, text="")
answer_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

# Create buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Respuesta", command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Siguiente", command=next)
next_button.grid(row=0, column=1)

hint_button = Button(button_frame, text="Pistas", command=hint)
hint_button.grid(row=0, column=2, padx=20)

# Create Hint Label
hint_label = Label (root, text="")
hint_label.pack(pady=20)

# run next functions
next()
root.mainloop()