from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import filedialog
win  = Tk()
img = PhotoImage(file="pp.png")
win.geometry("1000x500")
def popup():
    file = filedialog.askopenfilename()
Button(win,image=img,command=popup).place(x=30,y=150)


win.mainloop()