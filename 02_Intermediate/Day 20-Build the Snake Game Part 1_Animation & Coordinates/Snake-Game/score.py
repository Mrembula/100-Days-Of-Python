from turtle import Turtle
ALIGNMENT = 'CENTER'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.highscore = int(self.read_file())
        self.hideturtle()
        self.penup()
        self.setposition(0, 260)
        self.update_score()

    def reset(self):
        if self.highscore < self.score:
            with open('data.txt', 'w') as file:
                self.highscore = self.score
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.highscore}', False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def read_file(self):
        with open('data.txt', 'r') as file:
            return file.read()