from tkinter import *
from tkinter import ttk


root = Tk()
root.title("S0S")
root.geometry("600x400")
root.resizable(False, False)

# Creating a 2D board game
#board = [[None]*5]*5


boardFrame = Frame(root, width=300, height=300, highlightbackground="red", highlightthickness="1")
boardFrame.place(relx=.5, rely=.5, anchor="center")

rows = 8
columns = 8
board = [[None for i in range (rows)] for j in range (columns)]

def black(b):	
	b.configure(text="S")


for i in range(rows):
	for j in range(columns):
		board[i][j] = Button(boardFrame, bg="white", height=2, width=4, relief=RAISED)
		#board[i][j]["command"] = lambda b=board[i][j]:black(b)
		board[i][j].grid(row=i, column=j)






root.mainloop()