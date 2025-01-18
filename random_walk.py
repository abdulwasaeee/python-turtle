from turtle import Turtle,Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim=Turtle()
screen=Screen()
tim.shape("turtle")
tim.color("green")
tim.pensize(10)
tim.speed(10)

for _ in range(100):
    tim.pencolor(random.choice(colours))
    tim.forward(30)
    tim.right(random.choice([0,90,180,270]))


screen.exitonclick()
