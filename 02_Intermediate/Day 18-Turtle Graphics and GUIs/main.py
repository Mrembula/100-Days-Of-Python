import random
import turtle as t
from turtle import Turtle, Screen

tim = Turtle()
t.colormode(255)


def random_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return (R, G, B)

# shapes
'''for shape in range(3, 11):
    angle = 360 / shape
    for _ in range (shape):
        tim.color(random.choice(colors))
        tim.forward(100)
        tim.right(angle)

directions = [0, 90, 180, 270, 360]
tim.width(13)
for _ in range(50):
    tim.forward(30)
    tim.color(random_color())
    tim.setheading(random.choice(directions))'''


tim.speed('fastest ')
def draw_circle(num_of_gap):
    for i in range(int((360/num_of_gap))):
        tim.color(random_color())
        tim.circle(100)
        tim.right(num_of_gap)


def draw_spirograph(size_of_graph):
 for i in range(int((360/size_of_graph))):
    tim.color(random_color())
    tim.circle(100)
    print(tim.xcor() + 10)
    tim.setheading(tim.heading() + 10)

draw_circle(5)


screen = Screen()
screen.exitonclick()
