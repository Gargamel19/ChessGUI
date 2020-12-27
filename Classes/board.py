from Classes.square import Square
import tkinter as tk
from Classes.Figures.Queen import Queen
from Classes.Figures.King import King
from Classes.Figures.Pawn import Pawn
from Classes.Figures.Rook import Rook
from Classes.Figures.Bishop import Bishop
from Classes.Figures.Knite import Knite


class Board:

    white_bottom = True

    color_black = ""
    color_white = ""
    squares = []
    window = None
    heigth = 0

    def __init__(self, window, heigth, color_white, color_black):
        self.color_white = color_white
        self.color_black = color_black
        self.window = window
        self.heigth = heigth
        for x in range(8):
            if x%2==0:
                if self.white_bottom:
                    white = True
                else:
                    white = False
            else:
                if self.white_bottom:
                    white = False
                else:
                    white = True
            self.squares.append([])
            line = self.squares[x]
            for y in range(8):
                if white:
                    line.append(Square("white", x, y, self.heigth))
                else:
                    line.append(Square("black", x, y, self.heigth))
                white = not white

    def print_board(self):
        canvas = tk.Canvas(self.window, width=self.heigth, height=self.heigth)

        for line in self.squares:
            for sqaure in line:
                if sqaure.color == "white":
                    sqaure.draw_square(self.color_white, canvas)
                else:
                    sqaure.draw_square(self.color_black, canvas)
        canvas.pack()

    def set_figure_to_coords(self, figure, coordinateA, coordinate1):
        x = 0
        y = 0

        if coordinateA == "a":
            a = 7
        elif coordinateA == "b":
            a = 6
        elif coordinateA == "c":
            a = 5
        elif coordinateA == "d":
            a = 4
        elif coordinateA == "e":
            a = 3
        elif coordinateA == "f":
            a = 2
        elif coordinateA == "g":
            a = 1
        elif coordinateA == "h":
            a = 0

        x = coordinate1-1

        if self.white_bottom:
            a = abs(a - 7)
            x = abs(x - 7)

        print(str(x) + ":" + str(a))

        self.squares[a][x].content = figure


    def reset_board(self):
        # Queens
        self.set_figure_to_coords(Queen("white"), "d", 1)
        self.set_figure_to_coords(Queen("black"), "d", 8)
        # Kings
        self.set_figure_to_coords(King("white"), "e", 1)
        self.set_figure_to_coords(King("black"), "e", 8)
        # Knites
        self.set_figure_to_coords(Knite("white"), "b", 1)
        self.set_figure_to_coords(Knite("white"), "g", 1)
        self.set_figure_to_coords(Knite("black"), "b", 8)
        self.set_figure_to_coords(Knite("black"), "g", 8)
        # Bishop
        self.set_figure_to_coords(Bishop("white"), "c", 1)
        self.set_figure_to_coords(Bishop("white"), "f", 1)
        self.set_figure_to_coords(Bishop("black"), "c", 8)
        self.set_figure_to_coords(Bishop("black"), "f", 8)
        # Rook
        self.set_figure_to_coords(Rook("white"), "a", 1)
        self.set_figure_to_coords(Rook("white"), "h", 1)
        self.set_figure_to_coords(Rook("black"), "a", 8)
        self.set_figure_to_coords(Rook("black"), "h", 8)
        # pawns
        self.set_figure_to_coords(Pawn("white"), "a", 2)
        self.set_figure_to_coords(Pawn("white"), "b", 2)
        self.set_figure_to_coords(Pawn("white"), "c", 2)
        self.set_figure_to_coords(Pawn("white"), "d", 2)
        self.set_figure_to_coords(Pawn("white"), "e", 2)
        self.set_figure_to_coords(Pawn("white"), "f", 2)
        self.set_figure_to_coords(Pawn("white"), "g", 2)
        self.set_figure_to_coords(Pawn("white"), "h", 2)
        self.set_figure_to_coords(Pawn("black"), "a", 7)
        self.set_figure_to_coords(Pawn("black"), "b", 7)
        self.set_figure_to_coords(Pawn("black"), "c", 7)
        self.set_figure_to_coords(Pawn("black"), "d", 7)
        self.set_figure_to_coords(Pawn("black"), "e", 7)
        self.set_figure_to_coords(Pawn("black"), "f", 7)
        self.set_figure_to_coords(Pawn("black"), "g", 7)
        self.set_figure_to_coords(Pawn("black"), "h", 7)
