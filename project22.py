from tkinter import *

root=Tk()

canvas=Canvas(root, width=600, height=600)
canvas.pack()
canvas.create_rectangle(100,100,250,250)
canvas.create_rectangle(50,50,200,200)
canvas.create_line(50,50,100,100)
canvas.create_line(250,250,200,200)
canvas.create_line(100,250,50,200)
canvas.create_line(200,50,250,100)
root.mainloop()