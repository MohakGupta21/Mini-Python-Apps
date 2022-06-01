from tkinter import *
class Window:
    def __init__(self,root):
        self.window = Frame(root,height=200,width=200)
        self.label1=Label(self.window,text="Enter your name: ")
        self.entry1=Entry(self.window)
        self.label1.grid(row=0,column=0,padx=10,pady=10)
        self.entry1.grid(row=0,column=1,padx=10,pady=10)
        self.label2=Label(self.window,text="Enter your number: ")
        self.entry2=Entry(self.window)
        self.label2.grid(row=1,column=0,padx=10,pady=10)
        self.entry2.grid(row=1,column=1,padx=10,pady=10)

        self.submit = Button(self.window,text="Submit",bd=1,command=self.funct1)
        self.submit.grid(row=3,column=0,columnspan=2)
        self.window.pack()
    def funct1(self):
        print("Name: "+self.entry1.get())
        print("Number: "+self.entry2.get())
        

root = Tk()
app1=Window(root)
root.mainloop()