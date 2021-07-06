from tkinter import *
import tkinter.font as TkFont
from random import randrange

mainBackgroundcolor = "#EDFFB3"
mainTextColor = '#6767f5'
centerHorizontalValue = 5;
gridRowValue = 10;
gridColumnValue = 10;
lastGuess = False;

def initScreenSize(root):
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    appWidth = 700
    appHeight = 700
    positionMiddleX = (screenWidth/2) - (appWidth/2)
    positionMiddleY = (screenHeight/2) - (appHeight/2)
    root.geometry(f"{appWidth}x{appHeight}+{int(positionMiddleX)}+{int(positionMiddleY)}")


def configureAppInfo(root):
    #main app background color
    root.configure(bg=f'{mainBackgroundcolor}')

    
    #configure grid rows for main app
    rows = 0
    while rows < gridRowValue+1:
        root.rowconfigure(rows,weight=1)
        root.columnconfigure(rows,weight=1)
        rows += 1
    

def emptyFrame(root):
    for child in root.winfo_children():
        child.destroy()


def resetGame(root):
    for child in root.winfo_children():
        child.destroy()
    
    generateRangeForm(root)

def displayWinScreen(root, answer):
    startingRow = 0

    #display winning text
    winLabelFont = TkFont.Font(family="Helvetica",size=30,weight="bold")
    winLabel = Label(root, text='You won!', font=f'{winLabelFont}', fg=f'{mainTextColor}', bg=f'{mainBackgroundcolor}')
    winLabel.grid(row=startingRow, column=0, columnspan=10)

     #empty label for spacing
    emptyLabel = Label(root,text='', bg=f'{mainBackgroundcolor}')
    emptyLabel.grid(row=startingRow+1,column=0, columnspan=10)

    #display guess text
    resultLabel = Label(root, text='The number was: ', font=f'{winLabelFont}', fg=f'{mainTextColor}', bg=f'{mainBackgroundcolor}')
    resultLabel.grid(row=startingRow+2, column=0, columnspan=6)

    #display answer text
    resultLabel = Label(root, text=f'{answer}', font=f'{winLabelFont}', fg='black', bg=f'{mainBackgroundcolor}')
    resultLabel.grid(row=startingRow+2, column=6, columnspan=4)
    
    #empty label for spacing
    emptyLabel = Label(root,text='', bg=f'{mainBackgroundcolor}')
    emptyLabel.grid(row=startingRow+3,column=0, columnspan=10)

    #button to play again
    playAgainFont = TkFont.Font(family="Helvetica",size=20)
    playAgainButton = Button(root, text="Play Again!", font=f'{playAgainFont}', command= lambda: resetGame(root))
    playAgainButton.config(width=10,height=2, highlightbackground = "blue")
    playAgainButton.grid(row=startingRow+4, column=0, columnspan=10)

def submitGuess(root, guessText, userGuess, answer, fromRange, toRange):
    print(f'User guessed: {userGuess}. Actually answer: {answer}')

    if not userGuess.isnumeric():
        guessText.set('')
        guessText.set('Error: Must enter numeric values only');
        return

    #case if user guessed correctly
    if int(userGuess) == answer:
        emptyFrame(root)
        displayWinScreen(root, answer)

    global lastGuess

    if not lastGuess:
        lastGuess = int(userGuess)
        if abs(int(userGuess) - answer) < ((int(toRange)-int(fromRange))/2):
                guessText.set('')
                guessText.set('Warm')
        else:
                guessText.set('')
                guessText.set('Cold')
    
    else:
        if abs(answer-lastGuess) > abs(answer-int(userGuess)):
            guessText.set('')
            guessText.set('Getting warmer')
        else:
            guessText.set('')
            guessText.set('Getting colder')
         

def generateGame(root, fromValue, toValue, answer):
    print(f'answer: {answer}')
    startingRow = 0

    #display range label
    rangeLabelFont = TkFont.Font(family="Helvetica",size=30,weight="bold")
    guessRangeLabel = Label(root, text='Guess the number between ', font=f'{rangeLabelFont}', fg=f'{mainTextColor}', bg=f'{mainBackgroundcolor}')
    guessRangeLabel.grid(row=startingRow, column=0, columnspan=4)

    fromValueRangeLabel= Label(root, text=f'{fromValue}',font=f'{rangeLabelFont}', fg=f'black', bg=f'{mainBackgroundcolor}')
    fromValueRangeLabel.grid(row=startingRow, column=4, columnspan=1)

    toTextRangeLabel= Label(root, text='to',font=f'{rangeLabelFont}', fg=f'{mainTextColor}', bg=f'{mainBackgroundcolor}')
    toTextRangeLabel.grid(row=startingRow, column=5, columnspan=1)

    toValueRangeLabel= Label(root, text=f'{toValue}',font=f'{rangeLabelFont}', fg=f'black', bg=f'{mainBackgroundcolor}')
    toValueRangeLabel.grid(row=startingRow, column=6, columnspan=4)

    #empty label for spacing
    emptyLabel = Label(root,text='', bg=f'{mainBackgroundcolor}')
    emptyLabel.grid(row=startingRow+1,column=0, columnspan=10)

    #display input guesser
    smallerTextFont = TkFont.Font(family="Helvetica",size=20)
    userGuessEntry = Entry(root)
    userGuessEntry.grid(row=startingRow+2,column=3)
    userGuessEntry.config(font = f'{smallerTextFont}', highlightbackground = "black", highlightcolor= "black")

    #guess label
    guessText = StringVar()
    guessText.set('')
    guessLabel = Label(root, font=f'{smallerTextFont}', textvariable=guessText, bg=f'{mainBackgroundcolor}')
    guessLabel.grid(row=startingRow+3,column=0, columnspan=10)

    #button to submit guess
    submitGuessFont = TkFont.Font(family="Helvetica",size=20)
    submitGuessButton = Button(root, text="Guess!", font=f'{submitGuessFont}', command= lambda: submitGuess(root, guessText, userGuessEntry.get(), answer, fromValue, toValue ))
    submitGuessButton.config(width=10,height=2, highlightbackground = "blue")
    submitGuessButton.grid(row=startingRow+4, column=0, columnspan=10)

    #empty label for spacing
    emptyLabel = Label(root,text='', bg=f'{mainBackgroundcolor}')
    emptyLabel.grid(row=startingRow+5,column=0, columnspan=10)

    #button to reset game
    resetButton = Button(root, text="Reset", font=f'{submitGuessFont}', command= lambda: resetGame(root))
    resetButton.config(width=10,height=2, highlightbackground = "blue")
    resetButton.grid(row=startingRow+6, column=0, columnspan=10)


