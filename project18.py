import turtle
screen=turtle.getscreen()
t=turtle.Turtle()
t.penup()
t.goto(-100,100)
t.begin_fill()
t.color('grey')
t.pendown()
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(100)
t.end_fill()
t.penup()
t.goto(-100,-20)
t.pendown()
t.begin_fill()
t.color('black')






screen.mainloop()