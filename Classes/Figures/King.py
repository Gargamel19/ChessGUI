from Classes.ImageLoader import ImageLoader
from Classes.Figure import Figure


class King(Figure):

    def __init__(self, color, size):
        il = ImageLoader
        img = [il.load("src/ChessPiecesArray.png", 1, 0, 170, size), il.load("src/ChessPiecesArray.png", 0, 0, 170, size)]
        super(King, self).__init__(img, color)