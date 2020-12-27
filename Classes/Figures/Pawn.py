from Classes.ImageLoader import ImageLoader
from Classes.Figure import Figure


class Pawn(Figure):

    def __init__(self, color):
        il = ImageLoader
        img = [il.load("src/ChessPiecesArray.png", 0, 5, 60), il.load("src/ChessPiecesArray.png", 1, 5, 60)]
        super(Pawn, self).__init__(img, color)
