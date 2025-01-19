import random
from turtle import Turtle,Screen

race=True
screen=Screen()
screen.setup(width=500,height=400)
bet=screen.textinput(title="race",prompt="what color wins? ")
positions=[-70,-40,-10,20]
colors=["red","green","blue","yellow"]
players=[]

for i in range(4):
    tim=Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230,y=positions[i])
    players.append(tim)

while race:
    for i in players:
     d=random.randint(0,10)
     i.forward(d)
     if i.xcor()>230:
         print(f"{i.pencolor()} wins!")
         race=False
         if i.pencolor==bet:
          print("You won the bet!")
         else:
           print("you lost the bet")











screen.exitonclick()

