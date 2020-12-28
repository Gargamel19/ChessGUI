class Square:
    heigth = 0
    color_code = ""
    color = "white"
    content = None
    positionX = 1
    positionA = 1

    def __init__(self, color, x, a, heigth):
        self.heigth = heigth
        self.color = color
        self.positionX = x
        self.positionA = a

    def draw_square(self, color, color_code, canvas):
        self.color_code = color_code
        canvas.create_rectangle(self.positionX * (self.heigth / 8),
                                self.positionA * (self.heigth / 8),
                                self.positionX * (self.heigth / 8) + (self.heigth / 8),
                                self.positionA * (self.heigth / 8) + (self.heigth / 8),
                                outline=color, fill=color)
        if self.content != None:
            if self.content.alive:
                self.content.draw(self.positionX * (self.heigth / 8), self.positionA * (self.heigth / 8), canvas, self.heigth/ 8)

    def draw_content_in_square(self, canvas):
        canvas.create_rectangle(self.positionX * (self.heigth / 8),
                                self.positionA * (self.heigth / 8),
                                self.positionX * (self.heigth / 8) + (self.heigth / 8),
                                self.positionA * (self.heigth / 8) + (self.heigth / 8),
                                outline=self.color_code, fill=self.color_code)
        if self.content != None:
            if self.content.alive:
                self.content.draw(self.positionX * (self.heigth / 8), self.positionA * (self.heigth / 8), canvas, self.heigth/ 8)
