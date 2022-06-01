from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("Newfile")
def function1():
    popup=tkinter.messagebox.askquestion("Question1","Do you like tea?")
    if popup == "yes":
        print("You like tea")
    else:
        print("You don't like tea")
mymenu =Menu(root)
root.config(menu=mymenu)
submenu =Menu(mymenu)
submenu.add_command(label ="Project",command = lambda :print("Menu Item Clicked"))
submenu.add_command(label ="File",command = lambda :print("Menu Item Clicked"))
submenu.add_separator()
submenu.add_command(label="Window",command=lambda :print("Menu Item Clicked"))
submenu.add_command(label="Help",command=lambda :print("Menu Item Clicked"))
mymenu.add_cascade(label="File",menu=submenu)

submenu2 =Menu(mymenu)
submenu2.add_command(label = "Save",command = lambda:print("Menu Item Clicked"))
submenu2.add_command(label="Reset",command= lambda:tkinter.messagebox.showinfo("Title","Resetted successfully!"))
mymenu.add_cascade(label="Edit",menu=submenu2)
mymenu.add_command(label="Question",command = function1)

# Status bar
status = Label(text="This is a status bar", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()