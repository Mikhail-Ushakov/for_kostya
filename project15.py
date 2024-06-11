import turtle

screen=turtle.getscreen()
t=turtle.Turtle()
# t.forward(100)
# t.left(90)
# t.forward(100)
for i in range(4):
    t.forward(50)
    t.left(90)
t.color('green')
t.begin_fill()
t.circle(100)
t.end_fill()


for i in range(35):
    t.forward(100)
    t.left(160)


screen.mainloop()