from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from functools import partial
from copy import deepcopy
import random


root = Tk()
root.title("S0S_Project")
root.geometry("700x450")
root.resizable(False, False)


# board size variable

board_size_list = [6, 8, 9]
global board_size
board_size = random.choice(board_size_list)


# creating a SOS label text
myLabel = Label(root, text="S0S GAME")
myLabel.pack()
myLabel.place(x=100, y=1)


# using radio button to create game's options (simple game or general game)
gameMode = StringVar()
gameMode.set(None)
simpleGame = Radiobutton(root, text="Simple Game", value="Simple Game", variable=gameMode)
generalGame = Radiobutton(root, text="General Game", value="General Game", variable=gameMode, padx=10)
simpleGame.pack()
generalGame.pack()
simpleGame.place(x=220, y=1)
generalGame.place(x=350, y=1)


# red, blue string variable and set both of them empty 
redStringVar = StringVar()
redStringVar.set(None)
blueStringVar = StringVar()
blueStringVar.set(None)


# red player's frame
redMode = StringVar()
redMode.set(None)

redSO = [
    ('S', 'S'),
    ('O', 'O'),
]

redHuman = Radiobutton(root, text="Human", fg="red", variable=redMode, value="Human")
redPC = Radiobutton(root, text="Computer", fg="red", variable=redMode, value="Computer")
redHuman.place(x=5, y=120)
redPC.place(x=5,y=250)

redHumanFrame = LabelFrame(root, text="R", fg="red", labelanchor=N)
redHumanFrame.place(x=5,y=160)

for choices, options in redSO:
    redButtons = Radiobutton(redHumanFrame, text=choices, variable=redStringVar, value=options, fg="red").pack()



# blue player's frame
blueMode = StringVar()
blueMode.set(None)

blueSO = [
    ('S', 'S'),
    ('O', 'O'),
]

blueHuman = Radiobutton(root, text="Human", fg="blue", variable=blueMode, value="Human")
bluePC = Radiobutton(root, text="Computer", fg="blue", variable=blueMode, value="Computer")
blueHuman.place(x=600, y=120)
bluePC.place(x=600,y=250)

blueHumanFrame = LabelFrame(root, text="B", fg="blue", labelanchor=N)
blueHumanFrame.place(x=600, y=160)

for choices, options in blueSO:
    blueButtons = Radiobutton(blueHumanFrame, text=choices, variable=blueStringVar, value=options, fg="blue").pack()


# a varible deciding the players' turn 
global turn
turn = 0 


# a variable helding a current position (red or blue)
global position
position = 0


# red and blue point count for general mode
red_point_count = 0
blue_point_count = 0


# board game frame  
boardFrame = Frame(root, width=300, height=300, highlightbackground="red", highlightthickness="1")
boardFrame.place(relx=.5, rely=.5, anchor="center")


# board game
global board 
board = [[' ' for i in range (board_size)] for j in range (board_size)]  


# Check the board is full or not
def isfull():
    flag = True
    for i in board:
        if(i.count(' ') > 0):
            flag = False
    return flag


