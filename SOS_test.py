from tkinter import *
from tkinter import messagebox
from functools import partial
from copy import deepcopy
import time
import random

root = Tk()
root.title("SOS")
root.geometry('1100x800')
root.resizable(False, False)

global board_size
board_size = random.randint(8, 10)

# Buttons to choose between simple game and general game
GameMode = StringVar()
GameMode.set(None)
Label(root, font=('Times New Roman', 18), text='SOS').place(x=280, y=30)
Radiobutton(root, text='Simple Game', font=('Times New Roman', 18), variable=GameMode, value='Simple Game').place(x=380,
                                                                                                                  y=30)
Radiobutton(root, text='General Game', font=('Times New Roman', 18), variable=GameMode, value='General Game').place(
    x=530, y=30)
Label(root, font=('Times New Roman', 18), text='Board Size').place(x=730, y=30)
Label(root, font=('Times New Roman', 18), text=board_size).place(x=830, y=30)

# Blue Player GUI
blue_player = Label(root, font=('Times New Roman', 18), text='Blue Player').place(x=10, y=200)
Mode_1 = StringVar()
Mode_1.set(None)
Radiobutton(root, text='Human', font=('Times New Roman', 18), variable=Mode_1, value='Human').place(x=10, y=250)
Radiobutton(root, text='Computer', font=('Times New Roman', 18), variable=Mode_1, value='Computer').place(x=10, y=400)
frame = LabelFrame(root, font=('Times New Roman', 15), bg='white')
frame.place(x=10, y=300)
BlueSOS = StringVar()
BlueSOS.set(None)
blueSOS = [
    ('S', 'S'),
    ('O', 'O'),
]
for choice, option in blueSOS:
    Radiobutton(frame, font=('Times New Roman', 18), text=choice, variable=BlueSOS, value=option).pack(anchor=NW)

# Red Player GUI
red_player = Label(root, font=('Times New Roman', 18), text='Red Player').place(x=980, y=200)
Mode_2 = StringVar()
Mode_2.set(None)
Radiobutton(root, text='Human', font=('Times New Roman', 18), variable=Mode_2, value='Human').place(x=980, y=250)
Radiobutton(root, text='Computer', font=('Times New Roman', 18), variable=Mode_2, value='Computer').place(x=980, y=400)
frame2 = LabelFrame(root, font=('Times New Roman', 15), bg='white')
frame2.place(x=980, y=300)
RedSOS = StringVar()
RedSOS.set(None)
Value_2 = RedSOS.get()
redSOS = [
    ('S', 'S'),
    ('O', 'O'),
]

for choices, options in redSOS:
    Radiobutton(frame2, font=('Times New Roman', 18), text=choices, variable=RedSOS, value=options).pack(anchor=NW)

# Board Frame
BoardFrame = Frame(root, highlightbackground="black", highlightthickness=1)
BoardFrame.place(relx=.5, rely=.5, anchor="center")

# sign variable to decide the turn of which player
sign = 0

# Creates an empty board
global board
board = [[" " for x in range(board_size)] for y in range(board_size)]
turn = ''


