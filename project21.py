from tkinter import *
root=Tk()
def click_handler():
    a=my_label.get()
    my_label.delete(0,END)
    my_label.insert(0,int(a)+1)
btn=Button(root,text='Click Me!',command=click_handler)
btn.pack()
my_label=Entry(root,text=0)
my_label.pack()
root.mainloop()