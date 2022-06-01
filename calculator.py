from tkinter import *
import tkinter.messagebox
import parser
import math
root =Tk()
root.title("Calculator")


# input field
enter=Entry(root)
enter.grid(row=0,columnspan=5,sticky=W+E,padx=5,pady=5)
i=0
def get_variables(num):
    global i
    enter.insert(i,num)
    i+=1
def clear_all():
    enter.delete(0,END)

def undo():
    if len(enter.get()):
        newstring = enter.get()[:-1]
        clear_all()
        enter.insert(0,newstring)
    else:
        clear_all()
def get_operation(operator):
    global i
    enter.insert(i,operator)
    i+=len(operator)

def calculate():
    entire_string = enter.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        enter.insert(0,result)
    except Exception:
        clear_all()
        enter.insert(0,"Error")
def fact():
    entire_string=enter.get()
    
    if len(entire_string):
        try:
            x=int(entire_string)
            y=math.factorial(x)
            clear_all()
            enter.insert(0,str(y))
        except Exception:
            tkinter.messagebox.showinfo("Alert","Invalid Operation!")
    else:
        clear_all()
def ten_power():
    entire_string=enter.get()
    
    if len(entire_string):
        try:
            x=float(entire_string)
            y=10**x
            clear_all()
            enter.insert(0,str(y))
        except Exception:
            tkinter.messagebox.showinfo("Alert","Invalid Operation!")
    else:
        clear_all()
def log():
    entire_string=enter.get()
    
    if len(entire_string):
        try:
            x=float(entire_string)
            y=math.log10(x)
            clear_all()
            enter.insert(0,str(y))
        except Exception:
            tkinter.messagebox.showinfo("Alert","Invalid Operation!")
    else:
        clear_all()
def ln():
    entire_string=enter.get()
    
    if len(entire_string):
        try:
            x=float(entire_string)
            y=math.log(x)
            clear_all()
            enter.insert(0,str(y))
        except Exception:
            tkinter.messagebox.showinfo("Alert","Invalid Operation!")
    else:
        clear_all()
def negation():
    entire_string=enter.get()
    if len(entire_string):
        try:
            x=float(entire_string)
            y=(-1)*float(entire_string)
            clear_all()
            enter.insert(0,str(y))
        except Exception:
            tkinter.messagebox.showinfo("Alert","Invalid operation!")
    else:
        clear_all()
# 1st row
Button(root,text="x^2",width=10,command = lambda : get_operation('**2')).grid(row=1,column=0)
Button(root,text="pi",width=10,command = lambda : get_operation('*3.14')).grid(row=1,column=1)
Button(root,text="e",width=10,command = lambda : get_operation('*2.71')).grid(row=1,column=2)
Button(root,text="AC",width=10,command=clear_all).grid(row=1,column=3)
Button(root,text="del",width=10,command=undo).grid(row=1,column=4)

# 2nd row
Button(root,text="x^1/2",width=10,command = lambda : get_operation('**0.5')).grid(row=2,column=0)
Button(root,text="(",width=10,command = lambda : get_operation('(')).grid(row=2,column=1)
Button(root,text=")",width=10,command = lambda : get_operation(')')).grid(row=2,column=2)
Button(root,text="x!",width=10,command = lambda : fact()).grid(row=2,column=3)
Button(root,text="/",width=10,command = lambda : get_operation('/')).grid(row=2,column=4)

# 3rd row
Button(root,text="x^y",width=10,command = lambda : get_operation('**')).grid(row=3,column=0)
Button(root,text="7",width=10,command=lambda :get_variables(7)).grid(row=3,column=1)
Button(root,text="8",width=10,command=lambda :get_variables(8)).grid(row=3,column=2)
Button(root,text="9",width=10,command=lambda :get_variables(9)).grid(row=3,column=3)
Button(root,text="*",width=10,command = lambda : get_operation('*')).grid(row=3,column=4)

# 4th row
Button(root,text="10^x",width=10,command = lambda : ten_power()).grid(row=4,column=0)
Button(root,text="4",width=10,command=lambda :get_variables(4)).grid(row=4,column=1)
Button(root,text="5",width=10,command=lambda :get_variables(5)).grid(row=4,column=2)
Button(root,text="6",width=10,command=lambda :get_variables(6)).grid(row=4,column=3)
Button(root,text="-",width=10,command = lambda : get_operation('-')).grid(row=4,column=4)

# 5th row
Button(root,text="log",width=10,command = lambda : log()).grid(row=5,column=0)
Button(root,text="1",width=10,command=lambda :get_variables(1)).grid(row=5,column=1)
Button(root,text="2",width=10,command=lambda :get_variables(2)).grid(row=5,column=2)
Button(root,text="3",width=10,command=lambda :get_variables(3)).grid(row=5,column=3)
Button(root,text="+",width=10,command = lambda : get_operation('+')).grid(row=5,column=4)

# last row
Button(root,text="ln",width=10,command = lambda : ln()).grid(row=6,column=0)
Button(root,text="+/-",width=10,command = lambda : negation()).grid(row=6,column=1)
Button(root,text="0",width=10,command=lambda :get_variables(0)).grid(row=6,column=2)
Button(root,text=".",command = lambda : get_operation('.'),width=10).grid(row=6,column=3)
Button(root,text="=",command = calculate,width=10).grid(row=6,column=4)

root.mainloop()