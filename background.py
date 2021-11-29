from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from functools import partial


root = Tk()
root.title("S0S_Project")
root.geometry("600x400")
root.resizable(False, False)


# creating a SOS text
myLabel = Label(root, text="S0S GAME")
myLabel.pack()
myLabel.place(x=100, y=1)


# using radio button to create game's options (simple game or general game)
var1 = StringVar()
var2 = StringVar()
simpleGame = Radiobutton(root, text="Simple Game", value=var1)
generalGame = Radiobutton(root, text="General Game", value=var2, padx=10)
simpleGame.deselect()
generalGame.deselect()
simpleGame.pack()
generalGame.pack()
simpleGame.place(x=180, y=1)
generalGame.place(x=300, y=1)


# red, blue string variable and set both of them empty 
redStringVar = StringVar()
redStringVar.set(None)
blueStringVar = StringVar()
blueStringVar.set(None)

redSO = [
    ('S', 'S'),
    ('O', 'O'),
]
blueSO = [
    ('S', 'S'),
    ('O', 'O'),
]


# red player's frame
redFrame = LabelFrame(root, text="Red Player", fg="red", labelanchor=W)
for choices, options in redSO:
    redButtons = Radiobutton(redFrame, text=choices, variable=redStringVar, value=options, fg="red").pack()
redFrame.pack(side=LEFT)
redFrame.place(x=5, y=100)


# blue player's frame
blueFrame = LabelFrame(root, text="Blue Player", fg="blue", labelanchor=W)
for choices, options in blueSO:
    blueButtons = Radiobutton(blueFrame, text=choices, variable=blueStringVar, value=options, fg="blue").pack()
blueFrame.pack(side=LEFT)
blueFrame.place(x=5, y=200)


# a varible deciding the players' turn
turn = 0 


# board game with 8x8 grid 
boardFrame = Frame(root, width=300, height=300, highlightbackground="red", highlightthickness="1")
boardFrame.place(relx=.5, rely=.5, anchor="center")


# create an empty 8x8 board
board = [[None for i in range (8)] for j in range (8)]  


# get_text() function passing 2 parameters row and column
def get_text(rows, columns):
    global turn 
    if board[rows][columns] == ' ':
        if turn % 2 == 0:
            board[rows][columns] = redStringVar.get()
        else:
            board[rows][columns] = blueStringVar.get()
        turn += 1
        button[rows][columns].config(text=board[rows][columns])


# create a GUI board 
def gameBoard(): 
    global button
    button = []
    for i in range(8):
        m = i
        button.append(i)
        button[i] = []
        for j in range(8):
            n = j
            button[i].append(j)

            get_t = partial(get_text, i, j)
            button[i][j] = Button(boardFrame, bg="white", command=get_t, height=2, width=4, relief=RAISED)
            button[i][j].grid(row=m, column=n)


gameBoard()



""" Activated the program """
root.mainloop()