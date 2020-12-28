from Classes.ImageLoader import ImageLoader
from Classes.Figure import Figure


class Bishop(Figure):

    def __init__(self, color, size):
        il = ImageLoader
        img = [il.load("src/ChessPiecesArray.png", 1, 2, 170, size), il.load("src/ChessPiecesArray.png", 0, 2, 170, size)]
        super(Bishop, self).__init__(img, color)
