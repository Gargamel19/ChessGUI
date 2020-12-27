from Classes.ImageLoader import ImageLoader
from Classes.Figure import Figure


class King(Figure):

    def __init__(self, color):
        il = ImageLoader
        img = [il.load("src/ChessPiecesArray.png", 0, 1, 60), il.load("src/ChessPiecesArray.png", 1, 1, 60)]
        super(King, self).__init__(img, color)