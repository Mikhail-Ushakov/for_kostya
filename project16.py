
if __name__=='__main__':
    import turtle



    screen=turtle.getscreen()
    t=turtle.Turtle()
class DrawShape:
    def draw(self, color='red'):
        if self.fill:
            t.color(color)
            t.begin_fill()
        for _ in range(self.sides):
            t.forward(self.size)
            t.left(self.angle)
        if self.fill:
            t.end_fill()
class Rect(DrawShape):
    def __init__(self,size,fill=False):
        self.size=size
        self.sides=4
        self.angle=90
        self.fill=fill
class Triangle(DrawShape):
    def __init__(self,size,fill=False):
        self.size=size
        self.sides=3
        self.angle=120
        self.fill=fill
# triangle=Triangle(120,fill=True)
# triangle.draw()

# rect=Rect(60,fill=True)
# rect.draw()
if __name__=='__main__':

    rect=Rect(40,fill=True)
    rect.draw(color='green')
    t.goto(0,40)
    rect.draw(color='yellow')
    t.goto(0,80)
    rect.draw(color='red')

    screen.mainloop()

