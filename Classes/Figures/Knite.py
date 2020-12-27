from Classes.ImageLoader import ImageLoader
from Classes.Figure import Figure


class Knite(Figure):

    def __init__(self, color):
        il = ImageLoader
        img = [il.load("src/ChessPiecesArray.png", 0, 3, 60), il.load("src/ChessPiecesArray.png", 1, 3, 60)]
        super(Knite, self).__init__(img, color)
