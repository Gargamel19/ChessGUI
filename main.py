from Classes.board import Board
from Classes.PGNReader import PGNReader
import tkinter as tk

window = tk.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
min_value = min(screen_width, screen_height) - 100


window.geometry(str(min_value) + 'x' + str(min_value) + "+" + str(int((screen_width-min_value)/2)) + "+0")

board = Board(window, min_value, "#FFFFFF", "#94633a")
pgn_r = PGNReader()
pgn_r.read(board, min_value/8)
#board.reset_board()



board.print_board()

window.mainloop()