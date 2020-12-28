from Classes.ImageLoader import ImageLoader
from Classes.Figure import Figure


class Pawn(Figure):

    def __init__(self, color, size):
        il = ImageLoader
        img = [il.load("src/ChessPiecesArray.png", 0, 5, 60, size), il.load("src/ChessPiecesArray.png", 1, 5, 60, size)]
        super(Pawn, self).__init__(img, color)
