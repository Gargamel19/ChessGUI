import math
import tkinter as tk

from chess import Move


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

            before_x = math.floor(event.x / self.height)
            before_a = math.floor(event.y / self.height)

            [start_a, start_x] = self.board.get_coordinate_from_square(self.x, self.y)
            [goal_a, goal_x] = self.board.get_coordinate_from_square(before_x, before_a)

            print(start_a+str(start_x)+goal_a+str(goal_x))
            move = Move.from_uci(start_a+str(start_x)+goal_a+str(goal_x))
            print(1)
            if move in self.board.board_pgn.legal_moves:
                self.board.board_pgn.push(move)
            print(2)
            self.board.make_board_to_gui()
            print(3)
            self.board.check_if_right()
            print(4)

        return

    def draw(self, x, y, canvas, height):
        self.canvas = canvas
        self.height = height
        if self.color == "white":
            image = self.img[1]
        else:
            image = self.img[0]

        self.tkinterID = canvas.create_image(x, y, image=image, anchor="nw")
        canvas.tag_raise(self.tkinterID)
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

    def destroy(self):
        self.canvas.delete(self.tkinterID)

