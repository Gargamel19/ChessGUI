from Classes.ImageLoader import ImageLoader
from Classes.Figure import Figure


class Bishop(Figure):

    def __init__(self, color):
        il = ImageLoader
        img = [il.load("src/ChessPiecesArray.png", 0, 4, 60), il.load("src/ChessPiecesArray.png", 1, 4, 60)]
        super(Bishop, self).__init__(img, color)
