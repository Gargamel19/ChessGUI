import math
import tkinter as tk


class Figure:

    img = []
    alive = True
    color = "white"
    height = -1
    buttonPressed = False
    tkinterID = -1
    canvas = None
    lastx = -1
    lasty = -1
    y = None
    x = None
    board = None

    def __init__(self, img, color):
        self.img = img
        self.color = color


    def motion(self, event):
        if self.buttonPressed:
            self.canvas.move(self.tkinterID, event.x - self.lastx, event.y - self.lasty)
            self.lastx = event.x
            self.lasty = event.y
            #print("Mouse position: (%s %s)" % (event.x, event.y))

        return

    def button(self, event):
        print(event)
        if event.num == 1:
            self.canvas.tag_raise(self.tkinterID)
            self.buttonPressed = True
            self.lastx = event.x
            self.lasty = event.y

        return

    def button_release(self, event):
        print(event)
        if event.num == 1:
            self.buttonPressed = False
            self.board.squares[self.x][self.y].content = None
            self.canvas.delete(self.tkinterID)
            before_x = math.floor(event.x / self.height)
            before_a = math.floor(event.y / self.height)
            [a, x] = self.board.get_coordinate_from_square(before_x, before_a)
            self.board.set_figure_to_coords(self, a, x)
            self.board.squares[before_x][before_a].draw_content_in_square(self.canvas)


        return



    def draw(self, x, y, canvas, heigth):
        self.canvas = canvas
        self.height = heigth
        if self.color == "white":
            image = self.img[1]
        else:
            image = self.img[0]



        self.tkinterID = canvas.create_image(x, y, image=image, anchor="nw")
        canvas.tag_bind(self.tkinterID, '<Motion>', self.motion)
        canvas.tag_bind(self.tkinterID, '<Button>', self.button)
        canvas.tag_bind(self.tkinterID, '<ButtonRelease>', self.button_release)


    def is_between(self, original, border_low, border_high):
        if original > border_low:
            if original < border_high:
                return True
        return False

    def set_square(self, x, y):
        self.x = x
        self.y = y

    def set_board(self, board):
        self.board = board