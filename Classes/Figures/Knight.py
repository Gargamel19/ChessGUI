from Classes.ImageLoader import ImageLoader
from Classes.Figure import Figure


class Knight(Figure):

    def __init__(self, color, size):
        il = ImageLoader
        img = [il.load("src/ChessPiecesArray.png", 1, 3, 170, size), il.load("src/ChessPiecesArray.png", 0, 3, 170, size)]
        super(Knight, self).__init__(img, color)
