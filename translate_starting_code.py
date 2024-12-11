from tkinter import *
from tkinter import messagebox   # for error messages
from tkinter import ttk          # for the Separator GUI element

root = Tk()
root.title("Super Funtime")
wordsused=[]
prevword = StringVar(root, value="") 
roundcount = IntVar(root, value = 1)
playerindicator = IntVar(root, value=1)
def reset():
    print("reset button clicked")
    roundcount.set(1)
    playerindicator.set(1)
    prevword.set("") 
    wordsused=[]
def check():
    print("check button clicked")
    entered_text = InputField.get()
    previous_word = prevword.get()

    if roundcount.get() != 1 and entered_text.lower() in wordsused:
        messagebox.showerror('word check', 'The word has already been used, try a different word.')
        return
    elif roundcount.get() != 1 and entered_text[0].lower() != previous_word[-1].lower():
        messagebox.showerror('word check', f'The first letter of {entered_text} is not the same as the last letter of {previous_word}. Try a different word.')
        return
    roundcount.set(roundcount.get() + 1)
    if playerindicator.get() == 1:
        playerindicator.set(2)
    elif playerindicator.get() == 2:
        playerindicator.set(1)
    prevword.set(entered_text)
    wordsused.append(entered_text.lower())
    print(wordsused)
# Init buttons, labels, entries
ResetBut = Button(root, text='Reset', command=reset)
CheckBut = Button(root, text='Check', command=check)
InputField = Entry(root)
PlayerLabel = Label(root, text="Player: ")
RoundLabel = Label(root, text="Round: ")
PlayerC = Label(root, textvariable=playerindicator)
RoundC = Label(root, textvariable=roundcount)
PrevLab = Label(root, text="Previous: ")
WordLab = Label(root, text="Word: ")
PrevDispLab = Label(root, textvariable=prevword)
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
