import turtle
from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def mf():
    tim.forward(100)

def mb():
    tim.backward(100)

def cc():
    tim.left(10)

def c():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(key="w",fun=mf)
screen.onkey(key="s",fun=mb)
screen.onkey(key="a",fun=cc)
screen.onkey(key="d",fun=c)
screen.onkey(key="c",fun=clear)

screen.exitonclick()
