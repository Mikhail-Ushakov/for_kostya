import turtle
from random import randint
from project16 import Rect
screen=turtle.getscreen()
t=turtle.Turtle()
a=Rect(8,True)

t.pensize(20)
t.color('brown')
t.circle(100)

t.begin_fill()
t.pensize(20)
t.goto(0,20)
t.color('yellow')
t.circle(80)
t.end_fill()

t.pensize(1)
for i in range(10):
    t.penup()
    t.goto(0,100)
    t.color('red')
    t.left(randint(1,360))
    t.forward(randint(5,95))
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

for i in range(10):
    t.penup()
    t.goto(0,100)
    t.color('red')
    t.left(randint(1,360))
    t.forward(randint(5,95))
    t.pendown()
    t.begin_fill()
    a.draw('green')
    t.end_fill()

screen.mainloop()
