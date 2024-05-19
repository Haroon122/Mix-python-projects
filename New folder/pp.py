from tkinter import*
from tkinter import messagebox
win=Tk()
global num
num=int()
def even():
   
    if(num%2==0):
        messagebox.showinfo("","The Number is Even")   
    else:
        messagebox.showinfo("The Number is ODD") 
         


Label(win,text="Enter a Number").place(x=5,y=5)
Entry(win,textvariable=num).place(x=30,y=30)
Button(text="check",command=even).place(x=70,y=50)

win.mainloop()