from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def anti_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='a', fun=anti_clockwise)
screen.onkey(key='c', fun=clear)
screen.exitonclick()

