from Classes.ImageLoader import ImageLoader
from Classes.Figure import Figure


class Rook(Figure):

    def __init__(self, color, size):
        il = ImageLoader
        img = [il.load("src/ChessPiecesArray.png", 1, 4, 170, size), il.load("src/ChessPiecesArray.png", 0, 4, 170, size)]
        super(Rook, self).__init__(img, color)

