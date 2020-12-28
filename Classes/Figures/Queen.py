from Classes.ImageLoader import ImageLoader
from Classes.Figure import Figure


class Queen(Figure):

    def __init__(self, color, size):
        il = ImageLoader
        img = [il.load("src/ChessPiecesArray.png", 1, 1, 170, size), il.load("src/ChessPiecesArray.png", 0, 1, 170, size)]
        super(Queen, self).__init__(img, color)


