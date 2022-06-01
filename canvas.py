# Drawing in tkinter
from tkinter import *

root=Tk()
canvas =Canvas(root,height=100,width=200)
canvas.pack()

line=canvas.create_line(0,0,140,100)

root.mainloop()