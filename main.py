from Classes.board import Board
from Classes.ImageLoader import ImageLoader
import tkinter as tk
from screeninfo import get_monitors

window = tk.Tk()

min_value = min(get_monitors()[0].height, get_monitors()[0].width) - 100

window.geometry(str(min_value) + 'x' + str(min_value) + "+" + str(int((get_monitors()[0].width-min_value)/2)) + "+0")

board = Board(window, min_value, "#FFFFFF", "#94633a")
board.reset_board()


board.print_board()

window.mainloop()