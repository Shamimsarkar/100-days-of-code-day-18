import turtle
from turtle import Turtle, Screen
import random

direction = [0, 90, 180, 270]
tim = Turtle()
turtle.colormode(255)
tim.shape("classic")

tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)

    return colors

print(random_color())

def til_circle(angle):
    for i in range(int(360/angle)):
        tim.pensize(100)
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + angle)

til_circle(20)


























screen = Screen()
screen.exitonclick()