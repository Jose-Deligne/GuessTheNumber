from tkinter import *


def runGame():
    root = Tk()
    mainLabel = Label(root,text="Guess The Number!");
    mainLabel.pack()
    root.mainloop()

if __name__ == "__main__":
    runGame();