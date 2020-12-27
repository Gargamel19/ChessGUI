class Figure:

    img = []
    alive = True
    color = "white"

    def __init__(self, img, color):
        self.img = img
        self.color = color

    def draw(self, x, y, canvas):
        if self.color == "white":
            image = self.img[1]
        else:
            image = self.img[0]
        canvas.create_image(x, y, image=image, anchor="nw")