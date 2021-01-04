from Classes.board import Board
import tkinter as tk

window = tk.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
min_value = min(screen_width, screen_height) - 100
textbox_size = 500

window.geometry(str(min_value+textbox_size) + 'x' + str(min_value) + "+" + str(int((screen_width-min_value-textbox_size)/2)) + "+0")

board = Board(window, min_value, "#FFFFFF", "#94633a", textbox_size)

window.mainloop()