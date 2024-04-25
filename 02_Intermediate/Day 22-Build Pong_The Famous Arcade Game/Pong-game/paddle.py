from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.player = position
        self.create_puddle()

    def create_puddle(self):
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(self.player[0], self.player[1])
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        change_position = self.ycor() + MOVE_DISTANCE
        self.goto(self.player[0], change_position)

    def move_down(self):
        change_position = self.ycor() - MOVE_DISTANCE
        self.goto(self.player[0], change_position)
