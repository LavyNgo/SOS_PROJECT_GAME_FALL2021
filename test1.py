
from tkinter import *
from tkinter import messagebox
from functools import partial

root = Tk()
root.title("Tic Tac Toe")
root.geometry('700x500')
root.resizable(False, False)

BlueSOS = StringVar()
RedSOS = StringVar()
GameMode = StringVar()
BlueSOS.set(None)
RedSOS.set(None)
GameMode.set(None)
Value_1 = BlueSOS.get()
Value_2 = RedSOS.get()


frame2 = LabelFrame(root, text='Blue Player', bg='white')
frame2.place(x=10, y=150)

frame3 = LabelFrame(root, text='Red Player', bg='white')
frame3.place(x=610, y=150)

BoardFrame = Frame(root, highlightbackground="black", highlightthickness=1)
BoardFrame.place(relx=.5, rely=.5, anchor="center")

Label(root, text='SOS').place(x=200, y=10)
Radiobutton(root, text='Simple Game', variable=GameMode, value='Simple Game').place(x=250, y=10)
Radiobutton(root, text='General Game', variable=GameMode, value='General Game').place(x=400, y=10)

blueSOS = [
    ('S', 'S'),
    ('O', 'O'),
]
redSOS = [
    ('S', 'S'),
    ('O', 'O'),
]

for choice, option in blueSOS:
    Radiobutton(frame2, text=choice, variable=BlueSOS, value=option).pack(anchor=NW)

for choices, options in redSOS:
    Radiobutton(frame3, text=choices, variable=RedSOS, value=options).pack(anchor=NW)

# sign variable to decide the turn of which player
sign = 0

# Creates an empty board
global board
board = [[" " for x in range(6)] for y in range(6)]


def winner(b, S, O):
    return b[0][0] == S and b[0][1] == 0 and b[0][2] == 1


# Configure text on button while playing with another player
def get_text(i, j):
    global button
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            board[i][j] = BlueSOS.get()
        else:
            board[i][j] = RedSOS.get()
        sign += 1
        button[i][j].config(text=board[i][j])


# Create the GUI of game board for play along with another player

button = []
for i in range(6):
    m = 3+i
    button.append(i)
    button[i] = []
    for j in range(6):
        n = j
        button[i].append(j)
        get_t = partial(get_text, i, j)
        button[i][j] = Button(BoardFrame, bg="white", command=get_t, height=4, width=9, highlightbackground="white",
                              highlightthickness=0)
        button[i][j].grid(row=m, column=n)


root.mainloop()
