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
PlayerC = Label(root, command=player)
RoundC = Label(root, command=count)
PrevLab = Label(root, text="Previous: ")
WordLab = Label(root, text="Word: ")
PrevDispLab = Label(root, command=prevWord)
# Arrange widgets on the screen
PrevBut.pack(side=LEFT)
NextBut.pack(side=LEFT)
CheckBut.pack(side=RIGHT)
InputField.pack(side=RIGHT)

root.mainloop()
