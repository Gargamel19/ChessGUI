from Classes.ImageLoader import ImageLoader
from Classes.Figure import Figure


class Rook(Figure):

    def __init__(self, color):
        il = ImageLoader
        img = [il.load("src/ChessPiecesArray.png", 0, 2, 60), il.load("src/ChessPiecesArray.png", 1, 2, 60)]
        super(Rook, self).__init__(img, color)

