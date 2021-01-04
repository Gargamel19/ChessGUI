class Square:
    heigth = 0
    color_code = ""
    color_code_green = "#DAF7A6"
    color = "white"
    content = None
    positionX = 1
    positionA = 1
    green = False

    def __init__(self, color, x, a, heigth):
        self.heigth = heigth
        self.color = color
        self.positionX = x
        self.positionA = a

    def draw_square(self, color, color_code, canvas):
        self.color_code = color_code
        square = canvas.create_rectangle(self.positionX * (self.heigth / 8),
                                self.positionA * (self.heigth / 8),
                                self.positionX * (self.heigth / 8) + (self.heigth / 8),
                                self.positionA * (self.heigth / 8) + (self.heigth / 8),
                                outline=color, fill=color)
        if self.green:
            green_square = canvas.create_rectangle(self.positionX * (self.heigth / 8),
                                             self.positionA * (self.heigth / 8),
                                             self.positionX * (self.heigth / 8) + (self.heigth / 8),
                                             self.positionA * (self.heigth / 8) + (self.heigth / 8),
                                             outline=self.color_code_green, fill=self.color_code_green)
            canvas.tag_lower(green_square)
        canvas.tag_lower(square)
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
