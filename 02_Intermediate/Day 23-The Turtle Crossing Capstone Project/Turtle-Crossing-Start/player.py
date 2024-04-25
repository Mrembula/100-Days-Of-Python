from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        move_forward = self.ycor() + MOVE_DISTANCE
        self.goto(STARTING_POSITION[0], move_forward)

    def move_down(self):
        move_backward = self.ycor() - MOVE_DISTANCE
        self.goto(STARTING_POSITION[0], move_backward)

    def reached_top(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        return False