# winner check
def winner(b, s, o):
    return (
            # horizontal check
            (b[0][0] == s and b[0][1] == o and b[0][2] == s) or
            (b[0][1] == s and b[0][2] == o and b[0][3] == s) or
            (b[0][2] == s and b[0][3] == o and b[0][4] == s) or
            (b[1][0] == s and b[1][1] == o and b[1][2] == s) or
            (b[1][1] == s and b[1][2] == o and b[1][3] == s) or 
            (b[1][2] == s and b[1][3] == o and b[1][4] == s) or
            (b[2][0] == s and b[2][1] == o and b[2][2] == s) or
            (b[2][1] == s and b[2][2] == o and b[2][3] == s) or
            (b[2][2] == s and b[2][3] == o and b[2][4] == s) or
            (b[3][0] == s and b[3][1] == o and b[3][2] == s) or
            (b[3][1] == s and b[3][2] == o and b[3][3] == s) or
            (b[3][2] == s and b[3][3] == o and b[3][4] == s) or
            (b[4][0] == s and b[4][1] == o and b[4][2] == s) or
            (b[4][1] == s and b[4][2] == o and b[4][3] == s) or
            (b[4][2] == s and b[4][3] == o and b[4][4] == s) or
            (b[0][3] == s and b[0][4] == o and b[0][5] == s) or
            (b[1][3] == s and b[1][4] == o and b[1][5] == s) or
            (b[2][3] == s and b[2][4] == o and b[2][5] == s) or
            (b[3][3] == s and b[3][4] == o and b[3][5] == s) or
            (b[4][3] == s and b[4][4] == o and b[4][5] == s) or
            (b[5][3] == s and b[5][4] == o and b[5][5] == s) or
            (b[5][0] == s and b[5][1] == o and b[5][2] == s) or
            (b[5][1] == s and b[5][2] == o and b[5][3] == s) or
            (b[5][2] == s and b[5][3] == o and b[5][4] == s) or

            # vertical check
            (b[0][0] == s and b[1][0] == o and b[2][0] == s) or
            (b[1][0] == s and b[2][0] == o and b[3][0] == s) or
            (b[2][0] == s and b[3][0] == o and b[4][0] == s) or
            (b[0][1] == s and b[1][1] == o and b[2][1] == s) or
            (b[1][1] == s and b[2][1] == o and b[3][1] == s) or
            (b[2][1] == s and b[3][1] == o and b[4][1] == s) or
            (b[0][2] == s and b[1][2] == o and b[2][2] == s) or
            (b[1][2] == s and b[2][2] == o and b[3][2] == s) or
            (b[2][2] == s and b[3][2] == o and b[4][2] == s) or
            (b[0][3] == s and b[1][3] == o and b[2][3] == s) or
            (b[1][3] == s and b[2][3] == o and b[3][3] == s) or
            (b[2][3] == s and b[3][3] == o and b[4][3] == s) or
            (b[0][4] == s and b[1][4] == o and b[2][4] == s) or
            (b[1][4] == s and b[2][4] == o and b[3][4] == s) or
            (b[2][4] == s and b[3][4] == o and b[4][4] == s) or
            (b[0][5] == s and b[1][5] == o and b[2][5] == s) or
            (b[1][5] == s and b[2][5] == o and b[3][5] == s) or
            (b[2][5] == s and b[3][5] == o and b[4][5] == s) or
            (b[3][5] == s and b[4][5] == o and b[5][5] == s) or
            (b[3][4] == s and b[4][4] == o and b[5][4] == s) or
            (b[3][3] == s and b[4][3] == o and b[5][3] == s) or
            (b[3][2] == s and b[4][2] == o and b[5][2] == s) or
            (b[3][1] == s and b[4][1] == o and b[5][1] == s) or
            (b[3][0] == s and b[4][0] == o and b[5][0] == s) or

            # Diagol check
            (b[0][0] == s and b[1][1] == o and b[2][2] == s) or
            (b[1][1] == s and b[2][2] == o and b[3][3] == s) or
            (b[2][2] == s and b[3][3] == o and b[4][4] == s) or
            (b[0][1] == s and b[1][2] == o and b[2][3] == s) or
            (b[1][2] == s and b[2][3] == o and b[3][4] == s) or
            (b[0][2] == s and b[1][3] == o and b[2][4] == s) or
            (b[1][0] == s and b[2][1] == o and b[3][2] == s) or
            (b[2][1] == s and b[3][2] == o and b[4][3] == s) or
            (b[2][0] == s and b[3][1] == o and b[4][2] == s) or
            (b[0][4] == s and b[1][3] == o and b[2][2] == s) or
            (b[1][3] == s and b[2][2] == o and b[3][1] == s) or
            (b[2][2] == s and b[3][1] == o and b[4][0] == s) or
            (b[0][3] == s and b[1][2] == o and b[2][1] == s) or
            (b[1][2] == s and b[2][1] == o and b[3][0] == s) or
            (b[0][2] == s and b[1][1] == o and b[2][0] == s) or
            (b[1][4] == s and b[2][3] == o and b[3][2] == s) or
            (b[2][3] == s and b[3][2] == o and b[4][1] == s) or
            (b[2][4] == s and b[3][3] == o and b[4][2] == s) or
            (b[2][3] == s and b[1][4] == o and b[0][5] == s) or
            (b[5][0] == s and b[4][1] == o and b[3][2] == s) or
            (b[5][1] == s and b[4][2] == o and b[3][3] == s) or
            (b[1][5] == s and b[2][4] == o and b[3][3] == s) or
            (b[5][2] == s and b[4][3] == o and b[3][4] == s) or
            (b[2][5] == s and b[3][4] == o and b[4][3] == s) or
            (b[5][3] == s and b[4][4] == o and b[3][5] == s) or
            (b[3][0] == s and b[4][1] == o and b[5][2] == s) or
            (b[3][1] == s and b[4][2] == o and b[5][3] == s) or
            (b[3][2] == s and b[4][3] == o and b[5][4] == s) or
            (b[3][3] == s and b[4][4] == o and b[5][5] == s) or
            (b[2][3] == s and b[3][4] == o and b[4][5] == s) or
            (b[1][3] == s and b[1][4] == o and b[1][5] == s) or
            (b[0][3] == s and b[0][4] == o and b[0][5] == s))


