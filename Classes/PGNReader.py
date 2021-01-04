import random
import chess.pgn
from tkinter.filedialog import askopenfilename

class PGNReader:

    board_gui = None
    games = []


    def __init__(self, board_gui):
        self.board_gui = board_gui
        filename = askopenfilename()
        pgn = open(filename)

        game = chess.pgn.read_game(pgn)
        while game is not None:
            self.games.append(game)
            game = chess.pgn.read_game(pgn)

    def read_random(self):

        rand_index = random.randrange(len(self.games))
        game = self.games[rand_index]

        board = game.board()

        moves = []
        for move in game.mainline():
            moves.append({"move": move.move, "comment": move.comment})
            print(move.starting_comment)

        rand_index = random.randrange(len(moves))
        for x in range(len(moves)):
            if rand_index == x:
                break
            board.push(moves[x]["move"])
        print(len(board.move_stack))
        if self.board_gui.white_bottom:
            if len(board.move_stack) % 2 == 0:
                if len(board.move_stack) == rand_index:
                    rand_index = rand_index - 1
                    board.pop()
                else:
                    rand_index = rand_index + 1
                    board.push(moves[rand_index]["move"])
        else:
            if len(board.move_stack) % 2 == 1:
                if len(board.move_stack) == rand_index:
                    rand_index = rand_index - 1
                    board.pop()
                else:
                    rand_index = rand_index + 1
                    board.push(moves[rand_index]["move"])

        print(len(board.move_stack))
        next_move = moves[rand_index:]
        print(board)
        return [board, next_move]
