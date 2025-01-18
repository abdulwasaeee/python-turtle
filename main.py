from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")

colors = ["blue", "lime green", "yellow", "red", "pink", "orange", "purple", "indigo", "maroon", "cyan"]


def draw_shape(sides):
    tim.pencolor(random.choice(colors))
    for i in range(sides):
        angle = 360 / sides
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    draw_shape(i)

screen=Screen()
screen.exitonclick()
