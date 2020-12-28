import random
import chess.pgn

class PGNReader:

    board_gui = None
    games = []


    def __init__(self, board_gui):
        self.board_gui = board_gui
        pgn = open("C:\\Users\\trend\\PycharmProjects\\ChessGUI\\src\\file.pgn")

        game = chess.pgn.read_game(pgn)
        while game is not None:
            self.games.append(game)
            game = chess.pgn.read_game(pgn)

    def read_random(self):

        rand_index = random.randrange(len(self.games))
        game = self.games[rand_index]

        board = game.board()

        moves = []

        for move in game.mainline_moves():
            moves.append(move)

        rand_index = random.randrange(len(moves))
        if self.board_gui.white_bottom:
            if rand_index % 2 != 0:
                if rand_index == 0:
                    rand_index = rand_index + 1
                else:
                    rand_index = rand_index - 1
        else:
            if rand_index % 2 != 1:
                if rand_index == 0:
                    rand_index = rand_index + 1
                else:
                    rand_index = rand_index - 1
        for x in range(len(moves)):
            if rand_index == x:
                break
            board.push(moves[x])
        next_move = moves[rand_index:]
        return [board, next_move]