def winner(b, l, r):
    return ((b[0][0] == l and b[0][1] == r and b[0][2] == l) or
            (b[0][2] == l and b[0][3] == r and b[0][4] == l) or
            (b[0][4] == l and b[0][5] == r and b[0][6] == l) or
            (b[0][1] == l and b[0][2] == r and b[0][3] == l) or
            (b[0][3] == l and b[0][4] == r and b[0][5] == l) or
            (b[0][5] == l and b[0][6] == r and b[0][7] == l) or

            (b[1][0] == l and b[1][1] == r and b[1][2] == l) or
            (b[1][2] == l and b[1][3] == r and b[1][4] == l) or
            (b[1][4] == l and b[1][5] == r and b[1][6] == l) or
            (b[1][1] == l and b[1][2] == r and b[1][3] == l) or
            (b[1][3] == l and b[1][4] == r and b[1][5] == l) or
            (b[1][5] == l and b[1][6] == r and b[1][7] == l) or

            (b[2][0] == l and b[2][1] == r and b[2][2] == l) or
            (b[2][2] == l and b[2][3] == r and b[2][4] == l) or
            (b[2][4] == l and b[2][5] == r and b[2][6] == l) or
            (b[2][1] == l and b[2][2] == r and b[2][3] == l) or
            (b[2][3] == l and b[2][4] == r and b[2][5] == l) or
            (b[2][5] == l and b[2][6] == r and b[2][7] == l) or

            (b[3][0] == l and b[3][1] == r and b[3][2] == l) or
            (b[3][2] == l and b[3][3] == r and b[3][4] == l) or
            (b[3][4] == l and b[3][5] == r and b[3][6] == l) or
            (b[3][1] == l and b[3][2] == r and b[3][3] == l) or
            (b[3][3] == l and b[3][4] == r and b[3][5] == l) or
            (b[3][5] == l and b[3][6] == r and b[3][7] == l) or

            (b[4][0] == l and b[4][1] == r and b[4][2] == l) or
            (b[4][2] == l and b[4][3] == r and b[4][4] == l) or
            (b[4][4] == l and b[4][5] == r and b[4][6] == l) or
            (b[4][1] == l and b[4][2] == r and b[4][3] == l) or
            (b[4][3] == l and b[4][4] == r and b[4][5] == l) or
            (b[4][5] == l and b[4][6] == r and b[4][7] == l) or

            (b[5][0] == l and b[5][1] == r and b[5][2] == l) or
            (b[5][2] == l and b[5][3] == r and b[5][4] == l) or
            (b[5][4] == l and b[5][5] == r and b[5][6] == l) or
            (b[5][1] == l and b[5][2] == r and b[5][3] == l) or
            (b[5][3] == l and b[5][4] == r and b[5][5] == l) or
            (b[5][5] == l and b[5][6] == r and b[5][7] == l) or

            (b[6][0] == l and b[6][1] == r and b[6][2] == l) or
            (b[6][2] == l and b[6][3] == r and b[6][4] == l) or
            (b[6][4] == l and b[6][5] == r and b[6][6] == l) or
            (b[6][1] == l and b[6][2] == r and b[6][3] == l) or
            (b[6][3] == l and b[6][4] == r and b[6][5] == l) or
            (b[6][5] == l and b[6][6] == r and b[6][7] == l) or

            (b[7][0] == l and b[7][1] == r and b[7][2] == l) or
            (b[7][2] == l and b[7][3] == r and b[7][4] == l) or
            (b[7][4] == l and b[7][5] == r and b[7][6] == l) or
            (b[7][1] == l and b[7][2] == r and b[7][3] == l) or
            (b[7][3] == l and b[7][4] == r and b[7][5] == l) or
            (b[7][5] == l and b[7][6] == r and b[7][7] == l) or

            (b[0][0] == l and b[1][0] == r and b[2][0] == l) or
            (b[2][0] == l and b[3][0] == r and b[4][0] == l) or
            (b[4][0] == l and b[5][0] == r and b[6][0] == l) or
            (b[1][0] == l and b[2][0] == r and b[3][0] == l) or
            (b[3][0] == l and b[4][0] == r and b[5][0] == l) or
            (b[5][0] == l and b[6][0] == r and b[7][0] == l) or

            (b[0][1] == l and b[1][1] == r and b[2][1] == l) or
            (b[2][1] == l and b[3][1] == r and b[4][1] == l) or
            (b[4][1] == l and b[5][1] == r and b[6][1] == l) or
            (b[1][1] == l and b[2][1] == r and b[3][1] == l) or
            (b[3][1] == l and b[4][1] == r and b[5][1] == l) or
            (b[5][1] == l and b[6][1] == r and b[7][1] == l) or

            (b[0][2] == l and b[1][2] == r and b[2][2] == l) or
            (b[2][2] == l and b[3][2] == r and b[4][2] == l) or
            (b[4][2] == l and b[5][2] == r and b[6][2] == l) or
            (b[1][2] == l and b[2][2] == r and b[3][2] == l) or
            (b[3][2] == l and b[4][2] == r and b[5][2] == l) or
            (b[5][2] == l and b[6][2] == r and b[7][2] == l) or

            (b[0][3] == l and b[1][3] == r and b[2][3] == l) or
            (b[2][3] == l and b[3][3] == r and b[4][3] == l) or
            (b[4][3] == l and b[5][3] == r and b[6][3] == l) or
            (b[1][3] == l and b[2][3] == r and b[3][3] == l) or
            (b[3][3] == l and b[4][3] == r and b[5][3] == l) or
            (b[5][3] == l and b[6][3] == r and b[7][3] == l) or

            (b[0][4] == l and b[1][4] == r and b[2][4] == l) or
            (b[2][4] == l and b[3][4] == r and b[4][4] == l) or
            (b[4][4] == l and b[5][4] == r and b[6][4] == l) or
            (b[1][4] == l and b[2][4] == r and b[3][4] == l) or
            (b[3][4] == l and b[4][4] == r and b[5][4] == l) or
            (b[5][4] == l and b[6][4] == r and b[7][4] == l) or

            (b[0][5] == l and b[1][5] == r and b[2][5] == l) or
            (b[2][5] == l and b[3][5] == r and b[4][5] == l) or
            (b[4][5] == l and b[5][5] == r and b[6][5] == l) or
            (b[1][5] == l and b[2][5] == r and b[3][5] == l) or
            (b[3][5] == l and b[4][5] == r and b[5][5] == l) or
            (b[5][5] == l and b[6][5] == r and b[7][5] == l) or

            (b[0][6] == l and b[1][6] == r and b[2][6] == l) or
            (b[2][6] == l and b[3][6] == r and b[4][6] == l) or
            (b[4][6] == l and b[5][6] == r and b[6][6] == l) or
            (b[1][6] == l and b[2][6] == r and b[3][6] == l) or
            (b[3][6] == l and b[4][6] == r and b[5][6] == l) or
            (b[5][6] == l and b[6][6] == r and b[7][6] == l) or

            # Diagonal
            (b[0][0] == l and b[1][1] == r and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == r and b[2][0] == l) or
            (b[0][3] == l and b[5][5] == r and b[6][5] == l) or
            (b[1][5] == l and b[2][5] == r and b[3][5] == l) or
            (b[3][5] == l and b[4][5] == r and b[5][5] == l) or
            (b[5][5] == l and b[6][5] == r and b[7][5] == l) or

            (b[0][5] == l and b[1][5] == r and b[2][5] == l) or
            (b[2][5] == l and b[3][5] == r and b[4][5] == l) or
            (b[4][5] == l and b[5][5] == r and b[6][5] == l) or
            (b[1][5] == l and b[2][5] == r and b[3][5] == l) or
            (b[3][5] == l and b[4][5] == r and b[5][5] == l) or
            (b[5][5] == l and b[6][5] == r and b[7][5] == l))


