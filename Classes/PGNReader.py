import random
import chess.pgn
from Classes.Figures.Queen import Queen
from Classes.Figures.King import King
from Classes.Figures.Pawn import Pawn
from Classes.Figures.Rook import Rook
from Classes.Figures.Bishop import Bishop
from Classes.Figures.Knight import Knight


class PGNReader:


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

    def read(self, board_gui, size):
        pgn = open("C:\\Users\\FerdinandTrendelenbu\\PycharmProjects\\ChessGUI\\src\\file.pgn")

        games = []
        game = chess.pgn.read_game(pgn)
        while game is not None:
            games.append(game)
            game = chess.pgn.read_game(pgn)

        rand_index = random.randrange(len(games))
        game = games[rand_index]

        board = game.board()

        moves = []
        for move in game.mainline_moves():
            moves.append(move)

        rand_index = random.randrange(len(moves))
        for x in range(len(moves)):
            if rand_index == x:
                break
            board.push(moves[x])

        # [PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING]
        peaces = range(1, 7)
        for peace in peaces:
            # white
            for places in board.pieces(peace, True):
                move = self.SQUARES[places]
                if peace == 1:
                    board_gui.set_figure_to_coords(Pawn("white", size), move[0], int(move[1]))
                if peace == 2:
                    board_gui.set_figure_to_coords(Knight("white", size), move[0], int(move[1]))
                if peace == 3:
                    board_gui.set_figure_to_coords(Bishop("white", size), move[0], int(move[1]))
                if peace == 4:
                    board_gui.set_figure_to_coords(Rook("white", size), move[0], int(move[1]))
                if peace == 5:
                    board_gui.set_figure_to_coords(Queen("white", size), move[0], int(move[1]))
                if peace == 6:
                    board_gui.set_figure_to_coords(King("white", size), move[0], int(move[1]))
            # white
            for places in board.pieces(peace, False):
                move = self.SQUARES[places]
                if peace == 1:
                    board_gui.set_figure_to_coords(Pawn("black", size), move[0], int(move[1]))
                if peace == 2:
                    board_gui.set_figure_to_coords(Knight("black", size), move[0], int(move[1]))
                if peace == 3:
                    board_gui.set_figure_to_coords(Bishop("black", size), move[0], int(move[1]))
                if peace == 4:
                    board_gui.set_figure_to_coords(Rook("black", size), move[0], int(move[1]))
                if peace == 5:
                    board_gui.set_figure_to_coords(Queen("black", size), move[0], int(move[1]))
                if peace == 6:
                    board_gui.set_figure_to_coords(King("black", size), move[0], int(move[1]))
        print(board)