def pc():
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
            if i in [[0, 0], [0, 2], [2, 0], [2, 2], [3, 3], [0, 3], [0, 6], [6, 6], [6, 0], [4, 6]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner) - 1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1], [3, 1], [3, 2], [4, 1], [4, 2], [4, 3], [0][6], [1][6], [2][6],
                     [3][6], [4][6], [5][6], [6][6], [7][7]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge) - 1)
            return edge[move]
            

# get_text() function passing 2 parameters row and column
def get_text(rows, columns):    
    global turn, position, gameMode, red_point_count, blue_point_count
    if redMode.get() == "Human" and blueMode.get() == "Human":
        if board[rows][columns] == ' ':
            if turn % 2 == 0: # red goes first 
                board[rows][columns] = redStringVar.get()
                position = "red turn"
                current_turn = Label(root, text="Current turn: red")
                current_turn.pack()
                current_turn.place(x=5, y=300)
                print(position)
            else: # blue goes after that
                board[rows][columns] = blueStringVar.get()
                position = "blue turn"
                current_turn = Label(root, text="Current turn: blue")
                current_turn.pack()
                current_turn.place(x=5, y=300)
                print(position)
            turn += 1
            print(turn)
            button[rows][columns].config(text=board[rows][columns])

    if redMode.get() == "Human" and blueMode.get() == "Computer":
        if board[rows][columns] == ' ':
            if turn % 2 == 0:
                board[rows][columns] = redStringVar.get()
                position = "red turn"
                current_turn = Label(root, text="Current turn: red")
                current_turn.pack()
                current_turn.place(x=5, y=300)
            else:
                bat = "S"
                man = "O"
                values = [bat, man]
                board[rows][columns] = random.choice(values)
                position = "blue turn"
                current_turn = Label(root, text="Current turn: blue")
                current_turn.pack()
                current_turn.place(x=5, y=300)
                print(position)
            turn += 1
            button[rows][columns].config(text=board[rows][columns], bg='orange')
        bool = True
        if (bool):
            if turn % 2 != 0:
                move = pc()
                print(move)
                button[move[0]][move[1]].config(state=DISABLED)
                get_text(move[0], move[1])
                
    if gameMode.get() == "Simple Game":
        if isfull():
            box = messagebox.showinfo("DRAW!!!", "What a game!")
        if position == "blue turn" and winner(board, "S", "O"):
            box = messagebox.showinfo("Winner!!!", "Blue player won the match!!!")
        if position == "red turn" and winner(board, "S", "O"):
            box = messagebox.showinfo("Winner!!!", "Red player won the match!!!")
          

    if gameMode.get() == "General Game":
        if isfull():
            if red_point_count > blue_point_count:
                box = messagebox.showinfo(
                    "Winner!!!", "Red player won the match!!!")
            if blue_point_count > red_point_count:
                box = messagebox.showinfo(
                    "Winner!!!", "Blue player won the match!!!")
            if red_point_count == blue_point_count:
                box = messagebox.showinfo("DRAW!!!", "What a game!")
        if position == "red turn" and winner(board, "S", "O"):
            red_point_count += 1
        if position == "blue turn" and winner(board, "S", "O"):
            blue_point_count += 1
         

        #print(red_point_count)
        #print(blue_point_count)

            
def game_board_display():  
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
            button[i][j] = Button(boardFrame, bg="white", command=get_t, height=2, width=4, relief=RAISED)
            button[i][j].grid(row=m, column=n)


# override imagine in the beginning of the game (310 - 336)
def onClick():
    global state, board_size
    sizeLabel["text"] = "It is " + str(board_size)
    if state == "Hidden":
        background_label.place_forget()

    elif state == "Showing":
        background_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        state = "Hidden"
        state = DISABLED


img = Image.open("hoir.png")
resize_img = img.resize((350, 400))

background_image = ImageTk.PhotoImage(resize_img)
background_label = Label(root, image=background_image)

state = "Hidden"

sizeLabel = Button(root, text="Board Size?", command=onClick)
sizeLabel.pack()
sizeLabel.place(x=500, y=1)

background_label.place(relx=0.5, rely=0.5, anchor=CENTER)


# destroy function, clear everything
def destroy():
    rb = Button(root, text="break!!!", command=root.destroy)
    rb.pack()
    rb.place(x=600, y=350)


# calling function 
game_board_display()
destroy()

""" Activated the program """
root.mainloop()
