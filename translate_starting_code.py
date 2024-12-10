from tkinter import *

root = Tk()

words_en = ["mouse", "armadillo", "caterpillar", "buffalo", "dragonfly", "eel", "platypus", "lark", "manatee", "squid"]
words_nl = ["muis", "gordeldier", "rups", "buffel", "libelle", "paling", "vogelbekdier", "leeuwerik", "zeekoe", "inktvis"]
def previous():
    print("previous button clicked")
def next():
    print("next button clicked")
def check():
    print("check button clicked")

# Init buttons, labels, entries
PrevBut = Button(root, text='Previous', command=previous)
NextBut = Button(root, text='Next', command=next)
CheckBut = Button(root, text='Check', command=check)
InputField = Entry(root)


# Arrange widgets on the screen
PrevBut.pack(side=LEFT)
NextBut.pack(side=LEFT)
CheckBut.pack(side=RIGHT)
InputField.pack(side=RIGHT)

root.mainloop()
