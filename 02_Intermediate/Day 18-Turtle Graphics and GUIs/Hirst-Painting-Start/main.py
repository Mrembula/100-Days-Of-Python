# ##This code will not work in repl.it as there is no access to the colorgram package here.###
# #We talk about this in the video tutorials##
# import colorgram
#
# RGB_colors = []
# colors = colorgram.extract('image.jpg', 50)
#
# for i in range(len(colors)):
#     color = colors[i].rgb
#     RGB_colors.append(color[0:])
#
# print(RGB_colors)
import turtle
from turtle import Turtle, Screen
import random
point = Turtle()
turtle.colormode(255)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]

move_range = 10
point.penup()
for i in range(move_range):
    point.setposition(-300, ((i * 30) - 100))
    for _ in range(move_range):
        point.dot(15, random.choice(color_list))
        point.forward(50)

point.hideturtle()





screen = Screen()
screen.exitonclick()