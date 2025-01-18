import colorgram
from turtle import Turtle,Screen
import turtle
import random

turtle.colormode(255)
colors=colorgram.extract('hist.jpg',25)
colorlist=[]

for i in colors:
    r=i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    c=(r,g,b)
    colorlist.append(c)
    
screen=Screen()
tim=Turtle()
tim.hideturtle()

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

for i in range(100):
    if i%10==0 and i!=0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
    tim.pendown()
    tim.dot(30, random.choice(colorlist))
    tim.penup()
    tim.forward(50)

screen.exitonclick()
