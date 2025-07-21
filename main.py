import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
list_of_colors = [ (219, 173, 124), (159, 180, 190), (134, 73, 53), (49, 102, 153),  (118, 82, 93), (179, 140, 150), (41, 46, 65), (162, 104, 151), (126, 173, 114), (83, 96, 183), (67, 9, 27), (238, 241, 245), (81, 133, 107), (231, 188, 138), (52, 62, 79), (195, 90, 72), (116, 43, 58), (60, 41, 28), (92, 144, 117), (70, 67, 52), (182, 187, 207), (211, 181, 189), (102, 51, 38), (174, 199, 203), (181, 201, 180), (210, 184, 180), (41, 73, 82)]


for count_dot in range(1, 101):

    tim.dot(20, random.choice(list_of_colors))
    tim.forward(50)

    if count_dot % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()