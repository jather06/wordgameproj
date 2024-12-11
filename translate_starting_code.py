from tkinter import *
from tkinter import messagebox   # for error messages
from tkinter import ttk          # for the Separator GUI element

root = Tk()
root.title("Super Funtime")

def reset():
    print("reset button clicked")
def check():
    print("check button clicked")
def player():
    print('player 1/2')
def count():
    print('count xyz')
def prevword():
    print('this is prevword')

# Init buttons, labels, entries
ResetBut = Button(root, text='Reset', command=reset)
CheckBut = Button(root, text='Check', command=check)
InputField = Entry(root)
PlayerLabel = Label(root, text="Player: ")
RoundLabel = Label(root, text="Round: ")
PlayerC = Label(root, text="")
RoundC = Label(root, text="")
PrevLab = Label(root, text="Previous: ")
WordLab = Label(root, text="Word: ")
PrevDispLab = Label(root, text="")
Separator1 = ttk.Separator(root, orient="vertical")
# Arrange widgets on the screen
PlayerLabel.grid(row=0, column=0, sticky="e")
PlayerC.grid(row=0, column=1, sticky="w")
RoundLabel.grid(row=1, column=0, sticky="e")
RoundC.grid(row=1, column=1, sticky="w")
PrevLab.grid(row=0, column=2, sticky="e")
PrevDispLab.grid(row=0, column=3, sticky="w")
WordLab.grid(row=1, column=2, sticky="e")
InputField.grid(row=1, column=3, sticky="w")
ResetBut.grid(row=0, column=4, padx=5, pady=5)
CheckBut.grid(row=1, column=4, padx=5, pady=5)
Separator1.grid(row=0, column=1, rowspan=2, sticky="nse")
root.mainloop()
