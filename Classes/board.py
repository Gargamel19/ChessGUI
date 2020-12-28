from Classes.PGNReader import PGNReader
from Classes.square import Square
import tkinter as tk
from Classes.Figures.Queen import Queen
from Classes.Figures.King import King
from Classes.Figures.Pawn import Pawn
from Classes.Figures.Rook import Rook
from Classes.Figures.Bishop import Bishop
from Classes.Figures.Knight import Knight


class Board:

    SQUARES = [
        "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1",
        "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
        "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
        "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
        "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
        "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
        "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
        "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
    ]

    white_bottom = True

    color_black = ""
    color_white = ""
    squares = []
    window = None
    height = 0
    board_pgn = None
    canvas = None
    next_moves = []

    def __init__(self, window, height, color_white, color_black):
        self.color_white = color_white
        self.color_black = color_black
        self.window = window
        self.height = height
        self.canvas = tk.Canvas(window, width=height, height=height)
        self.canvas.pack()
        pgn_r = PGNReader(self)
        [self.board_pgn, next_moves] = pgn_r.read_random()
        print(next_moves)
        self.make_board_to_gui()

    def clean_board(self):

        for line in self.squares:
            for square in line:
                if square != None:
                    if square.content != None:
                        square.content.destroy()
                        square.content = None

        for x in range(8):
            if x % 2 == 0:
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
                    line.append(Square("white", x, y, self.height))
                else:
                    line.append(Square("black", x, y, self.height))
                white = not white

    def print_board(self):

        for line in self.squares:
            for sqaure in line:
                if sqaure.color == "white":
                    sqaure.draw_square(self.color_white, self.color_white, self.canvas)
                else:
                    sqaure.draw_square(self.color_black, self.color_black, self.canvas)


    def set_figure_to_coords(self, figure, coordinateA, coordinate1):

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

        self.squares[a][x].content = figure
        figure.set_square(a, x)
        figure.set_board(self)

    def get_coordinate_from_square(self, a, x):

        if self.white_bottom:
            a = abs(a - 7)
            x = abs(x - 7)

        if a == 7:
            a_erg = "a"
        elif a == 6:
            a_erg = "b"
        elif a == 5:
            a_erg = "c"
        elif a == 4:
            a_erg = "d"
        elif a == 3:
            a_erg = "e"
        elif a == 2:
            a_erg = "f"
        elif a == 1:
            a_erg = "g"
        elif a == 0:
            a_erg = "h"

        x = abs(x)
        x = x + 1

        return [a_erg, x]

    def reset_board(self):

        size = self.height / 8
        # Queens
        self.set_figure_to_coords(Queen("white", size), "d", 1)
        self.set_figure_to_coords(Queen("black", size), "d", 8)
        # Kings
        self.set_figure_to_coords(King("white", size), "e", 1)
        self.set_figure_to_coords(King("black", size), "e", 8)
        # Knites
        self.set_figure_to_coords(Knight("white", size), "b", 1)
        self.set_figure_to_coords(Knight("white", size), "g", 1)
        self.set_figure_to_coords(Knight("black", size), "b", 8)
        self.set_figure_to_coords(Knight("black", size), "g", 8)
        # Bishop
        self.set_figure_to_coords(Bishop("white", size), "c", 1)
        self.set_figure_to_coords(Bishop("white", size), "f", 1)
        self.set_figure_to_coords(Bishop("black", size), "c", 8)
        self.set_figure_to_coords(Bishop("black", size), "f", 8)
        # Rook
        self.set_figure_to_coords(Rook("white", size), "a", 1)
        self.set_figure_to_coords(Rook("white", size), "h", 1)
        self.set_figure_to_coords(Rook("black", size), "a", 8)
        self.set_figure_to_coords(Rook("black", size), "h", 8)
        # pawns
        self.set_figure_to_coords(Pawn("white", size), "a", 2)
        self.set_figure_to_coords(Pawn("white", size), "b", 2)
        self.set_figure_to_coords(Pawn("white", size), "c", 2)
        self.set_figure_to_coords(Pawn("white", size), "d", 2)
        self.set_figure_to_coords(Pawn("white", size), "e", 2)
        self.set_figure_to_coords(Pawn("white", size), "f", 2)
        self.set_figure_to_coords(Pawn("white", size), "g", 2)
        self.set_figure_to_coords(Pawn("white", size), "h", 2)
        self.set_figure_to_coords(Pawn("black", size), "a", 7)
        self.set_figure_to_coords(Pawn("black", size), "b", 7)
        self.set_figure_to_coords(Pawn("black", size), "c", 7)
        self.set_figure_to_coords(Pawn("black", size), "d", 7)
        self.set_figure_to_coords(Pawn("black", size), "e", 7)
        self.set_figure_to_coords(Pawn("black", size), "f", 7)
        self.set_figure_to_coords(Pawn("black", size), "g", 7)
        self.set_figure_to_coords(Pawn("black", size), "h", 7)

    def make_board_to_gui(self):

        size = self.height / 8
        self.clean_board()
        print(self.board_pgn)
        # [PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING]
        peaces = range(1, 7)
        for peace in peaces:
            # white
            for places in self.board_pgn.pieces(peace, True):
                move = self.SQUARES[places]
                if peace == 1:
                    self.set_figure_to_coords(Pawn("white", size), move[0], int(move[1]))
                if peace == 2:
                    self.set_figure_to_coords(Knight("white", size), move[0], int(move[1]))
                if peace == 3:
                    self.set_figure_to_coords(Bishop("white", size), move[0], int(move[1]))
                if peace == 4:
                    self.set_figure_to_coords(Rook("white", size), move[0], int(move[1]))
                if peace == 5:
                    self.set_figure_to_coords(Queen("white", size), move[0], int(move[1]))
                if peace == 6:
                    self.set_figure_to_coords(King("white", size), move[0], int(move[1]))
            # white
            for places in self.board_pgn.pieces(peace, False):
                move = self.SQUARES[places]
                if peace == 1:
                    self.set_figure_to_coords(Pawn("black", size), move[0], int(move[1]))
                if peace == 2:
                    self.set_figure_to_coords(Knight("black", size), move[0], int(move[1]))
                if peace == 3:
                    self.set_figure_to_coords(Bishop("black", size), move[0], int(move[1]))
                if peace == 4:
                    self.set_figure_to_coords(Rook("black", size), move[0], int(move[1]))
                if peace == 5:
                    self.set_figure_to_coords(Queen("black", size), move[0], int(move[1]))
                if peace == 6:
                    self.set_figure_to_coords(King("black", size), move[0], int(move[1]))
        self.print_board()