def submitRangeInfo(root,errorText, fromValue, toValue):
    print(f'from {fromValue} to {toValue}')
    if not fromValue.isnumeric() or not toValue.isnumeric():
        errorText.set('')
        errorText.set('Error: Must enter numeric values only');
        return
    
    elif int(fromValue) >= int(toValue):
        errorText.set('')
        errorText.set('Error: From value must be less than to value');

        return 

    else:
        numberToGuess = 0
        if fromValue == 0:
            numberToGuess = randrange(int(toValue)+1)
        else:
            numberToGuess = randrange(int(fromValue)-1, int(toValue)+1)
        emptyFrame(root)
        generateGame(root, fromValue, toValue, numberToGuess)

def generateRangeForm(root):
    startingRow = 0;
    
    #select range text
    rangeLabelFont = TkFont.Font(family="Helvetica",size=40,weight="bold")
    rangeLabel = Label(root,text='Select Range', font=f'{rangeLabelFont}', fg=f'{mainTextColor}', bg=f'{mainBackgroundcolor}');
    rangeLabel.grid(row=startingRow,column=0, columnspan=10)

    #empty label for spacing
    emptyLabel = Label(root,text='', bg=f'{mainBackgroundcolor}')
    emptyLabel.grid(row=startingRow+1,column=0, columnspan=10)

    #from text
    smallerTextFont = TkFont.Font(family="Helvetica",size=20)
    fromLabelFont = TkFont.Font(family="Helvetica",size=25,weight="bold")
    selectFromLabel = Label(root,text="From",font=f'{fromLabelFont}', fg='black', bg=f'{mainBackgroundcolor}')
    selectFromLabel.grid(row=startingRow+2,column=2);

    #from input field
    selectFromEntry = Entry(root)
    selectFromEntry.grid(row=startingRow+2,column=3)
    selectFromEntry.config(font = f'{smallerTextFont}', highlightbackground = "black", highlightcolor= "black")

    #to text
    fromLabelFont = TkFont.Font(family="Helvetica",size=25,weight="bold")
    selectToLabel = Label(root,text="To",font=f'{fromLabelFont}', fg='black', bg=f'{mainBackgroundcolor}')
    selectToLabel.grid(row=startingRow+2,column=5);

    #to input field
    selectToEntry = Entry(root)
    selectToEntry.grid(row=startingRow+2,column=6)
    selectToEntry.config(font=f'{smallerTextFont}', highlightbackground = "black", highlightcolor= "black")

    #error label 
    errorText = StringVar()
    errorText.set("")
    errorLabel = Label(root, font=f'{smallerTextFont}', textvariable= errorText, bg=f'{mainBackgroundcolor}')
    errorLabel.grid(row=startingRow+3,column=0, columnspan=10)

    #button to run game
    startButtonFont = TkFont.Font(family="Helvetica",size=20)
    startButton = Button(root, text="Start!", font=f'{startButtonFont}')
    startButton.config(width=10,height=2, highlightbackground = "blue", command= lambda: submitRangeInfo(root, errorText, selectFromEntry.get(), selectToEntry.get() ))
    startButton.grid(row=startingRow+4, column=0, columnspan=10)



def runGame():
    root = Tk()
    initScreenSize(root)
    configureAppInfo(root)
    

    startingRow=2
    #main label for game name
    mainLabelFont = TkFont.Font(family="Helvetica",size=50,weight="bold")
    mainLabel = Label(root,text="Guess The Number!",font=f'{mainLabelFont}',fg=f"{mainTextColor}", bg=f'{mainBackgroundcolor}')
    mainLabel.grid(row=startingRow,column=0, columnspan=10)

    #Frame for game
    mainFrame = Frame(root, bg=f'{mainBackgroundcolor}')
    mainFrame.grid(row=startingRow+1, column=0, columnspan=gridColumnValue)
    
    rows = 0
    while rows < gridRowValue+1:
        mainFrame.rowconfigure(rows,weight=1)
        mainFrame.columnconfigure(rows,weight=1)
        rows += 1
    #form for selecting range
    generateRangeForm(mainFrame);

    root.mainloop()

if __name__ == "__main__":
    runGame();