# Check the board is full or not
def isfull():
    flag = True
    for i in board:
        if i.count(' ') > 0:
            flag = False
    return flag


# Check if the player can push the button or not
def isfree(i, j):
    return board[i][j] == " "


BlueScore = 0
RedScore = 0


# Decide the next move of system
def RedComputer():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['S', 'O']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2], [3, 3], [0, 3], [0, 7], [7, 7], [7, 0], [4, 7]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner) - 1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1], [3, 1], [3, 2], [4, 1], [4, 2], [4, 3], [0][7], [1][7], [2][7],
                     [3][7], [4][7], [5][7], [6][7], [7][7], [8][7]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge) - 1)
            return edge[move]


# Decide the next move of system
def BlueComputer():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['S', 'O']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 7], [7, 7], [7, 0]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner) - 1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1], [3, 1], [3, 2], [4, 1], [4, 2], [4, 3], [0][7], [1][7], [2][7],
                     [3][7], [4][7], [5][7], [6][7], [7][7], [8][7]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge) - 1)
            return edge[move]


# Configure text on button while playing with another player
def get_text(i, j):
    global sign
    global turn
    global BlueScore
    global RedScore
    if Mode_1.get() == 'Human' and Mode_2.get() == "Human":
        if board[i][j] == ' ':
            if sign % 2 == 0:
                board[i][j] = BlueSOS.get()
                turn = 'Blue'
                Label(root, font=('Times New Roman', 18), text="Current turn: Blue").place(x=450, y=750)
            else:
                turn = 'Red'
                board[i][j] = RedSOS.get()
                Label(root, font=('Times New Roman', 18), text="Current turn: Red").place(x=450, y=750)
            sign += 1
            button[i][j].config(text=board[i][j], bg='orange')

    if Mode_1.get() == 'Human' and Mode_2.get() == 'Computer':
        if board[i][j] == ' ':
            print(sign)
            print(turn)
            if sign % 2 == 0:
                board[i][j] = BlueSOS.get()
                turn = 'Blue'
                Label(root, font=('Times New Roman', 18), text="Current turn: Blue").place(x=450, y=750)
            else:
                d = "S"
                c = "O"
                values = [d, c]
                board[i][j] = random.choice(values)
                turn = 'Red'
                Label(root, font=('Times New Roman', 18), text="Current turn: Red").place(x=450, y=750)
            sign += 1
            button[i][j].config(text=board[i][j], bg='orange')
        x = True
        if (x):
            if sign % 2 != 0:
                move = RedComputer()
                print(move)
                button[move[0]][move[1]].config(state=DISABLED)
                get_text(move[0], move[1])
    if Mode_1.get() == 'Computer' and Mode_2.get() == 'Human':
        if board[i][j] == ' ':
            if sign % 2 == 0:
                board[i][j] = RedSOS.get()
                turn = 'Red'
                Label(root, font=('Times New Roman', 18), text="Current turn: Red").place(x=450, y=750)
            else:
                d = "S"
                c = "O"
                values = [d, c]
                board[i][j] = random.choice(values)
                turn = 'Blue'
                Label(root, font=('Times New Roman', 18), text="Current turn: Blue").place(x=450, y=750)
            button[i][j].config(text=board[i][j], bg='orange')
            sign += 1
        x = True
        if (x):
            if sign % 2 != 0:
                move = BlueComputer()
                print(move)
                button[move[0]][move[1]].config(state=DISABLED)
                get_text(move[0], move[1])
    if Mode_1.get() == 'Computer' and Mode_2.get() == 'Computer':
        if board[i][j] == ' ':
            if sign % 2 == 0:
                variables = ['S', 'O']
                board[i][j] = random.choice(variables)
                turn = 'Blue'
                Label(root, font=('Times New Roman', 18), text="Current turn: Blue").place(x=450, y=750)
            else:
                d = "S"
                c = "O"
                values = [d, c]
                board[i][j] = random.choice(values)
                turn = 'Red'
                Label(root, font=('Times New Roman', 18), text="Current turn: Red").place(x=450, y=750)
            button[i][j].config(text=board[i][j], bg='orange')
            sign += 1
        x = True
        if (x):
            if sign % 2 == 0:
                move = BlueComputer()
                print(move)
                button[move[0]][move[1]].config(state=DISABLED)
                get_text(move[0], move[1])
            else:
                move_1 = RedComputer()
                print(move_1)
                button[move_1[0]][move_1[1]].config(state=DISABLED)
                get_text(move_1[0], move_1[1])
    if GameMode.get() == 'Simple Game':
        if isfull():
            box = messagebox.showinfo("Tie Game", "Tie Game")
        if turn == "Blue" and winner(board, 'S', 'O'):
            box = messagebox.showinfo("Blue player wins the game", "Blue Player win the games")
        if turn == "Red" and winner(board, 'S', 'O'):
            box = messagebox.showinfo("Red player wins the game", "Red Player win the games")
    elif GameMode.get() == 'General Game':
        print(BlueScore)
        print(RedScore)
        if isfull():
            if BlueScore == RedScore:
                box = messagebox.showinfo("Tie Game", "Tie Game")
            elif RedScore > BlueScore:
                box = messagebox.showinfo("Red player wins the game", "Red Player win the games")
            elif BlueScore > RedScore:
                box = messagebox.showinfo("Red player wins the game", "Red Player win the games")
        if turn == "Blue" and winner(board, 'S', 'O'):
            BlueScore += 1
        if turn == "Red" and winner(board, 'S', 'O'):
            RedScore += 1


global button
button = []
for i in range(board_size):
    m = i
    button.append(i)
    button[i] = []
    for j in range(board_size):
        n = j
        button[i].append(j)
        get_t = partial(get_text, i, j)
        button[i][j] = Button(BoardFrame, bg="white", command=get_t, height=4, width=9, highlightbackground="white",
                              highlightthickness=0)
        button[i][j].grid(row=m, column=n)

root.mainloop()
